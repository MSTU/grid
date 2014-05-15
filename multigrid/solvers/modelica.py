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

import re
import os
import ntpath
import sys
import shutil
import time
import subprocess
import launcher

from multigrid import constants
from multigrid import debug
from multigrid.solvers.common_methods import create_file
from multigrid.solvers.solversloadcase import SolversLoadcase
from multigrid.conf import configworker

name = "ModelicaDynamic"
logger = debug.logger
log_filename = "compilation.log"

def timeit(method):

	def timed(*args, **kw):
		ts = time.time()
		result = method(*args, **kw)
		te = time.time()

		print '%r (%r, %r) %2.2f sec' % \
			  (method.__name__, args, kw, te-ts)
		return result

	return timed

class ModelicaLoadcase(SolversLoadcase):
	"""
	Loadcase for ModelicaSolver.

	scheme: string
		Path to Modelica file.
	desc: string
		Loadcase name.
	is_filetransfer: bool
		True if files are big and file transfer need, False otherwise
	transfer_params: dict
		Contain information about files included in model
	criteria_list: list
		List of result parameters, which will be included in result dict
	solver_params : dict
		Dictionary of options which will pass to Modelica
		Example of dictionary of options:
		{'startTime' = 0.0, 'endTime' = 10.0, 'interval' = 0.1}

	"""
	def __init__(self, scheme, desc=constants.DEFAULT_LOADCASE, is_filetransfer=False, transfer_params=None, criteria_list=None, solver_params=None):
		SolversLoadcase.__init__(self, scheme, name, desc, is_filetransfer, transfer_params, criteria_list, solver_params)
		self.load_data()

	# preparing of data for calculation
	# writes dictionary in Loadcase variable inData
	# keys are mos and mo filenames; values are lists of the file string
	def load_data(self):
		if not self.is_filetransfer:
			#files_dict = dict() #files dictionary, where keys are filenames and values are list of file strings
			# load .mos file
			with open(self.scheme, 'r') as f:
				mo = f.readlines()
			# files_dict[MOS_filename] = mos
			# files_dict.update(CreateMOfilesDict(self.scheme))
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
	f.append('simulate('+class_name+', '+simulate_params+', outputFormat="plt")\n')
	#f.append('simulate('+class_name+', '+simulate_params+')')
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
		import traceback
		traceback.print_exc()
		logger.error("Can not open \"" + mo_filename + "\" for reading")
	for line in mo_file:
		if line.startswith("model"):
			class_name = line.split()[1]
	return class_name

def create_mos_by_mo(mo_filename, class_name, simulate_params):
	mos_file = []
	mos_file.append('loadModel(Modelica);\n')
	mos_file.append('getErrorString();\n')
	mos_file.append('loadFile("' + mo_filename + '");\n')
	mos_file.append('getErrorString();\n')
	mos_file.append('simulate('+class_name+', '+generate_params_string(simulate_params)+', outputFormat="plt");\n')
	mos_file.append('getErrorString();\n')
	return mos_file

