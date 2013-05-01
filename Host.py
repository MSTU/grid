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


# класс хоста

class Host:
	# инициализация объекта
	def __init__(self):
		self.config = ConfigHost.ConfigHost()
		# TODO:
		# Сейчас задачи почему-то хранятся в словаре. Не понятно зачем. На список нужно заменить скорее всего
		self.tasks = {}
		self.monitor = Monitor.Monitor("host.log")
		ns = Pyro4.naming.locateNS()
		uri = ns.lookup("Master")
		self.master = Pyro4.core.Proxy(uri)

	def RegisterOnMaster(self):
		uri = self._pyroDaemon.uriFor(self)
		#Говорим, что при вызове RegisterHost на Мастере не нужно ждать завершения этого метода.
		# Тоесть управление возвращается сразу же.
		#Это сделано потому, что в момент вызова RegisterHost на Мастере,
		# должен быть запущен requestloop демона, на котором запущен этот хост.
		#А запускается он сразу после вызова текущего метода. Надо это пофиксить.
		# Наверное requestloop запустить в отдельном потоке.
		self.master._pyroOneway.add("RegisterHost")
		self.monitor.Log("Send registration request")
		self.master.RegisterHost(uri)

	# запуск задачи на расчет
	def RunTask(self, task):
		# инициализация объекта класса Launcher (PRADISSolver или ModelicaSolver)
		for i in task.lc:
			solver = self.config.solvers[i.Solver]
			solver.Init()
			status = solver.Run(i, task.ma)
			#  TODO:
			# Нужно наконец разобраться со статусами и корректно их обрабатывать

			# Это немного странно. Если это с делать, то наверное != нужно поставить.
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