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
		ns = Pyro4.naming.locateNS()
		uri = ns.lookup("Master")
		self.master = Pyro4.core.Proxy(uri)

	def RegisterOnMaster(self):
		uri = self._pyroDaemon.uriFor(self)
		#�������, ��� ��� ������ RegisterHost �� ������� �� ����� ����� ���������� ����� ������.
		# ������ ���������� ������������ ����� ��.
		#��� ������� ������, ��� � ������ ������ RegisterHost �� �������,
		# ������ ���� ������� requestloop ������, �� ������� ������� ���� ����.
		#� ����������� �� ����� ����� ������ �������� ������. ���� ��� ���������.
		# �������� requestloop ��������� � ��������� ������.
		self.master._pyroOneway.add("RegisterHost")
		self.monitor.Log("Send registration request")
		self.master.RegisterHost(uri)

	# ������ ������ �� ������
	def RunTask(self, task):
		# ������������� ������� ������ Launcher (PRADISSolver ��� ModelicaSolver)
		for i in task.lc:
			solver = self.config.solvers[i.Solver]
			solver.Init()
			status = solver.Run(i, task.ma)
			#  TODO:
			# ����� ������� ����������� �� ��������� � ��������� �� ������������

			# ��� ������� �������. ���� ��� � ������, �� �������� != ����� ���������.
			if status < task.GetModelAnalysis().GetStatus():
				task.ma.SetStatus(status)
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