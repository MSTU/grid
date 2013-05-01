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

import uuid

import Pyro4
import Constants

from conf import ConfigClient
import Task

# Интерфейс для работы с системой

class ModelGrid:
	# инициализация объекта
	def __init__(self):
		self.id = uuid.uuid4() # Каждому клиенту генерируется уникальный id.
		self.lc = []
		# TODO:
		# Не пойму зачем сделал словарем. Надо разобарться.
		self.task_dict = dict()
		self.config = ConfigClient.ConfigClient()
		self.counter = 0 # Счетчик задач. У каждого клиента свой.

		uri = "PYRO:" + Constants.MASTER_NAME + "@" + ConfigClient.MASTER_IP_ADDRESS + ":" + str(ConfigClient.PORT)
		self.master = Pyro4.core.Proxy(uri)

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

	# ждать пока выполнится весь список ma_list
	def Wait(self):
		tasks = self.master.WaitAll(self.id)
		ma_list = [task.ma for task in tasks]
		return ma_list

	# TODO:
	# Хорошо бы добавить wait для конкретного "расчетного случая"

	# инициализировать список расчетов
	def Init(self):
		self.task_dict = dict()