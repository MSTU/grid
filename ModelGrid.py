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

import Pyro4
import Constants
import GridLogger

from conf import ConfigClient
import Task

# ��������� ��� ������ � ��������

class ModelGrid:
	# ������������� �������
	def __init__(self, config=None):
		if config is None:
			self.config = ConfigClient.ConfigClient()
		else:
			self.config = config
		self.id = uuid.uuid4()  # ������� ������� ������������ ���������� id.
		#self.logger = GridLogger.GridLogger("client" + str(self.id))
		self.logger = GridLogger.GridLogger("client")
		self.logger.Log(logging.DEBUG, "uuid = " + str(self.id))
		self.lc = []
		# TODO:
		# �� ����� ����� ������ ��������. ���� �����������.
		self.task_dict = dict()
		self.counter = 0  # ������� �����. � ������� ������� ����.

		uri = "PYRO:" + Constants.MASTER_NAME + "@" + ConfigClient.MASTER_IP_ADDRESS + ":" + str(self.config.masterPort)
		self.master = Pyro4.core.Proxy(uri)

	# ��������� ��������� ������� � ��������� ������
	def SetLoadcases(self, loadcases):
		self.lc = loadcases
		for i in loadcases:
			solver = self.config.solvers[i.Solver]
			solver.LoadData(i)

	# ���������� ��������� ������ ���������� ������
	def AddLoadcases(self, loadcases):
		self.lc.extend(loadcases)
		for i in loadcases:
			solver = self.config.solvers[i.Solver]
			solver.LoadData(i)


	def GetLoadCases(self):
		return self.lc

	# ��������� �� ������ ������ �������� ModelAnalysis. ������ ����������� � ��� ��������.
	# ����� ��������� � ������ ������� ������������ Calculate
	def Calculate(self, ma_list):
		# ������ ����� �� ma_list
		for i in ma_list:
			task = Task.Task(self.lc, i, self.counter, self.id)
			self.counter += 1
			self.task_dict[i] = task
			self.master.RunTask(task)
			self.logger.Log(logging.INFO, "Run task number " + str(self.counter))

	# ����� ���� ���������� ���� ������ ma_list
	def Wait(self):
		tasks = self.master.Wait(self.id)
		self.logger.Log(logging.INFO, "Get all tasks for client " + str(self.id))
		ma_list = [task.ma for task in tasks]
		return ma_list

	# TODO:
	# ������ �� �������� wait ��� ����������� "���������� ������"

	# ���������������� ������ ��������
	def Init(self):
		self.task_dict = dict()