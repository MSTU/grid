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

import re
import subprocess
import os
import ntpath
import sys
import constants
import launcher
import debug
from solvers.common_methods import create_file
from loadcase import Loadcase
from solversloadcase import SolversLoadcase

name = "ModelicaDynamic"
logger = debug.logger
log_filename = "compilation.log"

class ModelicaLoadcase(SolversLoadcase):
	"""
	Loadcase for ModelicaSolver.

	scheme: string
		Path to Modelica file.
	desc: string
		Loadcase name.
	criteria_list: list
		List of result parameters, which will be included in result dict
	solver_params : dict
		Dictionary of options which will pass to Modelica
		Example of dictionary of options:
		{'startTime' = 0.0, 'endTime' = 10.0, 'interval' = 0.1}

	"""
	def __init__(self, scheme, desc=constants.DEFAULT_LOADCASE, criteria_list=None, solver_params=None):
		SolversLoadcase.__init__(self, scheme, name, desc, criteria_list, solver_params)


	# preparing of data for calculation
	# writes dictionary in Loadcase variable inData
	# keys are mos and mo filenames; values are lists of the file string
	def load_data(self):
		Loadcase.load_data(self)

		#files_dict = dict() #files dictionary, where keys are filenames and values are list of file strings
		# load .mos file
		with open(self.scheme, 'r') as f:
			mo = f.readlines()
		# files_dict[MOS_filename] = mos
		# files_dict.update(create_mo_files_dict(self.scheme))
		self.inData = mo

def create_mo_files_dict(MOS_file_path):
	"""
	Returns a dictionary, where keys are mo filenames and values are list of mo file strings.
	Dictionary is created using mos file located at MOS_file_path

	"""
	files_dict = dict()
	cwd = os.getcwd()
	#filenames.append(re.search('(\w)+\.mos', MOS_file_path).group())
	with open(MOS_file_path, 'r') as mos:#mos = open(MOS_file_path, 'r')
		if (MOS_file_path.rpartition('/')[0] != 0):
			os.chdir(MOS_file_path.rpartition('/')[0])
		for line in mos:
			if (not line.startswith('loadFile')):
				pass
			else:
				mo_filename = re.search('(\w)+\.mo', line).group()
				#mo_filepath = MOS_file_path.rpartition('/')[0] + '/' + mo_filename
				with open(re.split('"', line)[1], 'r') as mo:
					mo_file = mo.readlines()
					files_dict[mo_filename] = mo_file
				#filenames.append(re.search('(\w)+\.mo', line).group())
	os.chdir(cwd)

	return files_dict

def generate_params_string(params):
	result = ''
	if isinstance(params, dict):
		for key, value in params.iteritems():
			result += key + '=' + str(value)
			result += ', '
		# delete last comma and space
		result = result[:-2]
	else:
		result = params
	return result

def create_mos_by_mo(mo_filename, class_name, simulate_params):
	mos_file = []
	mos_file.append('loadModel(Modelica);\n')
	mos_file.append('getErrorString();\n')
	mos_file.append('loadFile("' + mo_filename + '");\n')
	mos_file.append('getErrorString();\n')
	#mos_file.append('simulate(dcmotor, ' + generate_params_string(simulate_params) + ', outputFormat = "plt");\n')
	mos_file.append('simulate('+class_name+', '+generate_params_string(simulate_params)+', outputFormat="plt");\n')
	mos_file.append('getErrorString();\n')
	return mos_file

def get_class_name_by_mo(mo_filename):
	"""
	Returns last class name readed from mo-file (at this string: (model className)
	It's required for getting model's C code, its compilation and execution

	"""
	try:
		mo_file = open(mo_filename, "r")
	except IOError:
		logger.error("Can not open \"" + mo_filename + "\" for reading")
	for line in mo_file:
		if line.startswith("model"):
			#starting line: "model dcmotor\n"
			class_name = line[6:-2]
			#we are cutting 6 symbols from beginning: 'model '
			#and 2 symbols from ending: "\n"
	return class_name

