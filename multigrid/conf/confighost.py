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
from solvers import pradissolver, modelicasolver, pythonsolver, lsdynasolver, cfxsolver, mechanicalsolver

BACKEND = 'amqp'
BROKER = 'amqp://guest@localhost//'

USERNAME = ""
PASSWORD = ""
CLIENT_NAME = ""
SHARE_DIR = 'share'

class ConfigHost:

	def __init__(self):
		self.Solvers()

	def Solvers(self):
		self.solvers = dict()

		pradis = pradissolver.PRADISSolver()
		self.solvers[pradis.name] = pradis

		modelica = modelicasolver.ModelicaSolver()
		self.solvers[modelica.name] = modelica

		python = pythonsolver.PythonSolver()
		self.solvers[python.name] = python

		ANSYS_LSDYNA = lsdynasolver.LSDYNASolver()
		self.solvers[ANSYS_LSDYNA.name] = ANSYS_LSDYNA

		ANSYS_CFX = cfxsolver.CFXSolver()
		self.solvers[ANSYS_CFX.name] = ANSYS_CFX
		ANSYS_Mechanical = mechanicalsolver.MechanicalSolver()
		self.solvers[ANSYS_Mechanical.name] = ANSYS_Mechanical
