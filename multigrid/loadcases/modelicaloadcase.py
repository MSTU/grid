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
import constants
from loadcase import Loadcase
from solvers.modelicasolver import ModelicaSolver

class ModelicaLoadcase(Loadcase):
	"""
	Loadcase for ModelicaSolver.
	"""
	def __init__(self, scheme, criteria_list=None, solver_params=None, desc=constants.DEFAULT_LOADCASE):
		Loadcase.__init__(self, scheme, ModelicaSolver.name, desc)

		self.criteria_list = criteria_list
		self.solver_params = solver_params
