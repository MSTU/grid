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

import sys
import debug
import constants
import launcher
from solvers.ansys.ansys_methods import get_ansys_version
from solvers.ansys.common_methods import create_file_from_list


class LSDYNASolver(launcher.Launcher):
	name = "ANSYS_LS-DYNA"
	_version = get_ansys_version()
	_exec_path = ["/ansys_inc/v" + _version + "/ansys/bin/lsdyna" + _version]

	# object initialization
	def __init__(self):
		launcher.Launcher.__init__(self)
		self.exec_options = ["G", "D", "F", "T", "A", "M", "S", "Z",
		                     "L", "B", "W", "E", "X", "C", "K", "V",
		                     "Y", "BEM", "MEMORY", "NCPU",
		                     "PARA", "ENDTIME", "NCYCLE",
		                     "JOBID", "D3PROP", "GMINP", "GMOUT",
		                     "MCHECK"]
		self.logger = debug.logger

	# Loads content of *.k file in special variable inData
	def load_data(self, lc):
		if not os.path.isfile(lc.scheme):
			self.logger.error("ERROR: " + lc.scheme + " does not exist")
			return None
		with open(lc.scheme, 'r') as f:
			lc.inData = f.readlines()

	def run(self, loadcase, input_params):
		if loadcase.inData is None:
			self.logger.error("ERROR: inData contains nothing")
			return constants.ERROR_STATUS
		cwd = os.getcwd()
		if not os.path.exists(loadcase.name): os.makedirs(loadcase.name)
		os.chdir(loadcase.name)
		log_filename = "ls_dyna_log"
		try:
			log_file = open(log_filename, "w")
		except IOError:
			self.logger.error("ERROR: Can not create \"" + log_filename + "\"")
			loadcase.status = constants.ERROR_STATUS
		# loadcase.scheme.rpartition("/")[2] - actual filename
		# for example
		# path = /home/user/ls-dyna/file.k
		# path.rparition("/")[2] = "file.k"
		k_filename = loadcase.scheme.rpartition("/")[2]
		create_file_from_list(loadcase.inData, k_filename)
		# options is a list of option strings: ["option_1=value_1", "option_2=value_2"]
		# there are options for LS DYNA command in ModelAnalysis parameters' dictionary
		if(loadcase.solver_params is not None):
			options = self.create_options_command(loadcase.solver_params)
		else:
			options = []
		options += ["I=" + k_filename]

		if sys.platform.startswith('win'):
			pass
		elif sys.platform.startswith('linux'):
			self.logger.info('executing LS-DYNA')
			subprocess.call(self._exec_path + options, stdout=log_file)
			self.logger.info('LS-DYNA finished')
		else:
			self.logger.error('Сan not determine your platform')
			loadcase.status = constants.ERROR_STATUS
		log_file.close()
		return_code = self.check_log(log_filename)
		os.chdir(cwd)

		if (return_code == 1):
			loadcase.status = constants.SUCCESS_STATUS
		else:
			self.logger.error("ERROR Termination")
			self.logger.error("Check \"" + log_filename + "\" for a more detailed description")
			loadcase.status = constants.ERROR_STATUS
		return None


	def create_options_command(self, solver_params):
		"""
		Creates string of options for LS-DYNA
		Args: string of solver parameters
		Returns: list. Its length is equal to amount of parameters in input string

		"""
		if((solver_params.find("I=") or solver_params.find("I =")) != -1):
			self.logger.error("ERROR: You have already specified name of the input file in loadcase definition")
		index = solver_params.find("=")
		while(index != -1):
			temp = solver_params
			# there are whitespaces on both sides of = ("option = value")
			if(solver_params[index-1:index] == " " and solver_params[index+1:index+2] == " "):
				temp = solver_params[:index-1] + "=" + solver_params[index+2:]
			# there is only one whitespace on left side of = ("option =value")
			elif(solver_params[index-1:index] == " "):
				temp = solver_params[:index-1] + solver_params[index:]
			# there is only one whitespace on the right side of = ("option= value")
			elif(solver_params[index+1:index+2] == " "):
				temp = solver_params[:index+1] + solver_params[index+2:]
			index = temp.find("=", index+1)
			solver_params = temp
		options_command = solver_params.split()
		return options_command

	def check_log(self, log_filename):
		"""
		Checks error log file called "log_filename" for errors
		Returns:
		-1 -- if error occurred
		1 -- otherwise

		"""
		normal_string = "Normaltermination"
		flag = -1
		try:
			log_file = open(log_filename, "r")
		except IOError:
			self.logger.error("Can not open \"" + log_filename + "\" for reading")
			return None
		#string about termination is the last line
		#we move by 90 bytes from the end to the beginning of the file,
		#because last line is approximately < 90 bytes in length

		#we are using line.replace(" ", "") to delete all whitespaces,
		#because there are too many of them
		log_file.seek(-90, 2)
		for line in log_file:
			if normal_string in line.replace(" ", ""):
				flag = 1

		log_file.close()
		return flag
