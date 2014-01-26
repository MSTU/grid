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
	from LocalWorker import RunTask
else:
	from Worker import RunTask

class ModelGrid:
	def __init__(self, config=None):
		if config is None:
			self.config = ConfigClient.ConfigClient()
		else:
			self.config = config
		self.loadcases = []
		self.Init()

	def SetLoadcases(self, loadcases):
		self.loadcases = loadcases
		for loadcase in loadcases:
			solver = self.config.solvers[loadcase.solver]
			solver.LoadData(loadcase)

	def AddLoadcases(self, loadcases):
		self.loadcases.extend(loadcases)
		for i in loadcases:
			solver = self.config.solvers[i.Solver]
			solver.LoadData(i)


	def GetLoadcases(self):
		return self.loadcases

	def clearLoadcases(self):
		self.loadcases = []

	def Calculate(self, input_list):
		"""
		For all items in input_list create Task instance and run them.
		Return ids of created Tasks
		"""
		result_ids = []
		for item in input_list:
			task = Task(self.loadcases, item)
			if not ConfigClient.LOCAL_WORK:
				self.inputTasks.append(task)
				asyncResult = RunTask.delay(task)
				task.id = asyncResult.task_id
				result_ids.append(task.id)
				self.taskAsyncResults[task] = asyncResult
			else:
				self.readyTasks.append(RunTask(task))
		return result_ids

	def waitTasks(self, task_ids):
		"""
		Wait and return result of tasks with ids specified in task_ids list
		"""
		results = []
		for id in task_ids:
			asyncResult = AsyncResult(id)
			results.append(asyncResult.get())
		return results


	def WaitAll(self):
		if ConfigClient.LOCAL_WORK:
			return [task.result_params for task in self.readyTasks]
		for task in self.inputTasks:
			self.readyTasks.append(self.taskAsyncResults[task].get())
		result_list = [task.result_params for task in self.readyTasks]
		self.Init()
		return result_list

	def Init(self):
		self.inputTasks = []
		self.readyTasks = []
		self.taskAsyncResults = dict()