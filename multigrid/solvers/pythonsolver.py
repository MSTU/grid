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
import pickle
import cloudpickle
import constants
from launcher import Launcher
from loadcase import Loadcase

name = "Python"

class PythonLoadcase(Loadcase):
	"""
	Loadcase for PythonSolver.
	"""
	def __init__(self, scheme, desc=None):
		if not desc:
			desc = scheme.__name__
		func_dump = cloudpickle.dumps(scheme)
		Loadcase.__init__(self, func_dump, name, desc, False)

class PythonSolver(Launcher):

	def run(self, lc, input_params):
		result = None
		try:
			func = pickle.loads(lc.scheme)
			if isinstance(input_params, tuple) or isinstance(input_params, list):
				result = func(*input_params)
			else:
				result = func(input_params)

			status = constants.SUCCESS_STATUS
		except Exception as e:
			status = constants.ERROR_STATUS
			# TODO is it right?
			#result = e

		lc.status = status
		return result
