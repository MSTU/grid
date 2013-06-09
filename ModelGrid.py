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
import logging

import uuid

import Constants
import GridLogger
from LocalMaster import LocalMaster

from conf import ConfigClient
import Task

try:
	import Pyro4
except ImportError:
	pass

# Интерфейс для работы с системой

class ModelGrid:
	# инициализация объекта
	def __init__(self, config=None):
		if config is None:
			self.config = ConfigClient.ConfigClient()
		else:
			self.config = config
		self.id = uuid.uuid4()  # Каждому клиенту генерируется уникальный id.
		#self.logger = GridLogger.GridLogger("client" + str(self.id))
		self.logger = GridLogger.GridLogger("client")
		self.logger.Log(GridLogger.DEBUG, "uuid = " + str(self.id))
		self.lc = []
		# TODO:
		# Не пойму зачем сделал словарем. Надо разобарться.
		self.task_dict = dict()
		self.counter = 0  # Счетчик задач. У каждого клиента свой.
		if not ConfigClient.LOCAL_WORK:
			uri = "PYRO:" + Constants.MASTER_NAME + "@" + ConfigClient.MASTER_IP_ADDRESS + ":" + str(self.config.masterPort)
			Pyro4.config.HOST = ConfigClient.CLIENT_IP_ADDRESS
			self.master = Pyro4.core.Proxy(uri)
		else:
			self.master = LocalMaster()

	# установка расчетных случаев и подгтовка данных
	def SetLoadcases(self, loadcases):
		self.lc = loadcases
		for i in loadcases:
			solver = self.config.solvers[i.Solver]
			solver.LoadData(i)

	# добавление расчетных случев подготовка данных
	def AddLoadcases(self, loadcases):
		self.lc.extend(loadcases)
		for i in loadcases:
			solver = self.config.solvers[i.Solver]
			solver.LoadData(i)


	def GetLoadCases(self):
		return self.lc

	# запустить на расчет список объектов ModelAnalysis. Расчет запускается и нет ожидания.
	# Можно добавлять и другие объекты последующими Calculate
	def Calculate(self, ma_list):
		# запуск задач из ma_list
		for i in ma_list:
			task = Task.Task(self.lc, i, self.counter, self.id)
			self.counter += 1
			self.task_dict[i] = task
			self.master.RunTask(task)
			self.logger.Log(GridLogger.INFO, "Run task number " + str(self.counter))

	# ждать пока выполнится весь список ma_list
	def WaitAll(self):
		tasks = self.master.WaitAll(self.id)
		self.logger.Log(GridLogger.INFO, "Get all tasks for client " + str(self.id))
		ma_list = [task.ma for task in tasks]
		return ma_list

	# TODO:
	# Хорошо бы добавить wait для конкретного "расчетного случая"

	# инициализировать список расчетов
	def Init(self):
		self.task_dict = dict()