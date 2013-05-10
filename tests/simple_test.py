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
import threading

import unittest
import Pyro4
import Constants
import Host
import Loadcase
import Master
import ModelAnalysis
import ModelGrid
from conf import ConfigMaster
from tests import test_lib


class SimpleTestCase(unittest.TestCase):

	master = Master.Master()
	hosts = []
	hostsDaemons = []
	hostsTheads = []
	clients = []

	def setUp(self):
		daemonMaster=Pyro4.Daemon(port = ConfigMaster.PORT)
		daemonMaster.register(self.master, Constants.MASTER_NAME)
		self.master.RunBalancer()
		self.masterThread = threading.Thread(target=daemonMaster.requestLoop)
		self.masterThread.start()
		for i in range(0,2):
			host = Host.Host()
			daemon = Pyro4.Daemon()
			daemon.register(host)
			host.RegisterOnMaster()
			thread = threading.Thread(target=daemon.requestLoop)
			thread.start()
			self.hosts.append(host)
			self.hostsDaemons.append(daemon)
			self.hostsTheads.append(thread)

	def test_something(self):

		lc1 = Loadcase.Loadcase([], [test_lib.func_1, '', '', 'Python'], desc = 'lc1')

		# подготовка объекта решателя
		mg = ModelGrid.ModelGrid()
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
		ma_list = mg.Wait()
		# обработка результатов
		result = {}
		for i in ma_list:
			if (i.GetStatus() == 0):
				result[i.GetParameter('x')] = i.GetResults()['lc1']
		# сброс параметров предыдущего расчета
		mg.Init()

		real = {}
		for i in range(3):
			self.assertEqual(result[i][0], i**2)


if __name__ == '__main__':
	unittest.main()
