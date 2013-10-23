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
import Task
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
			solver = self.config.solvers[loadcase.Solver]
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

	def Calculate(self, ma_list):
		for ma in ma_list:
			task = Task.Task(self.loadcases, ma)
			if not ConfigClient.LOCAL_WORK:
				self.inputTasks.append(task)
				self.taskAsyncResults[task] = RunTask.delay(task)
			else:
				self.readyTasks.append(RunTask(task))

	def WaitAll(self):
		if ConfigClient.LOCAL_WORK:
			return [task.ma for task in self.readyTasks]
		for task in self.inputTasks:
			self.readyTasks.append(self.taskAsyncResults[task].get())
		ma_list = [task.ma for task in self.readyTasks]
		self.Init()
		return ma_list

	def Init(self):
		self.inputTasks = []
		self.readyTasks = []
		self.taskAsyncResults = dict()