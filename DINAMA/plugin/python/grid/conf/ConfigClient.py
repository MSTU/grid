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

# класс конфигурации клиента
from solvers import PRADISSolver, ModelicaSolver, PythonSolver

MASTER_IP_ADDRESS = 'localhost'
CLIENT_IP_ADDRESS = 'localhost'
PORT = 9000

LOCAL_WORK = False

class ConfigClient:
	# инициализация объекта
	def __init__(self):
		self.masterPort = PORT
		#sys.excepthook=Pyro4.util.excepthook
		#Pyro4.config.DETAILED_TRACEBACK = False
		#Pyro4.config.COMPRESSION = False
		#Pyro4.config.ONEWAY_THREADED = False
		#Pyro4.config.HMAC_KEY = None
		#Pyro4.config.HOST = CLIENT_IP_ADDRESS
		self.LOCAL_WORK = LOCAL_WORK
		self.Solvers()

	# инициализация решателей
	def Solvers(self):
		self.solvers = dict()

		pradis = PRADISSolver.PRADISSolver()
		self.solvers[pradis.name] = pradis

		modelica = ModelicaSolver.ModelicaSolver()
		self.solvers[modelica.name] = modelica

		pythonsolver = PythonSolver.PythonSolver()
		self.solvers[pythonsolver.name] = pythonsolver


	# адрес мастер-хоста
	def MasterURL(self):
		return "localhost"