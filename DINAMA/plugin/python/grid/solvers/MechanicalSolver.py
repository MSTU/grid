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

import Constants
import Launcher


class MechanicalSolver(Launcher.Launcher):
	name = "ANSYS_Mechanical"
	# object initialization
	def __init__(self):
		Launcher.Launcher.__init__(self)
		self.error_log_name = "global.err" #global error log (for all runs)

	# Loads content of *.dat file in special variable inData
	def LoadData(self, lc):
		if not os.path.isfile(lc.scheme):
			print "ERROR: " + lc.scheme + " does not exist"
			return None
		with open(lc.scheme, 'r') as f:
			lc.inData = f.readlines()

	def Run(self, loadcase, ma_object):
		if loadcase.inData is None:
			print "ERROR: inData contains nothing"
			return Constants.ERROR_STATUS
		cwd = os.getcwd()
		if not os.path.exists(loadcase.Name): os.makedirs(loadcase.Name)
		os.chdir(loadcase.Name)
		self.DeleteLocalLog()
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
		self.CreateFileFromList(loadcase.inData, dat_filename)
		# mechanical is a list that contains the only string to launch
		# ANSYS Mechanical Solver in a batch mode
		# example for ANSYS version 14.5: ["/path_to_ansys_bin/ansys145"]
		mechanical = self.CreateMechanicalCommand()
		if (len(ma_object.options) != 0):
			options = self.CreateOptionsCommand(ma_object.options)
		else:
			options = []
		options.append("-i")
		options.append(dat_filename)
		options.append("-o")
		options.append(output_filename)
		if (len(loadcase.ResultFile) != 0):
			options.append("-j")
			options.append(loadcase.ResultFile)
			local_error_log_filename = loadcase.ResultFile + ".err"

		if sys.platform.startswith('win'):
			pass
		elif sys.platform.startswith('linux'):
			print 'executing ANSYS Mechanical Solver'
			subprocess.call(mechanical + options)
			print 'ANSYS Mechanical Solver finished'
		else:
			print 'ERROR: Сan not determine your platform'
			return Constants.ERROR_STATUS

		self.UpdateGlobalLog(local_error_log_filename)
		error_flag = self.CheckLog(local_error_log_filename)

		os.chdir(cwd)
		if (not error_flag):
			return Constants.SUCCESS_STATUS
		return Constants.ERROR_STATUS

	# Creates file from list of strings
	def CreateFileFromList(self, stringList, filename):
		with open(filename, 'w') as f:
			for line in stringList:
				f.write(line)

	# Creates string to launch ANSYS Mechanical Solver
	def CreateMechanicalCommand(self):
		ANSYS_version = self.GetANSYSVersion()
		if ANSYS_version is not None:
			mech_command = ["/ansys_inc/v" + ANSYS_version + "/ansys/bin/ansys" + ANSYS_version,
			                "-b", "-p", "ANSYS"]
			return mech_command
		else:
			return []

	# Creates list of options for ANSYS Mechanical Solver
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

	# Checks error log file for warnings and errors,
	# counts and prints them to stdout
	def CheckLog(self, log_filename):
		error_string = "*** ERROR ***"
		warning_string = "*** WARNING ***"
		warn_count = 0
		err_count = 0
		error_flag = False
		i = 0
		try:
			log_file = open(log_filename, "r")
		except IOError:
			print "Can not open \"" + log_filename + "\" for reading"
			return None
		for line in log_file:
			if error_string in line:
				error_flag = True
				break

		log_file.seek(0)
		for line in log_file:
			i += 1 #skipping 2 lines that say when ANSYS was launched
			if (i > 2):
				if warning_string in line:
					warn_count += 1
				elif error_string in line:
					err_count += 1
				print line

		log_file.close()
		self.PrintProblems(warn_count, err_count)
		return error_flag

	# Deletes local error log file (its name is "*.err", but not "global.err") in current directory
	def DeleteLocalLog(self, ):
		files_list = os.listdir(".")
		for entry in files_list:
			if ".err" in entry:
				if self.error_log_name not in entry:
					os.remove(entry)

	# Appends lines from local_log_file to global_log_file
	def UpdateGlobalLog(self, local_log_filename):
		try:
			global_log_file = open(self.error_log_name, "a")
		except IOError:
			print "Can not open \"" + self.error_log_name + "\" for appending"
			return None
		try:
			local_log_file = open(local_log_filename, "r")
		except IOError:
			print "Can not open \"" + local_log_filename + "\" for reading"
			return None
		#append lines from local_log_file to global_log_file
		for line in local_log_file:
			global_log_file.write(line)
		global_log_file.write("\n")
		local_log_file.close()
		global_log_file.close()

	def PrintProblems(self, warn_count, err_count):
		if (warn_count == 1):
			print str(warn_count) + " warning"
		elif (warn_count > 1):
			print str(warn_count) + " warnings"
		if (err_count == 1):
			print str(err_count) + " error"
		elif (err_count > 1):
			print str(err_count) + " errors"
