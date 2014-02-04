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

# ����� ������������ �������
from solvers import PRADISSolver, ModelicaSolver, PythonSolver, LSDYNASolver, CFXSolver, MechanicalSolver

LOCAL_WORK = False

class ConfigClient:
	# ������������� �������
	def __init__(self):
		self.LOCAL_WORK = LOCAL_WORK
		self.init_solvers()

	# ������������� ���������
	def init_solvers(self):
		self.solvers = dict()

		pradis = PRADISSolver.PRADISSolver()
		self.solvers[pradis.name] = pradis

		modelica = ModelicaSolver.ModelicaSolver()
		self.solvers[modelica.name] = modelica

		pythonsolver = PythonSolver.PythonSolver()
		self.solvers[pythonsolver.name] = pythonsolver

		ANSYS_LSDYNA = LSDYNASolver.LSDYNASolver()
		self.solvers[ANSYS_LSDYNA.name] = ANSYS_LSDYNA

		ANSYS_CFX = CFXSolver.CFXSolver()
		self.solvers[ANSYS_CFX.name] = ANSYS_CFX
		ANSYS_Mechanical = MechanicalSolver.MechanicalSolver()
		self.solvers[ANSYS_Mechanical.name] = ANSYS_Mechanical

	# ����� ������-�����
	def MasterURL(self):
		return "localhost"