class ModelicaSolver(launcher.Launcher):
	#@timeit
	def compile(self, mos_filename):
		"""
		compiles *.mo file using *.mos file to get exe-file of the model
		"""
		try:
			log_file = open(log_filename, "w")
		except IOError:
			logger.error("Can not create \"" + log_filename + "\"")
		logger.info("Begin compiling")
		if sys.platform.startswith('win'):
			command = '%OPENMODELICAHOME%/bin/omc.exe ' + mos_filename
			subprocess.call(["cmd", "/C", command], stdout=log_file)
		elif sys.platform.startswith('linux'):
			subprocess.call(["omc", mos_filename], stdout=log_file)
		else:
			logger.error("Can't determine platform")
			return constants.ERROR_STATUS
		logger.info("End compiling")
		log_file.close()
		return self.check_log()
	#@timeit
	def run(self, loadcase, input_params):
		cwd = os.getcwd()
		if not os.path.exists(loadcase.name):
			os.makedirs(loadcase.name)
		os.chdir(loadcase.name)

		try:
			mo_filename = ntpath.basename(loadcase.scheme)
			mos_filename = "script.mos"
			par_filename = 'pl.txt'
			res_filename = 'results.plt'
			if not loadcase.is_filetransfer:
				create_file(loadcase.inData, mo_filename)

			params_string = generate_params_string(loadcase.solver_params)
			class_name = get_class_name_by_mo(mo_filename)
			recomp_flag = self.recompilation(mos_filename, mo_filename, class_name, loadcase.solver_params)
			#create mo-file on worker
			create_file(create_mos_by_mo(mo_filename, class_name, loadcase.solver_params), mos_filename)

			# create file with input parameters using dictionaries of input parameters
			self.create_par_files_from_dicts(par_filename, input_params)
			if recomp_flag:
				if self.compile(mos_filename) == constants.ERROR_STATUS:
					loadcase.status = constants.ERROR_STATUS
					logger.error("ERROR in compilation")
					os.chdir(cwd)
					return None
			if sys.platform.startswith('win'):
				command = class_name + '.exe -overrideFile ' + par_filename + ' -r ' + res_filename
				#logger.info("Begin executing")
				subprocess.call(["cmd", "/C", command])#, startupinfo=startupinfo)
				#logger.info("End executing")
			elif sys.platform.startswith('linux'):
				command = ['-overrideFile'] + [par_filename] + ['-r'] + [res_filename]
				logger.info("Begin executing")
				#logger.info("Begin executing")
				subprocess.call(["./" + class_name] + command)
				#logger.info("End executing")
			else:
				logger.info("Can not determine type of your OS")
				loadcase.status = constants.ERROR_STATUS
				os.chdir(cwd)
				return None
			if not self.check_execution(res_filename):
				loadcase.status = constants.ERROR_STATUS
				logger.error("ERROR in execution process")
				os.chdir(cwd)
				return None

			# if file transfer doesn't need parse file result in memory
			# otherwise return path to result file on worker
			if not loadcase.is_filetransfer:
				# getting dictionary of output parameters
				result = self.create_results_dict(res_filename)
			else:
				# store result file in FTP directory with name = task.id + .plt
				filename = str(loadcase.task_id) + '.plt'
				result_file_path = os.path.join(configworker.FTP_PATH, filename)
				# move result file
				shutil.move(res_filename, result_file_path)
				# store host and path to file in result
				result = dict()
				result['host'] = configworker.IP_ADDRESS
				result['file'] = filename

			loadcase.status = constants.SUCCESS_STATUS
			return result
		finally:
			os.chdir(cwd)

	def get_class_name(self, mos_filename):
		"""
		Returns class name readed from mos-file (at this string: (simulate(className, ...))
		It's required for getting model's C code, its compilation and execution
		"""
		class_name = None
		with open(mos_filename, 'r') as f:
			for line in f:
				if (not line.startswith('simulate')):
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
	#@timeit
	def create_results_dict(self, res_filename):
		"""
		Creates dictionary of results using result file named "res_filename"
		"""
		result_dict = {} # dictionary of results
		value_list = [] # list of values of current output parameter

		with open(res_filename, 'r') as f:
			for line in f:
				if not line.startswith('DataSet: '):
					continue
				key = re.split('DataSet: ', line)[1][:-1]
				for	string in f:
					if string != '\n':
						value_list.append(float(re.split('[\d.e-], ', string)[1][:-1]))
					else:
						break
				tmp = list(value_list[:-1]) # removed last element,
				# because value_list[last] = value_list[last-1]
				result_dict[key] = tmp
				del value_list[:] # delete content of the whole list
		return result_dict

	def recompilation(self, mos_filename, mo_filename, class_name, solver_params):
		"""
		Checks the need for compilation.
		All reasons for compilation are as follows:
		1) if there is no mos-file
		2) if there is no executable file
		3) if the name of the file to load changed in loadFile(...) string
		4) if the name of the class changed in simulate(class_name, ...) string
		5) if values or amount of parameters for solver changed in simulate(class_name, solver_params) string
		"""
		recompile_flag = False
		if sys.platform.startswith('win'):
			exec_name = class_name + '.exe'
		elif sys.platform.startswith('linux'):
			exec_name = class_name
		else:
			logger.info("Can not determine type of your OS")
			return constants.ERROR_STATUS
		if not os.path.isfile(mos_filename):
			# if it is first run, then there won't be any mos file and we need to compile
			print 'REASON 1: No mos-file'
			return True
		if not os.path.isfile(exec_name):
			# There is no any executable file, so we really need to compile
			print 'REASON 2: No executable file'
			return True
		try:
			mos_file = open(mos_filename, "r")
		except IOError:
			logger.error("Can not open \"" + mos_filename + "\" for reading")
			return constants.ERROR_STATUS
		for line in mos_file:
			if line.startswith("loadFile("):
				# line.split('"')[1] is the name of file to load
				if(line.split('"')[1] != mo_filename):
					recompile_flag = True
					print "REASON 3: model's name changed"
					break
			if line.startswith("simulate("):
				model_name = re.search('\(\w+\,', line).group(0)[1:-1]
				if(model_name != class_name):
					recompile_flag = True
					print "REASON 4: class name changed"
					break
				mos_params_dict = self.params_dict_by_string(line)
				params_dict = {}
				if isinstance(solver_params, basestring):
					params_dict = self.params_dict_by_string(solver_params)
				elif isinstance(solver_params, dict):
					params_dict = self.dict_with_str_values(solver_params)
				if not self.compare_params_dicts(mos_params_dict, params_dict):
					recompile_flag = True
					print "REASON 5: solver params changed"
					break
		return recompile_flag

	def params_dict_by_string(self, string):
		"""
		Generates dictionary of parameters using simulate string from mos file or just user's input string
		example of simulate string: "simulate(dcmotor, startTime=0.0, stopTime=10.0, ...)"
		example of user's input string: "startTime=0.0, stopTime=10.0, stepSize=0.05, ..."
		You can specify in "solver_params" string as many whitespaces, as you wish,
		because they are ignored while parsing.
		Returns:
		dictionary of simulate parameters (for our example it will be: {'startTime': 0.0, 'stopTime': 10.0, ...}
		"""
		params_dict = {}
		params_list = string.replace(' ', '').split(',')
		# params_list now containts something like this:
		# ['simulate(dcmotor', 'stopTime=10.0', 'startTime=0.0', 'numberOfIntervals=10', 'outputFormat="plt")\n']
		if string.startswith('simulate'):
			#del temp_params_list[0] # removed first element "'simulate(dcmotor'"
			del params_list[0] # removed first element "'simulate(dcmotor'"
		for item in params_list:
			temp_item = item.split('=')
			params_dict[temp_item[0]] = temp_item[1]
		if 'outputFormat' in params_dict.keys():
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
		if len(shared_items) == first_dict_length:
			result = True
		if not result:
			print 'mos-file: ', first_dict
			print 'solver params: ', second_dict
		return result

	def dict_with_str_values(self, dictionary):
		"""
		Converts values of dictionary to string format
		"""
		for key, value in dictionary.iteritems():
			dictionary[key] = str(value)
		return dictionary

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

	#Methods using OMPython library
	#@timeit
	def omp_compile(self, mo_filename, class_name, simulate_params):
		"""
		:param mo_filename: name of mo-file
		:param class_name: name of class inside mo-file
		:param simulate_params: parameters for simulation
		:return: constants.SUCCESS_STATUS if compilation was successful
		constants.ERROR_STATUS otherwise
		"""
		import OMPython as omp
		log = []
		if not omp.execute('loadModel(Modelica)'):
			omp.execute('getErrorString()')
			return constants.ERROR_STATUS
		load_file = 'loadFile("' + mo_filename + '")'
		if not omp.execute(load_file):
			logger.error('ERROR: could not load file "'+mo_filename+'"')
			omp.execute('getErrorString()')
			return constants.ERROR_STATUS
		simulate = 'simulate(' + class_name + ', ' + simulate_params + ', outputFormat="plt")'
		log.append(omp.execute(simulate))
		log.append(omp.execute('getErrorString()'))
		return self.omp_check(log)
	#@timeit
	def omp_run(self, loadcase, input_params):
		import OMPython as omp
		cwd = os.getcwd()
		# how did we come in directory "loadcases"?
		if not os.path.exists(loadcase.name):
			os.makedirs(loadcase.name)
		os.chdir(loadcase.name)

		try:
			omp.execute('cd("' + os.getcwd() + '")')
			mo_filename = ntpath.basename(loadcase.scheme)
			lrp_filename = "last_run_parameters.txt"
			par_filename = 'pl.txt'
			res_filename = 'results.plt'
			if not loadcase.is_filetransfer:
				create_file(loadcase.inData, mo_filename)

			params_string = generate_params_string(loadcase.solver_params)
			class_name = get_class_name_by_mo(mo_filename)
			recomp_flag = self.omp_recompilation(lrp_filename, mo_filename, class_name, loadcase.solver_params)
			#create mo-file on worker
			create_file(lrp_file_content(mo_filename, class_name, params_string), lrp_filename)

			# create file with input parameters using dictionaries of input parameters
			self.create_par_files_from_dicts(par_filename, input_params)
			if recomp_flag:
				if self.omp_compile(mo_filename, class_name, params_string) == constants.ERROR_STATUS:
					loadcase.status = constants.ERROR_STATUS
					logger.error("ERROR in compilation")
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
				return None
			#logger.info("End executing")

			# if file transfer doesn't need parse file result in memory
			# otherwise return path to result file on worker
			if not loadcase.is_filetransfer:
				# getting dictionary of output parameters
				result = self.create_results_dict(res_filename)
			else:
				# store result file in FTP directory with name = task.id + .plt
				filename = str(loadcase.task_id) + '.plt'
				result_file_path = os.path.join(configworker.FTP_PATH, filename)
				# move result file
				shutil.move(res_filename, result_file_path)
				# store host and path to file in result
				result = dict()
				result['host'] = configworker.IP_ADDRESS
				result['file'] = filename

			loadcase.status = constants.SUCCESS_STATUS
			os.chdir(cwd)
			return result
		finally:
			os.chdir(cwd)
	#@timeit
	def omp_create_results_dict(self, res_filename):
		"""
		Creates dictionary of results using result file named "res_filename"
		"""
		import OMPython as omp
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

	def omp_recompilation(self, lrp_filename, mo_filename, class_name, solver_params):
		"""
		Checks the need for compilation.
		All reasons for compilation are based on checking of file called "last_run_parameters.txt".
		We need to compile if:
		1) there is no executable file
		2) there is no such file ("last_run_parameters.txt" does not exist), so we can suppose it is first run
		3) the name of the file to load changed in string: "loadFile(...)"
		4) the name of the class changed in string: "simulate(class_name, ...)"
		5) values or amount of parameters for solver changed in string: "simulate(class_name, solver_params)"
		"""
		recompile_flag = False
		if sys.platform.startswith('win'):
			exec_name = class_name + '.exe'
		elif sys.platform.startswith('linux'):
			exec_name = class_name
		else:
			logger.info("Can not determine type of your OS")
			return constants.ERROR_STATUS
		if not os.path.isfile(exec_name):
			# There is no any executable file, so we really need to compile
			print 'REASON 1: No executable file'
			return True
			return True
		if os.path.isfile(lrp_filename):
			try:
				lrp_file = open(lrp_filename, "r")
			except IOError:
				logger.error("Can not open \"" + lrp_filename + "\" for reading")
				return constants.ERROR_STATUS
		else:
			#print 'There is no file with last run parameters.'
			print 'REASON 2: First execution'
			return True
		for line in lrp_file:
			if line.startswith("loadFile("):
				# line.split('"')[1] is the name of file to load
				if line.split('"')[1] != mo_filename:
					recompile_flag = True
					print "REASON 2: model's name changed"
					break
			if line.startswith("simulate("):
				model_name = re.search('\(\w+\,', line).group(0)[1:-1]
				if model_name != class_name:
					recompile_flag = True
					print "REASON 3: class name changed"
					break
				lrp_params_dict = self.params_dict_by_string(line)
				if isinstance(solver_params, basestring):
					solver_params = self.params_dict_by_string(solver_params)
				elif isinstance(solver_params, dict):
					solver_params = self.dict_with_str_values(solver_params)
				if not self.compare_params_dicts(lrp_params_dict, solver_params):
					recompile_flag = True
					print "REASON 4: solver params changed"
					break
		return recompile_flag

	def omp_check(self, log_list):
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
