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
import random
import threading

import unittest
import Pyro4
import grid.Constants as Constants
import grid.Host as Host
import grid.Loadcase as Loadcase
import grid.PyroMaster as PyroMaster
import grid.ModelAnalysis as ModelAnalysis
import grid.ModelGrid as ModelGrid
from grid.conf import ConfigMaster, ConfigHost, ConfigClient
from tests import test_lib


class SimpleTestCase(unittest.TestCase):

	master = PyroMaster.PyroMaster()
	hosts = []
	hostsDaemons = []
	hostsTheads = []
	clients = []

	isRun = True

	def isRunning(self):
		return self.isRun

	def setUp(self):
		#Pyro4.config.COMMTIMEOUT = 5
		Pyro4.config.SERVERTYPE = "multiplex"
		self.port = 4000 + random.randint(0, 12000)
		daemonMaster = Pyro4.Daemon(port=self.port)
		daemonMaster.register(self.master, Constants.MASTER_NAME)
		self.master.RunBalancer()
		self.masterThread = threading.Thread(target=daemonMaster.requestLoop, args=[self.isRunning])
		self.masterThread.start()
		for i in range(0, 2):
			hostConfig = ConfigHost.ConfigHost()
			hostConfig.masterPort = self.port
			host = Host.Host(hostConfig)
			daemon = Pyro4.Daemon()
			daemon.register(host)
			host.RegisterOnMaster()
			thread = threading.Thread(target=daemon.requestLoop, args=[self.isRunning])
			thread.start()
			self.hosts.append(host)
			self.hostsDaemons.append(daemon)
			self.hostsTheads.append(thread)

	def test_something(self):

		lc1 = Loadcase.Loadcase([], ['', '', [test_lib.func_1], ['[]'], 'Python', '%', '%', ''],desc = 'lc1')

		# подготовка объекта решателя
		clientConfig = ConfigClient.ConfigClient()
		clientConfig.masterPort = self.port
		mg = ModelGrid.ModelGrid(clientConfig)
		mg.Init()
		mg.SetLoadcases([lc1])

		# подготовка параметров
		ma_list = []
		for i in xrange(3):
			ma = ModelAnalysis.ModelAnalysis()
			par = dict()
			par['x'] = i
			ma.SetParameters(par)
			ma_list.append(ma)
		# расчет
		mg.Calculate(ma_list)
		# ожидание выполняения расчета
		ma_list = mg.WaitAll()
		# обработка результатов
		result = {}
		for i in ma_list:
			if (i.GetStatus() == 0):
				result[i.GetParameter('x')] = i.GetResults()['lc1']
		# сброс параметров предыдущего расчета
		mg.Init()

		real = {}
		for i in xrange(3):
			self.assertEqual(result[i][0], i ** 2)

		self.isRun = False
		for thread in self.hostsTheads:
			thread.join()
		self.master.stopBalancer()
		self.masterThread.join()


if __name__ == '__main__':
    unittest.main(exit=False)
