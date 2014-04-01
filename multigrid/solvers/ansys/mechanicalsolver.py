# -*- coding: cp1251 -*-

# ***************************************************************************
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
import sys

import debug
import constants
import launcher
from solvers.common_methods import create_file
from solvers.ansys.ansys_methods import get_ansys_version


class MechanicalSolver(launcher.Launcher):
	name = "ANSYS_Mechanical"
	_version = get_ansys_version()
	_exec_path = ["/ansys_inc/v" + _version + "/ansys/bin/ansys" + _version,
				  "-b", "-p", "ANSYS"]
	# object initialization
	def __init__(self):
		launcher.Launcher.__init__(self)
		self.error_log_name = "global.err"  #global error log (for all runs)
		self.logger = debug.logger

	# Loads content of *.dat file in special variable inData
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
		self.delete_local_log()
		# ANSYS will write its output to output.log instead of stdout
		# it is done with "-o output_filename" option
		output_filename = "output.log"
		# default ANSYS error log filename is file.err
		local_error_log_filename = "file.err"
		# loadcase.scheme.rpartition("/")[2] - actual filename
		# for example
		# path = /home/user/mechanical/file.dat
		# path.rparition("/")[2] = "file.dat"
		dat_filename = loadcase.scheme.rpartition("/")[2]
		create_file(loadcase.inData, dat_filename)
		if (loadcase.solver_params is not None):
			options = loadcase.solver_params.split()
		else:
			options = []
		options.append("-i")
		options.append(dat_filename)
		options.append("-o")
		options.append(output_filename)
		if ("-j" in options):
			res_index = options.index("-j") + 1
			local_error_log_filename = options[res_index] + ".err"

		if sys.platform.startswith('win'):
			pass
		elif sys.platform.startswith('linux'):
			self.logger.info('executing ANSYS Mechanical Solver')
			subprocess.call(self._exec_path + options)
			self.logger.info('ANSYS Mechanical Solver finished')
		else:
			self.logger.error('ERROR: Сan not determine your platform')
			loadcase.status = constants.ERROR_STATUS

		self.update_global_log(local_error_log_filename)
		error_flag = self.check_log(local_error_log_filename)

		os.chdir(cwd)
		if (not error_flag):
			loadcase.status = constants.SUCCESS_STATUS
		loadcase.status = constants.ERROR_STATUS

	def check_log(self, log_filename):
		"""
		Checks error log file for warnings and errors,
		counts and prints them to stdout

		"""
		error_string = "*** ERROR ***"
		warning_string = "*** WARNING ***"
		warn_count = 0
		err_count = 0
		i = 0
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

		log_file.seek(0)
		for line in log_file:
			i += 1  #skipping 2 lines that say when ANSYS was launched
			if (i > 2):
				if warning_string in line:
					warn_count += 1
				elif error_string in line:
					err_count += 1
				print line

		log_file.close()
		self.print_problems(warn_count, err_count)
		return error_flag

	def delete_local_log(self):
		"""
		Deletes local error log file (its name is "*.err", but not "global.err") in current directory

		"""
		files_list = os.listdir(".")
		for entry in files_list:
			if ".err" in entry:
				if self.error_log_name not in entry:
					os.remove(entry)

	def update_global_log(self, local_log_filename):
		"""
		Appends lines from local_log_file to global_log_file

		"""
		try:
			global_log_file = open(self.error_log_name, "a")
		except IOError:
			self.logger.error("Can not open \"" + self.error_log_name + "\" for appending")
			return None
		try:
			local_log_file = open(local_log_filename, "r")
		except IOError:
			self.logger.error("Can not open \"" + local_log_filename + "\" for reading")
			return None
		#append lines from local_log_file to global_log_file
		for line in local_log_file:
			global_log_file.write(line)
		global_log_file.write("\n")
		local_log_file.close()
		global_log_file.close()

	def print_problems(self, warn_count, err_count):
		if (warn_count == 1):
			self.logger.warning(str(warn_count) + " warning")
		elif (warn_count > 1):
			self.logger.warning(str(warn_count) + " warnings")
		if (err_count == 1):
			self.logger.error(str(err_count) + " error")
		elif (err_count > 1):
			self.logger.error(str(err_count) + " errors")
