# -*- coding: utf-8 -*-
import os
import json
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from django.db import models
from django.http import Http404, HttpResponse
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect

from grid_frontend import util

from grid_frontend.models import Job, MathModel, Loadcase, Task

from multigrid.loadcases.modelicaloadcase import ModelicaLoadcase
from multigrid.solvers.pythonsolver import PythonSolver
from multigrid.solvers.modelicasolver import ModelicaSolver
from multigrid.modelgrid import ModelGrid

import logging

logger = logging.getLogger('multigrid_web_app')

@login_required
def get_main(request):
	return redirect('/jobs/')


def register(request):
	if request.method == 'GET':
		return TemplateResponse(request, 'register.html')

	data, errors = {}, {}
	name = request.POST.get('username', 0)
	email = request.POST.get('email', 0)
	pass1 = request.POST.get('password1', 0)
	pass2 = request.POST.get('password2', 0)
	if name:
		data['name'] = name
	else:
		errors['name'] = u'Логин пользователя не введен'
	if email:
		data['email'] = email
	else:
		errors['email'] = u'Email пользователя не введен'

	if not pass1 or not pass2:
		errors['password'] = u'Пароль пользователя не введен'
	elif pass1 != pass2:
		errors['password'] = u'Введенный пароль не совпадает'

	if errors.keys():
		return TemplateResponse(request, 'register.html', {'errors': errors, 'data': data})

	user = User.objects.create_user(name, email, pass1)
	user.save()
	user = authenticate(username=name, password=pass1)
	if user.is_active:
		auth_login(request, user)
		return redirect("/jobs/")
	else:
		return HttpResponse("<html><body>Everything is BAD</body></html>")


def login(request):
	if request.method == 'GET':
		return TemplateResponse(request, 'login.html')

	data, errors = {}, {}
	username = request.POST.get('username', 0)
	password = request.POST.get('password', 0)
	user = None

	if not username:
		errors['username'] = u'Логин не введен'
	elif not password:
		errors['password'] = u'Пароль не введен'
	else:
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
			else:
				errors['data'] = u'Не верный логин или пароль'
		else:
			errors['data'] = u'Не верный логин или пароль'

	data['username'] = username

	if errors.keys():
		return TemplateResponse(request, 'login.html', {'errors': errors, 'data': data})
	else:
		return redirect('/jobs/')


def logout(request):
	auth_logout(request)
	return TemplateResponse(request, "logout.html")


@login_required
def jobs_list(request):
	all_jobs, errors, data, num_jobs = {}, {}, {}, {}
	#num_paginator = Jobs.objects.filter(user=request.user).count()
	all_jobs = Job.objects.filter(user=request.user).order_by("-date")

	paginator = Paginator(all_jobs, 8)
	page = request.GET.get('page')

	try:
		data = paginator.page(page)
	except PageNotAnInteger:
		data = paginator.page(1)
	except EmptyPage:
		data = paginator.page(paginator.num_pages)

	return TemplateResponse(request, 'jobs.html',
							{'errors': errors, 'data': data, 'num_pages': xrange(1, paginator.num_pages + 1)})


@login_required
def search_job(request):
	if request.method == 'GET':
		return redirect('/jobs/')
	else:
		data, errors, = {}, {}
		query = request.POST.get('search_q', 0)
		data = Job.objects.filter(user=request.user, name__icontains=query).order_by("-date")
		return TemplateResponse(request, 'search_jobs.html', {'errors': errors, 'data': data, 'query': query})


@login_required
def delete_job(request, job_id):
	try:
		job = Job.objects.get(user=request.user, pk=job_id)
	except Job.DoesNotExist:
		raise Http404
	job.delete()
	return redirect('/jobs/')


@login_required
def create_job(request):
	if request.method == 'GET':
		return TemplateResponse(request, 'create_job.html')
	response_data = {'status': 'fail'}
	name = request.POST.get('job_name', "")
	input_parameters = request.POST.get('input_parameters', "")
	loadcases_names = request.POST.get('loadcases').split(',')

	job = Job(name=name, user=request.user, input_params=input_parameters,
			  description=request.POST.get('job_description', ""))
	if job:
		response_data['status'] = 'ok'
		job.save()
	for lc_name in loadcases_names:
		job.loadcases.add(Loadcase.objects.get(name=lc_name))
	return redirect('/jobs/')


@login_required
def create_loadcase(request):
	response_data = {'status': 'fail'}

	name = request.POST.get('loadcase_name', "")
	description = request.POST.get('loadcase_description', "")
	model = request.POST.get('model', "")

	mathmodel = MathModel.objects.get(name=model)
	loadcase = Loadcase(name=name, description=description)
	loadcase.mathmodel = mathmodel
	if loadcase:
		response_data['status'] = 'ok'
		loadcase.save()
	return redirect('/create_job/')


@login_required
def create_model(request):
	response_data = {'status': 'fail'}
	model_type = request.POST.get('model_type', None)
	model = request.POST.get('model', "")

	file_model = request.FILES.get('file_model', None)
	if file_model:
		file_path = 'files/%s' % file_model
		default_storage.save(file_path, ContentFile(file_model.read()))
		model = file_model

	mathmodel = MathModel(name=model, type=model_type)
	if mathmodel:
		response_data['status'] = 'ok'
		mathmodel.save()
	return redirect('/create_job/')


@login_required
def edit_job(request, job_id):
	try:
		job = Job.objects.get(user=request.user, pk=job_id)
	except Job.DoesNotExist:
		raise Http404
	if request.method == 'GET':
		data = {}
		data['job'] = job
		return TemplateResponse(request, 'edit_job.html', {'data': data})
	else:
		job.name = request.POST.get('job_name', "")
		job.description = request.POST.get('job_description', "")
		job.input_params = request.POST.get('input_params', "")
		job.status = 0.0
		job.save()
		return redirect('/jobs/')


@login_required
def calc_job(request, job_id):
	job = Job.objects.get(pk=job_id)
	job.status = 0.0
	# if job recalculated delete previous calculated results
	job_tasks = job.task_set.all()
	for task in job_tasks:
		task.delete()
	job.save()

	loadcases = []
	for web_lc in job.loadcases.all():
		mathmodel = web_lc.mathmodel
		lc = None
		if mathmodel.type == PythonSolver.name:
			pass
		elif mathmodel.type == ModelicaSolver.name:
			lc = ModelicaLoadcase(mathmodel.name)
		loadcases.append(lc)

	mg = ModelGrid()
	mg.reinit()
	mg.set_loadcases(loadcases)

	input_parameters_string = job.input_params.split('|') # list of input parameters in string
	params_list = []
	for item in input_parameters_string:
		params_list.append(parse_input_params(item))

	task_ids = mg.calculate(params_list)

	for task_id, param in zip(task_ids, params_list):
		task = Task(task_id=task_id, input_params=param, job=job)
		task.save()

	return redirect('/jobs/')


@login_required
def get_job(request, job_id):
	data, errors = {}, {}
	try:
		job = Job.objects.get(user=request.user, pk=job_id)
		loadcases = job.loadcases.all()
		lc_names = [lc.name for lc in loadcases]
		#lc_names = util.decode_dict(lc_names)
		result = ', '.join([x for x in lc_names])
	except Job.DoesNotExist:
		raise Http404
	data['job'] = job
	data['loadcases'] = result
	return TemplateResponse(request, 'job.html', {'errors': errors, 'data': data})


def parse_input_params(param):
	parameter = json.loads(param, object_hook=util.decode_dict)
	return parameter