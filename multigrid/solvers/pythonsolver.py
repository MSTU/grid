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
from debug import logger

name = "Python"

class PythonLoadcase(Loadcase):
	"""
	Loadcase for PythonSolver.

	scheme: pickled function
		Pickled function to run
	desc: string
		Description of this loadcase
	preexecute_filename: string
		Path to preexecuted file
	"""
	def __init__(self, scheme, desc=None, preexecute_filename=None):
		if not desc:
			desc = scheme.__name__
		func_dump = cloudpickle.dumps(scheme)
		if preexecute_filename:
			try:
				with open(preexecute_filename) as f:
					self.preexecute_file = f.readlines()
				import ntpath
				self.preexecute_filename = ntpath.basename(preexecute_filename)
			except Exception as e:
				self.preexecute_file = None
				self.preexecute_filename = None
				logger.error("Error while read preexecuted file: " + e.message)
		Loadcase.__init__(self, func_dump, name, desc)

class PythonSolver(Launcher):

	def run(self, lc, input_params):
		result = None
		try:
			func = pickle.loads(lc.scheme)
			result = func(input_params)

			status = constants.SUCCESS_STATUS
		except Exception as e:
			status = constants.ERROR_STATUS
			# TODO is it right?
			result = e

		lc.status = status
		return result

	def preexecute(self, lc):
		if lc.preexecute_file:
			try:
				preexecute_file = open(lc.preexecute_filename, 'w')
				preexecute_file.writelines(lc.preexecute_file)
				preexecute_file.close()
			except Exception as e:
				logger.error("Error while create preexecuted file: " + e.message )
			try:
				execfile(lc.preexecute_filename)
			except Exception as e:
				logger.error("Error while exec preexecuted file: " + e.message)
