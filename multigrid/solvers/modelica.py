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
import os
import ntpath
import sys
import constants
import launcher
import debug
from solvers.common_methods import create_file
from loadcase import Loadcase
from solversloadcase import SolversLoadcase
import OMPython as omp

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

def create_mo_files_dict(mos_file_path):
	"""
	:param mos_file_path:
	:return: dictionary of mo files, listed in specified mos-file
	"""
	files_dict = {}
	cwd = os.getcwd()
	#filenames.append(re.search('(\w)+\.mos', MOS_file_path).group())
	with open(mos_file_path, 'r') as mos:#mos = open(MOS_file_path, 'r')
		if (mos_file_path.rpartition('/')[0] != 0):
			os.chdir(mos_file_path.rpartition('/')[0])
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
	"""
	:param params: string or dictionary of parameters for simulation of the Modelica model
	:return: formatted string to use in simulate(...) command
	"""
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

def lrp_file_content(mo_filename, class_name, simulate_params):
	"""
	lrp - last run parameters
	:param mo_filename: name of file with Modelica model
	:param class_name: name of class inside file with Modelica model
	:param simulate_params: parameters for simulation
	:return: strings for creating lrp file
	"""
	f = []
	f.append('loadModel(Modelica);\n')
	f.append('loadFile("' + mo_filename + '");\n')
	#f.append('simulate('+class_name+', '+simulate_params+', outputFormat="plt");\n')
	f.append('simulate('+class_name+', '+simulate_params+')')
	return f

def get_class_name_by_mo(mo_filename):
	"""
	:param mo_filename: name of mo-file
	:return: last class name read from mo-file (at this string: (model className)
	It's required for getting model's C code, its compilation and execution
	"""
	class_name = ''
	try:
		mo_file = open(mo_filename, "r")
	except IOError:
		logger.error("Can not open \"" + mo_filename + "\" for reading")
	for line in mo_file:
		if line.startswith("model"):
			class_name = line.split()[1]
	return class_name

