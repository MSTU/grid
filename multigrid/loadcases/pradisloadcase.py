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
from solvers.pradissolver import PRADISSolver

class PradisLoadcase(Loadcase):
	"""
	Loadcase for PradisSolver.
	"""
	def __init__(self, scheme, result_file, criteria_list, solver_params, open_sign, close_sign, desc=constants.DEFAULT_LOADCASE):
		Loadcase.__init__(self, scheme, PRADISSolver.name, desc)

		self.result_file = result_file
		self.criteria_list = criteria_list
		self.solver_params = solver_params
		self.open_sign = open_sign
		self.close_sign = close_sign
