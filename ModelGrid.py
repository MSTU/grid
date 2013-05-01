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

# ��������� ��� ������ � ��������

class ModelGrid:
	# ������������� �������
	def __init__(self):
		self.id = uuid.uuid4() # ������� ������� ������������ ���������� id.
		self.lc = []
		# TODO:
		# �� ����� ����� ������ ��������. ���� �����������.
		self.task_dict = dict()
		self.config = ConfigClient.ConfigClient()
		self.counter = 0 # ������� �����. � ������� ������� ����.

		uri = "PYRO:" + Constants.MASTER_NAME + "@" + ConfigClient.MASTER_IP_ADDRESS + ":" + str(ConfigClient.PORT)
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

	# ����� ���� ���������� ���� ������ ma_list
	def Wait(self):
		tasks = self.master.WaitAll(self.id)
		ma_list = [task.ma for task in tasks]
		return ma_list

	# TODO:
	# ������ �� �������� wait ��� ����������� "���������� ������"

	# ���������������� ������ ��������
	def Init(self):
		self.task_dict = dict()