class ModelicaSolver(launcher.Launcher):
	def compile(self, mo_filename, class_name, simulate_params):
		"""
		:param mo_filename: name of mo-file
		:param class_name: name of class inside mo-file
		:param simulate_params: parameters for simulation
		:return: constants.SUCCESS_STATUS if compilation was successful
		constants.ERROR_STATUS otherwise
		"""
		log = []
		if not omp.execute('loadModel(Modelica)'):
			omp.execute('getErrorString()')
			return constants.ERROR_STATUS
		load_file = 'loadFile("' + mo_filename + '")'
		if not omp.execute(load_file):
			logger.error('ERROR: could not load file "'+mo_filename+'"')
			omp.execute('getErrorString()')
			return constants.ERROR_STATUS
		simulate = 'simulate(' + class_name + ', ' + simulate_params + ')'
		log.append(omp.execute(simulate))
		log.append(omp.execute('getErrorString()'))
		return self.check(log)

	def run(self, loadcase, input_params):
		cwd = os.getcwd()
		# how did we come in directory "loadcases"?
		if not os.path.exists(loadcase.name):
			os.makedirs(loadcase.name)
		os.chdir(loadcase.name)
		omp.execute('cd("' + os.getcwd() + '")')
		mo_filename = ntpath.basename(loadcase.scheme)
		par_filename = "last_run_parameters.txt"
		create_file(loadcase.inData, mo_filename)

		params_string = generate_params_string(loadcase.solver_params)
		class_name = get_class_name_by_mo(mo_filename)
		recomp_flag = self.recompilation(par_filename, mo_filename, class_name, loadcase.solver_params)
		#create mo-file on worker
		create_file(lrp_file_content(mo_filename, class_name, params_string), par_filename)
		par_filename = 'pl.txt'
		res_filename = 'results.mat'

		# create file with input parameters using dictionaries of input parameters
		self.create_par_files_from_dicts(par_filename, input_params)
		if recomp_flag:
			if self.compile(mo_filename, class_name, params_string) == constants.ERROR_STATUS:
				loadcase.status = constants.ERROR_STATUS
				logger.error("ERROR in compilation")
				os.chdir(cwd)
				return None
		if sys.platform.startswith('win'):
			exec_filename = class_name + '.exe'
		elif sys.platform.startswith('linux'):
			exec_filename = './' + class_name
		else:
			logger.info("Can not determine type of your OS")
			loadcase.status = constants.ERROR_STATUS
			return None
		#logger.info("Begin executing")
		if omp.execute('system("'+exec_filename+' -overrideFile '+par_filename+' -r '+res_filename+'")') != 0:
			loadcase.status = constants.ERROR_STATUS
			logger.error("ERROR in execution process")
			os.chdir(cwd)
			return None
		#logger.info("End executing")
		# getting dictionary of output parameters
		result = self.create_results_dict(res_filename)
		loadcase.status = constants.SUCCESS_STATUS
		os.chdir(cwd)
		return result

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

	def create_par_files_from_dicts(self, par_filename, par_dict):
		"""
		Creates files of input parameters using dictionaries of input parameters

		"""
		with open(par_filename, 'w') as PAR_file:
			for k, v in par_dict.iteritems():
				PAR_file.write(k + '=' + str(v) + '\n')

	def create_results_dict(self, res_filename):
		"""
		Creates dictionary of results using result file named "res_filename"

		"""
		result_dict = {}
		# read all names of variables from "res_filename"
		res = omp.execute('readSimulationResultVars("'+res_filename+'")')
		# create list of variables' names
		temp_vars_list = omp.get(res, 'SET1.Values')[0].split(',')
		# delete first and last " symbols
		vars_list = [variable[1:-1] for variable in temp_vars_list]
		for key in vars_list:
			values_list = omp.execute('readSimulationResult("'+res_filename+'", '+key+')')
			# it is a workaround, because we have troubles with getting variables with
			# complex names, for example, der(der(mass1.flange_b.s)) (names with brackets)
			if len(values_list):
				# delete last value ([:-1]), because it is the same as penultimate
				result_dict[key] = omp.get(values_list, 'SET2.Set1')[:-1]
		omp.execute('closeSimulationResultFile()')

		return result_dict

	def check(self, log_list):
		"""
		:param log_list: list of output from OpenModelica API commands executed by OMPython
		:return: constants.SUCCESS_STATUS if there is no errors in output;
		constants.SUCCESS_STATUS otherwise
		"""
		error_flag = False
		for log in log_list:
			if ('Error' or 'Fail') in log:
				print log
				error_flag = True
		if error_flag:
			return constants.ERROR_STATUS
		return constants.SUCCESS_STATUS

	def recompilation(self, lrp_filename, mo_filename, class_name, params_dict):
		"""
			Checks the need for compilation.
			All reasons for compilation are based on checking of file called "last_run_parameters.txt".
			We need to compile if:
			1) there is no such file ("last_run_parameters.txt" does not exist), so we can suppose it is first run
			2) the name of the file to load changed in string: "loadFile(...)"
			3) the name of the class changed in string: "simulate(class_name, ...)"
			4) values or amount of parameters for solver changed in string: "simulate(class_name, solver_params)"
			"""
		recompile_flag = False
		if sys.platform.startswith('win'):
			if not os.path.isfile(class_name + ".exe"):
				# There is no any executable file, so we really need to compile
				return True
		elif sys.platform.startswith('linux'):
			if not os.path.isfile(class_name):
				return True
		else:
			logger.info("Can not determine type of your OS")
		if os.path.isfile(lrp_filename):
			try:
				lrp_file = open(lrp_filename, "r")
			except IOError:
				logger.error("Can not open \"" + lrp_filename + "\" for reading")
				return constants.ERROR_STATUS
		else:
			print 'There is no file with last run parameters.'
			print 'REASON 1: First execution'
			return True
		for line in lrp_file:
			if line.startswith("loadFile("):
				# line.split('"')[1] is the name of file to load
				if(line.split('"')[1] != mo_filename):
					recompile_flag = True
					print "REASON 2: model's name changed"
					break
			if line.startswith("simulate("):
				model_name = re.search('\(\w+\,', line).group(0)[1:-1]
				if(model_name != class_name):
					recompile_flag = True
					print "REASON 3: class name changed"
					break
				lrp_params_dict = self.params_dict_from_simulate(line)
				if not self.compare_params_dicts(lrp_params_dict, self.dict_with_str_values(params_dict)):
					recompile_flag = True
					print "REASON 4: solver params changed"
					break
		return recompile_flag

	def params_dict_from_simulate(self, simulate_string):
		"""
		Generates dictionary of parameters using simulate string from mos file
		example of simulate string: "simulate(dcmotor, startTime=0.0, stopTime=10.0, ...)"
		Returns:
		dictionary of simulate parameters (for our example it will be: {'startTime': 0.0, 'stopTime': 10.0, ...}

		"""
		temp_params_list = simulate_string.split(',')
		# [-1][:-1] --> delete ")" symbol from last element of the list
		temp_params_list[-1] = temp_params_list[-1][:-1]
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
		#del params_dict['outputFormat']
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

	def dict_with_str_values(self, dictionary):
		"""
		Converts values of dictionary to string format
		"""
		for key, value in dictionary.iteritems():
			dictionary[key] = str(value)
		return dictionary
