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

import subprocess
import os
import shutil

import sys
import debug
import constants
import launcher
from solvers.ansys.ansys_methods import get_ansys_version
from solvers.ansys.common_methods import create_file_from_list


class CFXSolver(launcher.Launcher):
	name = "ANSYS_CFX"
	_version = get_ansys_version()
	_exec_path = ["/ansys_inc/v" + _version + "/CFX/bin/cfx5solve"]

	def __init__(self):
		launcher.Launcher.__init__(self)
		self.logger = debug.logger

	# Loads content of *.def file in special variable inData
	def load_data(self, lc):
		if not os.path.isfile(lc.scheme):
			self.logger.error("ERROR: " + lc.scheme + " does not exist")
			return None
		with open(lc.scheme, 'r') as f:
			lc.inData = f.readlines()

	def run(self, loadcase, input_params):
		if loadcase.inData is None:
			self.logger.error("ERROR: inData contains nothing")
			loadcase.status = constants.ERROR_STATUS
		cwd = os.getcwd()
		if not os.path.exists(loadcase.name): os.makedirs(loadcase.name)
		os.chdir(loadcase.name)
		error_log_filename = "CFX_error_log"
		try:
			error_log_file = open(error_log_filename, "w")
		except IOError:
			self.logger.error("Can not create \"" + error_log_filename + "\"")
			loadcase.status = constants.ERROR_STATUS
		# loadcase.scheme.rpartition("/")[2] - actual filename
		# for example
		# path = /home/user/cfx/file.def
		# path.rparition("/")[2] = "file.def"
		def_filename = loadcase.scheme.rpartition("/")[2]
		create_file_from_list(loadcase.inData, def_filename)
		if(loadcase.solver_params is not None):
			options = loadcase.solver_params.split()
		else:
			options = []
		options.append("-def")
		options.append(def_filename)
		self.check_options(options)

		if sys.platform.startswith('win'):
			pass
		elif sys.platform.startswith('linux'):
			self.logger.info('executing ANSYS CFX Solver')
			subprocess.call(self._exec_path + options, stderr=error_log_file)
			self.logger.info('ANSYS CFX Solver finished')
		else:
			self.logger.error('ERROR: Сan not determine your platform')
			loadcase.status = constants.ERROR_STATUS
		error_log_file.close()
		if (os.path.getsize(error_log_filename) == 0):
			error_flag = False
			os.remove(error_log_filename)
		else:
			error_flag = self.check_log(error_log_filename)

		os.chdir(cwd)
		if (not error_flag):
			loadcase.status = constants.SUCCESS_STATUS
		loadcase.status = constants.ERROR_STATUS

	def check_log(self, log_filename):
		"""
		Checks error log file for errors, because sometimes CFX Solver writes
		something in stderr stream, but it is not an error.
		Example
		with -v option CFX Solver writes in stderr:
		"Adding host antonpc (Anton-PC) (linux-amd64) to the parallel environment."

		Returns:
		True - if error occured
		False - otherwise

		"""
		error_string = "An error has occurred in cfx5solve:"
		error_flag = False
		try:
			log_file = open(log_filename, "r")
		except IOError:
			self.logger.error("Can not open \"" + log_filename + "\" for reading")
			return None
		for line in log_file:
			if error_string in line:
				error_flag = True
				break

		if (error_flag):
			log_file.seek(0)
			for line in log_file:
				print line
			log_file.close()
		else:
			log_file.close()
			os.remove(log_filename)

		return error_flag

	def check_options(self, options):
		"""
		This function is needed for successful sequential runs of CFX solver.
		When you specify both -fullname <result_name> and -save options to solver,
		a temporary directory called "result_name.dir" is created and is not deleted after successful run
		(because of -save option). It is normal behavior, but when you try to run cfx solver again with the same
		<result_name> in -fullname option and with -save option it raises an error:
		<<Aborting due to internal error: "There is already a definition file, refusing to create a new one".>>
		This function gives us an opportunity to successfully perform sequential runs of cfx solver with -save option
		and with the same name of result file in -fullname option.
		This function checks if there are -fullname <result_name> and -save options specified in options string.
		Then it checks if temporary directory called "<result_name>.dir" exists.
		If it does exist, then this function deletes that temporary directory and all of its contents.

		"""
		if("-fullname" and "-save" in options):
			res_index = options.index("-fullname") + 1
			temp_dir_name = options[res_index] + ".dir"
			if (os.path.isdir(temp_dir_name)):
				shutil.rmtree(temp_dir_name)