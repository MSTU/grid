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

import threading
import time

import Pyro4

import conf.ConfigMaster as ConfigMaster
import Constants
import GridLogger


class Master:
	# инициализация объекта
	def __init__(self, config=None):
		if config is None:
			self.config = ConfigMaster.ConfigMaster()
		else:
			self.config = config
		self.logger = GridLogger.GridLogger("master")
		self.hosts_list = []  # Список Proxy хостов
		self.asynchosts_list = []  # Список Proxy хостов для асинхронных вызовов
		self.asyncresults = []  # Здесь хранятся результаты всех задач
		# TODO: хранить все задачи в словаре. Для каждого клиента свои задачи
		self.tasks_list = []  # список всех задач
		# Готвые задачи для каждого клиента сваливаются сюда. Ключ - id клиента, занчение - список решенных задач
		self.ready_tasks = dict()
		self.clientTasksCounter = dict()  #Для каждого клиента хранит количество его невыполненнных задач
		# (возможно надо сделать потокобезопасной)

	#Задача ставится в очередь
	def RunTask(self, task):
		self.tasks_list.append(task)
		if task.clientId in self.clientTasksCounter:
			self.clientTasksCounter[task.clientId] += 1
		else:
			self.clientTasksCounter[task.clientId] = 1
		self.logger.Log(logging.INFO, "run task " + str(task.id))

	#Хост вызывает этот метод, чтобы зарегистрировать себя
	def RegisterHost(self, host_uri):
		try:
			host = Pyro4.Proxy(host_uri)
			if host not in self.hosts_list:
				self.hosts_list.append(host)
			self.asynchosts_list.append(Pyro4.async(host))
			self.asyncresults.append(None)
			self.logger.Log(logging.INFO, "Host " + host_uri + "registered")

		except TypeError:
			pass

	#Ждет выполения всех задач клиента в очереди и возвращает все решенные задачи
	def Wait(self, clientId):
		# TODO:
		# Ожидание завершения задач происходит в цикле. На каждой итерации вызывается sleep(1),
		# так что все это тратит не так много ресурсов. Но правильнее поставить поток в ожидание
		# и возобновить работу когда количество нерешенных задач будте 0.
		while not self.clientTasksCounter[clientId] is 0:
			time.sleep(1)
		for i in range(len(self.hosts_list)):
			if not self.asyncresults[i] is None:
				self.ready_tasks[clientId].append(self.asyncresults[i].value)
		self.logger.Log(logging.INFO, "All tasks calculated")
		ready_tasks = self.ready_tasks[clientId]
		self.ready_tasks[clientId] = []
		self.asyncresults = []
		for i in range(len(self.hosts_list)):
			self.asyncresults.append(None)
		return ready_tasks

	def RunBalancer(self):
		def a():
			while True:
				if not len(self.tasks_list) is 0:
					task = self.tasks_list[0]
				else:
					# TODO:
					# Здесь тоже хорошо бы заменить sleep(1) на что-то типа wait()
					time.sleep(1)
					continue

				# TODO:
				# Возможно нужно сделать так, чтобы на одном хосте могло одновременно выполнятся несколько задач,
				# но с разными "расчетными случиями". Но тогда эти "расчетные случаи" на должны иметь доступ
				# к общим данным.

				for i in range(len(self.hosts_list)):
					if self.asyncresults[i] is None:
						try:
							self.asyncresults[i] = self.asynchosts_list[i].RunTask(task)
							self.deleteTask()
							self.logger.Log(logging.INFO, "send task " + str(task.GetId()) + " to Host " + str(i))
						except:
							pass
						#self.tasks_list.pop(0)
						#self.clientTasksCounter[task.clientId] -= 1
						# TODO:
						# Если задача не выполнилась, то ее нужно опять попробовать выполнить. Уменьшать счетчик нужно
						# после успешнго решения задачи
						break
					if self.asyncresults[i].ready is True:
						value = self.asyncresults[i].value
						# Проверка на ошибки
						# TODO:
						# Если с хостом что неладно, возможно ему не нужно ничего посылать.
						if value.ma.GetStatus() != Constants.TASK_SUCCESS:
							value.ma.ClearResults()
							value.ma.SetStatus(Constants.TASK_DEFAULT)
							task = value
							self.clientTasksCounter[value.clientId] += 1
						else:
							self.logger.Log(logging.INFO,
								"Host " + str(i) + " return task with parameters " + str(value.ma.GetResults()))
							if not value.clientId in self.ready_tasks:
								self.ready_tasks[value.clientId] = []
								self.ready_tasks[value.clientId].append(value)
							else:
								self.ready_tasks[value.clientId].append(value)
							self.deleteTask()
						try:
							self.asyncresults[i] = self.asynchosts_list[i].RunTask(task)
							self.logger.Log(logging.INFO, "send task number " + str(task.GetId()) + "to Host " + str(i))
						except:
							pass
						break


		thread = threading.Thread(target=a)
		#		thread.setDaemon(True)
		thread.start()

	def deleteTask(self):
		self.clientTasksCounter[self.tasks_list[0].clientId] -= 1
		self.tasks_list.pop(0)

