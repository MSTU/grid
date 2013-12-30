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
import re
import sys
import shutil

import Constants
import Launcher


class CFXSolver(Launcher.Launcher):
	name = "ANSYS_CFX"

	# Loads content of *.def file in special variable inData
	def LoadData(self, lc):
		if not os.path.isfile(lc.scheme):
			print "ERROR: " + lc.scheme + " does not exist"
			return None
		with open(lc.scheme, 'r') as f:
			lc.inData = f.readlines()

	def Run(self, loadcase, ma_object):
		if loadcase.inData is None:
			print "ERROR: inData contains nothing"
			return Constants.TASK_ERROR
		cwd = os.getcwd()
		if not os.path.exists(loadcase.Name): os.makedirs(loadcase.Name)
		os.chdir(loadcase.Name)
		error_log_filename = "CFX_error_log"
		try:
			error_log_file = open(error_log_filename, "w")
		except IOError:
			print "Can not create \"" + error_log_filename + "\""
			return Constants.TASK_ERROR
		# loadcase.scheme.rpartition("/")[2] - actual filename
		# for example
		# path = /home/user/cfx/file.def
		# path.rparition("/")[2] = "file.def"
		def_filename = loadcase.scheme.rpartition("/")[2]
		self.CreateFileFromList(loadcase.inData, def_filename)
		#cfx is a list that contains the only string to launch ANSYS CFX solver
		#example: ["/path_to_cfx_bin/cfx5solve"]
		cfx = self.CreateCFXCommand()
		if (len(ma_object.options) != 0):
			options = self.CreateOptionsCommand(ma_object.options)
		else:
			options = []
		options.append("-def")
		options.append(def_filename)
		if (len(loadcase.ResultFile) != 0):
			options.append("-fullname")
			options.append(loadcase.ResultFile)
			temp_dir_path = loadcase.ResultFile + ".dir"
			self.DeleteTempDir(temp_dir_path)

		if sys.platform.startswith('win'):
			pass
		elif sys.platform.startswith('linux'):
			print 'executing ANSYS CFX Solver'
			subprocess.call(cfx + options, stderr=error_log_file)
			print 'ANSYS CFX Solver finished'
		else:
			print 'ERROR: Сan not determine your platform'
			return Constants.TASK_ERROR
		error_log_file.close()
		if (os.path.getsize(error_log_filename) == 0):
			error_flag = False
			os.remove(error_log_filename)
		else:
			error_flag = self.checkLog(error_log_filename)

		os.chdir(cwd)
		if (not error_flag):
			return Constants.TASK_SUCCESS
		return Constants.TASK_ERROR

	# Creates file from list of strings
	def CreateFileFromList(self, stringList, filename):
		with open(filename, 'w') as f:
			for line in stringList:
				f.write(line)

	# Creates string to launch ANSYS CFX solver
	def CreateCFXCommand(self):
		ANSYS_version = self.GetANSYSVersion()
		if ANSYS_version is not None:
			cfx_command = ["/ansys_inc/v" + ANSYS_version + "/CFX/bin/cfx5solve"]
			return cfx_command
		else:
			return []

	# Creates list of options for ANSYS CFX solver
	# option, its arguments
	def CreateOptionsCommand(self, options):
		options_command = options.split()
		return options_command

	# Determines ANSYS version
	def GetANSYSVersion(self):
		if sys.platform.startswith('win'):
			pass
		elif sys.platform.startswith('linux'):
			if (os.path.isdir("/ansys_inc")):
				dir_list = os.listdir("/ansys_inc")
				for line in dir_list:
					temp = re.search("v[\d]+", line)
					if temp is not None:
						version = temp.group(0)[1:]
						return version
			else:
				print "ERROR: Сan not locate your ANSYS installation directory"
		else:
			print 'ERROR: Сan not determine your platform'
		return None

	# Checks error log file for errors, because
	# sometimes CFX Solver writes something in stderr stream, but it is not an error
	# example
	# with -v option CFX Solver writes in stderr:
	# "Adding host antonpc (Anton-PC) (linux-amd64) to the parallel environment."
	def checkLog(self, log_filename):
		error_string = "An error has occurred in cfx5solve:"
		error_flag = False
		try:
			log_file = open(log_filename, "r")
		except IOError:
			print "Can not open \"" + log_filename + "\" for reading"
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

	# This function deletes a directory which is created only when you specify -save
	# option to CFX solver execution command
	# When you specify -save and loadcase.ResultFile is not empty string CFX Solver will not work after first run.
	# If that temporary directory already exists and you run CFX solver for second time with the same
	# loadcase.ResultFile (the same result file name) it will crash and say: "There is already definition file,
	# refusing to create another one". It is because of "def" file inside that temporary directory
	# This function was written to fix such behavior of ANSYS CFX Solver
	def DeleteTempDir(self, dir_name):
		if (os.path.isdir(dir_name)):
			shutil.rmtree(dir_name)