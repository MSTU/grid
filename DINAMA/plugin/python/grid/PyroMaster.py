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
from Master import Master


class PyroMaster(Master):
	# ������������� �������
	def __init__(self):
		Master.__init__(self)
		self.hosts_list = []  # ������ Proxy ������
		self.asynchosts_list = []  # ������ Proxy ������ ��� ����������� �������
		self.asyncresults = []  # ����� �������� ���������� ���� �����
		# TODO: ������� ��� ������ � �������. ��� ������� ������� ���� ������
		self.tasks_list = []  # ������ ���� �����
		# ������ ������ ��� ������� ������� ����������� ����. ���� - id �������, �������� - ������ �������� �����
		self.ready_tasks = dict()
		self.clientTasksCounter = dict()  #��� ������� ������� ������ ���������� ��� �������������� �����
		# (�������� ���� ������� ����������������)
		Pyro4.config.HOST = ConfigMaster.MASTER_IP_ADDRESS
		self.isRunning = True

	#������ �������� � �������
	def RunTask(self, task):
		self.tasks_list.append(task)
		if task.clientId in self.clientTasksCounter:
			self.clientTasksCounter[task.clientId] += 1
		else:
			self.clientTasksCounter[task.clientId] = 1
		self.logger.Log(logging.INFO, "run task " + str(task.id))

	#���� �������� ���� �����, ����� ���������������� ����
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

	#���� ��������� ���� ����� ������� � ������� � ���������� ��� �������� ������
	def WaitAll(self, clientId):
		# TODO:
		# �������� ���������� ����� ���������� � �����. �� ������ �������� ���������� sleep(1),
		# ��� ��� ��� ��� ������ �� ��� ����� ��������. �� ���������� ��������� ����� � ��������
		# � ����������� ������ ����� ���������� ���������� ����� ����� 0.
		while not self.clientTasksCounter[clientId] is 0:
			time.sleep(1)
		for i in range(len(self.hosts_list)):
			if not self.asyncresults[i] is None:
				self.ready_tasks[clientId].append(self.asyncresults[i].value)
		self.logger.Log(GridLogger.INFO, "All tasks calculated")
		ready_tasks = self.ready_tasks[clientId]
		self.ready_tasks[clientId] = []
		self.asyncresults = []
		for i in range(len(self.hosts_list)):
			self.asyncresults.append(None)
		return ready_tasks

	def Wait(self, clientId, taskId):
		pass

	def RunBalancer(self):
		def a():
			while self.isRunning:
				if not len(self.tasks_list) is 0:
					task = self.tasks_list[0]
				else:
					# TODO:
					# ����� ���� ������ �� �������� sleep(1) �� ���-�� ���� wait()
					time.sleep(1)
					continue

				# TODO:
				# �������� ����� ������� ���, ����� �� ����� ����� ����� ������������ ���������� ��������� �����,
				# �� � ������� "���������� ��������". �� ����� ��� "��������� ������" �� ������ ����� ������
				# � ����� ������.

				for i in range(len(self.hosts_list)):
					if self.asyncresults[i] is None:
						try:
							self.asyncresults[i] = self.asynchosts_list[i].RunTask(task)
							self.deleteTask()
							self.logger.Log(GridLogger.INFO, "send task " + str(task.GetId()) + " to Host " + str(i))
						except:
							pass
						#self.tasks_list.pop(0)
						#self.clientTasksCounter[task.clientId] -= 1
						# TODO:
						# ���� ������ �� �����������, �� �� ����� ����� ����������� ���������. ��������� ������� �����
						# ����� �������� ������� ������
						break
					if self.asyncresults[i].ready is True:
						value = self.asyncresults[i].value
						# �������� �� ������
						# TODO:
						# ���� � ������ ��� �������, �������� ��� �� ����� ������ ��������.
						if value.ma.GetStatus() != Constants.TASK_SUCCESS:
							value.ma.ClearResults()
							value.ma.SetStatus(Constants.TASK_DEFAULT)
							task = value
							self.clientTasksCounter[value.clientId] += 1
						else:
							self.logger.Log(GridLogger.INFO,
								"Host " + str(i) + " return task with parameters " + str(value.ma.GetResults()))
							if not value.clientId in self.ready_tasks:
								self.ready_tasks[value.clientId] = []
								self.ready_tasks[value.clientId].append(value)
							else:
								self.ready_tasks[value.clientId].append(value)
							self.deleteTask()
						try:
							self.asyncresults[i] = self.asynchosts_list[i].RunTask(task)
							self.logger.Log(GridLogger.INFO, "send task number " + str(task.GetId()) + "to Host " + str(i))
						except:
							pass
						break


		self.maintThread = threading.Thread(target=a)
		#		thread.setDaemon(True)
		self.maintThread.start()

	def deleteTask(self):
		self.clientTasksCounter[self.tasks_list[0].clientId] -= 1
		self.tasks_list.pop(0)

	def stopBalancer(self):
		self.isRunning = False
		self.maintThread.join()