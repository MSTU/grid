# -*- coding: cp1251 -*-

#***************************************************************************
#
#    copyright            : (C) 2013 by Valery Ovchinnikov (LADUGA Ltd.)
#                                       Anton Lapshin
#                                       Anton Kargin
#    email                : laduga@laduga.com
#***************************************************************************
#***************************************************************************
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU General Public License as published by  *
#*   the Free Software Foundation; either version 2 of the License, or     *
#*   (at your option) any later version.                                   *
#*                                                                         *
#***************************************************************************/
from conf import ConfigClient
from Task import Task
from celery.result import AsyncResult

if ConfigClient.LOCAL_WORK:
	from multigrid.LocalWorker import run_task
else:
	from multigrid.Worker import run_task

class ModelGrid:
	def __init__(self, config=None):
		if config is None:
			self.config = ConfigClient.ConfigClient()
		else:
			self.config = config
		self.loadcases = []
		self.reinit()

	def set_loadcases(self, loadcases):
		self.loadcases = loadcases
		for loadcase in loadcases:
			solver = self.config.solvers[loadcase.solver]
			solver.load_data(loadcase)

	def add_loadcases(self, loadcases):
		self.loadcases.extend(loadcases)
		for i in loadcases:
			solver = self.config.solvers[i.Solver]
			solver.load_data(i)


	def get_loadcases(self):
		return self.loadcases

	def clear_loadcases(self):
		self.loadcases = []

	def calculate(self, input_list):
		"""
		For all items in input_list create Task instance and run them.
		Return ids of created Tasks
		"""
		result_ids = []
		for item in input_list:
			task = Task(self.loadcases, item)
			if not ConfigClient.LOCAL_WORK:
				self.input_tasks.append(task)
				async_result = run_task.delay(task)
				task.id = async_result.task_id
				result_ids.append(task.id)
				self.task_async_results[task] = async_result
			else:
				self.ready_tasks.append(run_task(task))
		return result_ids

	def wait_tasks(self, task_ids):
		"""
		Wait and return result of tasks with ids specified in task_ids list
		"""
		results = []
		for id in task_ids:
			async_result = AsyncResult(id)
			results.append(async_result.get())
		return results


	def wait_all(self):
		if ConfigClient.LOCAL_WORK:
			return [task.result_params for task in self.ready_tasks]
		for task in self.input_tasks:
			self.ready_tasks.append(self.task_async_results[task].get())
		result_list = [task.result_params for task in self.ready_tasks]
		self.reinit()
		return result_list

	def reinit(self):
		self.input_tasks = []
		self.ready_tasks = []
		self.task_async_results = dict()