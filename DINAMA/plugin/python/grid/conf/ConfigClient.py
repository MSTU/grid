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
from solvers import PRADISSolver, ModelicaSolver, PythonSolver, LSDYNASolver

LOCAL_WORK = True

class ConfigClient:
	# инициализация объекта
	def __init__(self):
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

		ANSYS_LSDYNA = LSDYNASolver.LSDYNASolver()
		self.solvers[ANSYS_LSDYNA.name] = ANSYS_LSDYNA


	# адрес мастер-хоста
	def MasterURL(self):
		return "localhost"