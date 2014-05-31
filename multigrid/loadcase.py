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
from serialization import cloudpickle
import constants


class Loadcase:
	"""
	Base class for calculation case specification. It's environment in which task will be calculated
	"""
	def __init__(self, scheme, solver, desc, is_local=False):
		self.scheme = scheme
		self.name = desc
		self.solver = solver
		self.status = constants.DEFAULT_STATUS
		self.is_filetransfer = False
		self.is_local = is_local

	def load_data(self):
		"""
		Run while Loadcase creating.
		"""
		pass

	def __repr__(self):
		return self.name

	def run(self, input_params):
		from solvers.holder import get_solver

		solver_instance = get_solver(self.solver)
		return solver_instance.run(self, input_params)


class SuperLoadcase:
	def __init__(self, nl, pl, desc=constants.DEFAULT_LOADCASE):
		scheme_name = pl[0]
		result_name = pl[1]
		self.functions_list = [cloudpickle.dumps(func) for func in pl[2]]
		self.criteria_list = pl[3]
		solver = pl[4]

		self.name = desc
		self.scheme = scheme_name
		self.result_file = result_name
		self.solver = solver

		self.solver_parameters = []
		self.open_sign = pl[5]
		self.close_sign = pl[6]
