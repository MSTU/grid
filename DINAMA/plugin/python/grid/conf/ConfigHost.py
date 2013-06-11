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

#import sys
#import Pyro4
#import Pyro4.util

import grid.solvers.PRADISSolver as PRADISSolver
import grid.solvers.ModelicaSolver as ModelicaSolver
import grid.solvers.PythonSolver as PythonSolver

HOST_IP_ADDRESS = 'localhost'
MASTER_IP_ADDRESS = 'localhost'
PORT = 9000

class ConfigHost:

	def __init__(self):
		self.masterPort = PORT
		self.Solvers()

	def Solvers(self):
		self.solvers = dict()

		pradis = PRADISSolver.PRADISSolver()
		self.solvers[pradis.name] = pradis

		modelica = ModelicaSolver.ModelicaSolver()
		self.solvers[modelica.name] = modelica

		pythonsolver = PythonSolver.PythonSolver()
		self.solvers[pythonsolver.name] = pythonsolver

	def MasterURL(self):
		return MASTER_IP_ADDRESS