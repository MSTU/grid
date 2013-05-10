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

import Pyro4
import Constants
import conf.ConfigHost as ConfigHost
import Monitor


# ����� �����

class Host:
	# ������������� �������
	def __init__(self):
		self.config = ConfigHost.ConfigHost()
		# TODO:
		# ������ ������ ������-�� �������� � �������. �� ������� �����. �� ������ ����� �������� ������ �����
		self.tasks = {}
		self.monitor = Monitor.Monitor("host.log")
		uri = "PYRO:" + Constants.MASTER_NAME + "@" + ConfigHost.MASTER_IP_ADDRESS + ":" + str(ConfigHost.PORT)
		try:
			self.master = Pyro4.core.Proxy(uri)
		except:
			pass

	def RegisterOnMaster(self):
		try:
			uri = self._pyroDaemon.uriFor(self)
			self.master._pyroOneway.add("RegisterHost")
			self.monitor.Log("Send registration request")
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
		self.monitor.Log("Task " + str(task.GetId()) + " is calculated")
		return task

	def SetTasks(self, tasks):
		self.tasks = tasks

	def GetTasks(self):
		return self.tasks
		# .............