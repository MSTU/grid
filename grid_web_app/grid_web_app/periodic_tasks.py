from __future__ import absolute_import

from celery import Celery
import os
from celery.result import AsyncResult
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grid_web_app.settings')

app = Celery('periodic_tasks')
#app.config_from_object('celeryconfig')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object(settings)
#app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# imports from django must be after config Celery
from grid_frontend.models import Job, Task

import multigrid.debug as debug

logger = debug.logger

@app.task
def check_results():
	# Get all unfinished tasks
	all_job_tasks = Task.objects.filter(is_finished=False)
	# Get results if it's ready
	for task in all_job_tasks:
		async_result = AsyncResult(task.task_id)
		if async_result.ready():
			#task.result = async_result.get().result_params
			task.is_finished = True
			task.save()
			logger.info("Task " + task.task_id + " finished")

	# Check if Job finished
	for job in Job.objects.filter(status__lt=1.0):
		all_job_tasks = job.task_set.all()
		finished_tasks_count = 0
		# Job can be finished if it had at least on Task
		# Count finished tasks rate
		if all_job_tasks.count():
			is_finished = True
		else:
			is_finished = False
		for task in all_job_tasks:
			if task.is_finished:
				is_finished &= True
				finished_tasks_count += 1
			else:
				is_finished &= False

		job.status = float(finished_tasks_count)/all_job_tasks.count() if all_job_tasks.count() > 0.0 else 0.0

		if is_finished:
			job.status = 1.0
			logger.info("Job " + job.name + " is finished")
			print 'sdf'

		job.save()