class ModelicaSolver(launcher.Launcher):
	def compile(self, MOS_filename):
		"""
		compiles *.mo file using *.mos file to get exe-file of the model

		"""
		try:
			log_file = open(log_filename, "w")
		except IOError:
			logger.error("Can not create \"" + log_filename + "\"")
		logger.info("Begin compiling")
		if sys.platform.startswith('win'):
			command = '%OPENMODELICAHOME%/bin/omc.exe ' + MOS_filename
			subprocess.call(["cmd", "/C", command], stdout=log_file)
		elif sys.platform.startswith('linux'):
			subprocess.call(["omc", MOS_filename], stdout=log_file)
		else:
			logger.error("Can't determine platform")
			return constants.ERROR_STATUS
		logger.info("End compiling")
		log_file.close()
		return self.check_log()

	def run(self, loadcase, input_params):
		cwd = os.getcwd()
		if not os.path.exists(loadcase.name):
			os.makedirs(loadcase.name)
		os.chdir(loadcase.name)

		# Host creates all required files
		# for k, v in loadcase.inData.iteritems():
		# 	create_file_from_list(v, k)

		mo_filename = ntpath.basename(loadcase.scheme)
		#mos_filename = mo_filename[:-3] + generate_params_string(loadcase.solver_params) + '.mos'
		mos_filename = "script.mos"
		create_file(loadcase.inData, mo_filename)
		params_string = generate_params_string(loadcase.solver_params)
		class_name = get_class_name_by_mo(mo_filename)
		recomp_flag = self.recompilation(mos_filename, mo_filename, class_name, loadcase.solver_params)
		#class_name = self.get_class_name(mos_filename)
		create_file(create_mos_by_mo(mo_filename, class_name, loadcase.solver_params), mos_filename)
		par_filename = 'pl.txt'
		res_filename = 'results.plt'

		# create file with input parameters using dictionaries of input parameters
		self.create_par_files_from_dicts(par_filename, input_params)

		if sys.platform.startswith('win'):
			if(os.path.isfile(class_name + '.exe')):
				pass
			else:
				#self.compile(mos_filename) # getting exe-file using mo and mos files
				if(self.compile(mos_filename) == constants.ERROR_STATUS):
					loadcase.status = constants.ERROR_STATUS
					os.chdir(cwd)
					return None
			command = class_name + '.exe -overrideFile ' + par_filename + ' -r ' + res_filename
			logger.info("Begin executing")
			subprocess.call(["cmd", "/C", command])#, startupinfo=startupinfo)
			logger.info("End executing")
		elif sys.platform.startswith('linux'):
			if(recomp_flag):
				if(self.compile(mos_filename) == constants.ERROR_STATUS):
					loadcase.status = constants.ERROR_STATUS
					logger.error("ERROR in compilation")
					os.chdir(cwd)
					return None
			command = ['-overrideFile'] + [par_filename] + ['-r'] + [res_filename]
			logger.info("Begin executing")
			subprocess.call(["./" + class_name] + command)
			if not self.check_execution():
				loadcase.status = constants.ERROR_STATUS
				logger.error("ERROR in execution process")
				os.chdir(cwd)
				return None
			logger.info("End executing")

		else:
			logger.info("Can not determine type of your OS")
			loadcase.status = constants.ERROR_STATUS
			return None

		# getting dictionary of output parameters
		result = self.create_results_dict(res_filename)
		loadcase.status = constants.SUCCESS_STATUS

		os.remove(log_filename)
		os.chdir(cwd)
		return result

	# using this function you can specify simulate parameters listed in MOS file
	# for instance: setSimulateParameters('mos_file.mos', 'stopTime', 35.5)
	def setSimulateParameter(self, MOS_filename, par_name, par_value):
		temp_file = open('temp', 'w')
		with open(MOS_filename, 'r') as f:
			for line in f:
				if (not line.startswith('simulate')):
					temp_file.write(line)
				else:
					temp_file.write(re.sub(par_name + '( )?=( )?(\d)+(\.(\d)+)*', par_name + ' = ' + par_value, line))
					#par_name + '( )?=( )?(\d)+(\.(\d)+)*
					#line matches above pattern if it contains something like:
					#par_name(1 or 0 spaces)=(1 or 0 spaces)(any number of digits)
					#par_name(1 or 0 spaces)=(1 or 0 spaces)(any number of digits).(1 digit or more)
		temp_file.close()
		#now temp file is a full copy of MOS file with one difference in parameter value
		#parameter named "par_name" has changed its old value to "par_value"
		os.unlink(MOS_filename) #deleting old MOS file
		os.rename(temp_file.name, MOS_filename)
		#changed temp filename to MOS filename, so we can use old filename with new content

	def get_class_name(self, mos_filename):
		"""
		Returns class name readed from mos-file (at this string: (simulate(className, ...))
		It's required for getting model's C code, its compilation and execution

		"""
		class_name = None
		with open(mos_filename, 'r') as f:
			for line in f:
				if(not line.startswith('simulate')):
					pass
				else:
					class_name = re.split('[(,]', line)[1]

		return class_name

	def create_par_files_from_dicts(self, par_filename, par_dic):
		"""
		Creates files of input parameters using dictionaries of input parameters

		"""
		with open(par_filename, 'w') as PAR_file:
			for k, v in par_dic.iteritems():
				PAR_file.write(k + '=' + str(v) + '\n')

	def create_results_dict(self, RES_filename):
		"""
		Creates dictionary of results using result file named "RES_filename"

		"""
		curvesNumber = 0 # amount of output variables
		result_dict = dict() # dictionary of results
		value_list = list() # list of values of current output parameter

		with open(RES_filename, 'r') as f:
			for line in f:
				if (not line.startswith('DataSet: ')):
					continue
				curvesNumber += 1
				#MA_object.SetCurves(curvesNumber)
				key = re.split('DataSet: ', line)[1][:-1]
				for line in f:
					if (line != '\n'):
						value_list.append(float(re.split('[\d.e-], ', line)[1][:-1]))
					else:
						break
				tmp = list(value_list[:-1]) # removed last element,
				# because value_list[last] = value_list[last-1]
				result_dict[key] = tmp
				del value_list[:] # delete content of the whole list

		#MA_object.SetLayer(len(tmp))
		return result_dict

	def check_log(self):
		"""
		Checks compilation log file named "log_filename" for errors
		Returns:
		constants.ERROR_STATUS - if error occurred
		constants.SUCCESS_STATUS - otherwise

		"""
		error_flag = False
		try:
			log_file = open(log_filename, "r")
		except IOError:
			logger.error("Can not open \"" + log_filename + "\" for reading")
			return constants.ERROR_STATUS
		for line in log_file:
			if "Error" in line:
				error_flag = True
				print line
		log_file.close()
		if(error_flag):
			return constants.ERROR_STATUS
		return constants.SUCCESS_STATUS

	def check_execution(self, res_filename):
		"""
		Checks the result of execution. If result file was created, then it counts as successful run.
		Returns:
		False - if error occurred and result file was not created
		True - otherwise

		"""
		if os.path.exists(res_filename):
			return True
		return False

	def recompilation(self, mos_filename, mo_filename, class_name, params_dict):
		"""
		Checks the need for compilation. Opens
		All reasons for compilation are based on checking of mos file:
		1) if the name of the file to load changed in loadFile(...) string
		2) if the name of the class changed in simulate(class_name, ...) string
		3) if values or amount of parameters for solver changed in simulate(class_name, solver_params) string
		"""
		recompile_flag = False
		#params_dict_with_str_values = self.dict_with_str_values(params_dict)
		if not os.path.isfile(mos_filename):
			# if it is first run, then there won't be any mos file and we need to compile
			print 'NO MOS FILE'
			return True
		try:
			mos_file = open(mos_filename, "r")
		except IOError:
			logger.error("Can not open \"" + log_filename + "\" for reading")
			return constants.ERROR_STATUS
		for line in mos_file:
			if line.startswith("loadFile("):
				# line.split('"')[1] is the name of file to load
				if(line.split('"')[1] != mo_filename):
					recompile_flag = True
					print "REASON 1: model's name changed"
					break
			if line.startswith("simulate("):
				model_name = re.search('\(\w+\,', line).group(0)[1:-1]
				if(model_name != class_name):
					recompile_flag = True
					print "REASON 2: class name changed"
					break
				mos_params_dict = self.generate_params_dict_by_simulate_string(line)
				if not self.compare_params_dicts(mos_params_dict, self.dict_with_str_values(params_dict)):
					recompile_flag = True
					print "REASON 3: solver params changed"
					break
		return recompile_flag

	def generate_params_dict_by_simulate_string(self, simulate_string):
		"""
		Generates dictionary of parameters using simulate string from mos file
		example of simulate string: "simmulate(dcmotor, startTime=0.0, stopTime=10.0, ...)"
		Returns:
		dictionary of simulate parameters (for our example it will be: {'startTime': 0.0, 'stopTime': 10.0, ...}

		"""
		temp_params_list = simulate_string.split(',')
		params_list = []
		params_dict = {}
		# params_list now containts something like this:
		# ['simulate(dcmotor', ' stopTime=10.0', ' startTime=0.0', ' numberOfIntervals=10', ' outputFormat="plt");']
		del temp_params_list[0] # removed first element "'simulate(dcmotor'"
		# remove whitespace from beginning of each element
		for item in temp_params_list:
			params_list.append(item[1:])
		for item in params_list:
			temp_item = item.split('=')
			params_dict[temp_item[0]] = temp_item[1]
		del params_dict['outputFormat']
		return params_dict

	def compare_params_dicts(self, first_dict, second_dict):
		"""
		Compares two dicts.
		Returns:
		True - if dictionaries have similar keys and values
		False - otherwise

		"""
		result = False
		first_dict_length = len(first_dict)
		shared_items = set(first_dict.items()) & set(second_dict.items())
		if(len(shared_items) == first_dict_length):
			result = True
		return result

	def dict_with_str_values(self, dict):
		"""
		Converts values of dictionary to string format
		"""
		for key, value in dict.iteritems():
			dict[key] = str(value)
		return dict
