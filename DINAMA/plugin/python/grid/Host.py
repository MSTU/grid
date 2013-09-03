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

import Constants
import conf.ConfigHost as ConfigHost
import conf.ConfigClient as ConfigClient
import GridLogger

try:
	import Pyro4
except ImportError:
	pass

# ����� �����

class Host:
	# ������������� �������
	def __init__(self, config=None):
		if config is None:
			self.config = ConfigHost.ConfigHost()
		else:
			self.config = config
		# TODO:
		# ������ ������ ������-�� �������� � �������. �� ������� �����. �� ������ ����� �������� ������ �����
		self.tasks = {}
		self.logger = GridLogger.GridLogger("host")
		uri = "PYRO:" + Constants.MASTER_NAME + "@" + ConfigHost.MASTER_IP_ADDRESS + ":" + str(self.config.masterPort)
		if not ConfigClient.LOCAL_WORK:
			try:
				self.master = Pyro4.core.Proxy(uri)
				Pyro4.config.HOST = ConfigHost.HOST_IP_ADDRESS
			except:
				pass

	def RegisterOnMaster(self):
		try:
			# it works only when this instance registered on PyroDaemon
			uri = self._pyroDaemon.uriFor(self)
			self.master._pyroOneway.add("RegisterHost")
			self.logger.Log(logging.INFO, "Send registration request")
			self.master.RegisterHost(uri)
		except:
			pass
		#�������, ��� ��� ������ RegisterHost �� ������� �� ����� ����� ���������� ����� ������.
		# ������ ���������� ������������ ����� ��.
		#��� ������� ������, ��� � ������ ������ RegisterHost �� �������,
		# ������ ���� ������� requestloop ������, �� ������� ������� ���� ����.
		#� ����������� �� ����� ����� ������ �������� ������. ���� ��� ���������.
		# �������� requestloop ��������� � ��������� ������.

	# ������ ������ �� ������
	def RunTask(self, task):
		# ������������� ������� ������ Launcher (PRADISSolver ��� ModelicaSolver)
		for i in task.lc:
			solver = self.config.solvers[i.Solver]
			solver.Init()
			try:
				status = solver.Run(i, task.ma)
				#  TODO:
				# ����� ������� ����������� �� ��������� � ��������� �� ������������

				# ��� ������� �������. ���� ��� � ������, �� �������� != ����� ���������.
				if status < task.GetModelAnalysis().GetStatus():
					task.ma.SetStatus(status)
			except:
				pass

		print "Parameters = " + str(task.ma.GetParameters())
		print "Results = " + str(task.ma.GetResults())
		# TODO: ???
		self.tasks[task.GetId()] = task
		self.logger.Log(logging.INFO, "Task " + str(task.GetId()) + " is calculated")
		return task

	def SetTasks(self, tasks):
		self.tasks = tasks

	def GetTasks(self):
		return self.tasks
		# .............