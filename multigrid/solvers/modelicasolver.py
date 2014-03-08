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

import re # for using regular expressions
import subprocess # for execution of command prompt scripts
import os # for navigation through catalogs
import ntpath

import sys # to define OS type
from solvers.common_methods import create_file
import constants
import launcher
import debug
from loadcase import Loadcase
from solversloadcase import SolversLoadcase


#MOS_filename = 'script.mos' # Host will use this name to create its own MOS file
name = "ModelicaDynamic"

logger = debug.logger

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
		# files_dict.update(CreateMOfilesDict(self.scheme))
		self.inData = mo


# Returns a dictionary, where keys are mo filenames and values are list of mo file strings
# dictionary is created using mos file located at MOS_file_path
def CreateMOfilesDict(MOS_file_path):
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
			result += key + ' = ' + str(value)
			result += ', '
		# delete last comma and space
		result = result[:-2]
	else:
		result = params
	return result

def create_mos_by_mo(mo_file, simulate_params):
	mos_file = []
	mos_file.append('loadModel(Modelica);\n')
	mos_file.append('getErrorString();\n')
	mos_file.append('loadFile("' + mo_file + '");\n')
	mos_file.append('getErrorString();\n')
	mos_file.append('simulate(dcmotor, ' + generate_params_string(simulate_params) + ', outputFormat = "plt");\n')
	mos_file.append('getErrorString();\n')
	return mos_file


class ModelicaSolver(launcher.Launcher):
	# compiles *.mo file using *.mos file to get exe-file of the model
	def compile(self, MOS_filename):
		if sys.platform.startswith('win'):
			command = '%OPENMODELICAHOME%/bin/omc.exe ' + MOS_filename
			logger.info("Begin compiling")
			subprocess.call(["cmd", "/C", command])#, startupinfo=startupinfo)
			logger.info("End compiling")
		elif sys.platform.startswith('linux'):
			logger.info("Begin compiling")
			subprocess.call(["omc", MOS_filename])
			logger.info("End compiling")
		else:
			logger.info("Can't determine platform")
			return constants.ERROR_STATUS

	def run(self, loadcase, input_params):
		cwd = os.getcwd()
		#if not os.path.exists(id): os.makedirs(id)
		#os.chdir(id)
		if not os.path.exists(loadcase.name):
			os.makedirs(loadcase.name)
		os.chdir(loadcase.name)

		# Host creates all required files
		# for k, v in loadcase.inData.iteritems():
		# 	create_file_from_list(v, k)

		mo_filename = ntpath.basename(loadcase.scheme)
		MOS_filename = mo_filename[:-3] + generate_params_string(loadcase.solver_params) + '.mos'
		create_file(loadcase.inData, mo_filename)
		create_file(create_mos_by_mo(mo_filename, loadcase.solver_params), MOS_filename)

		class_name = self.GetClassName(MOS_filename)
		''' something for checking file's checksum
		if sys.platform.startswith('win'):
			# ��������, ���������� �� ��� exe-���� ������ ��� ���
			if (os.path.isfile(class_name + '.exe')):
				pass
			else:
				self.Compile(self.MOS_filename) # ��������� exe-����� �� mos-�����
				hash = self.hashFile(class_name + '.exe', hashlib.sha256())
				with open(class_name + '.txt', 'w') as h:
					h.write(hash)
		elif sys.platform.startswith('linux'):
			if (os.path.isfile(class_name)):
				pass
			else:
				self.Compile(self.MOS_filename) # ��������� exe-����� �� mos-�����
				hash = self.hashFile(class_name + '.exe', hashlib.sha256())
				with open(class_name + '.txt', 'w') as h:
					h.write(hash)
		else:
			print 'can not determine your platform'
			return Constants.TASK_ERROR
		'''

		PAR_filename = 'pl.txt'
		RES_filename = 'results.plt'

		# create file with input parameters using dictionaries of input parameters
		self.CreateParFilesFromParDicts(PAR_filename, input_params)

		if sys.platform.startswith('win'):
			if (os.path.isfile(class_name + '.exe')):
				pass
			else:
				self.compile(MOS_filename) # getting exe-file using mo and mos files
			command = class_name + '.exe -overrideFile ' + PAR_filename + ' -r ' + RES_filename
			logger.info("Begin executing")
			subprocess.call(["cmd", "/C", command])#, startupinfo=startupinfo)
			logger.info("End executing")

		elif sys.platform.startswith('linux'):
			if (os.path.isfile(class_name)):
				pass
			else:
				self.compile(MOS_filename) # getting exe-file using mo and mos files
			command = ['-overrideFile'] + [PAR_filename] + ['-r'] + [RES_filename]
			logger.info("Begin executing")
			subprocess.call(["./" + class_name] + command)
			logger.info("End executing")

		else:
			logger.info("Can't determine platform")
			return constants.ERROR_STATUS

		# getting dictionary of output parameters
		result = self.CreateResultsDict(RES_filename)
		loadcase.status = constants.SUCCESS_STATUS

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

	# Returns class name readed from mos-file (at this string: (simulate(className, ...))
	# It's required for getting model's C code, its compilation and execution
	def GetClassName(self, MOS_filename):
		className = None
		with open(MOS_filename, 'r') as f:
			for line in f:
				if (not line.startswith('simulate')):
					pass
				else:
					className = re.split('[(,]', line)[1]

		return className

	# Returns file's checksum
	# filename - name of file; hasher - hash algorithm (md5, sha1, sha256, ...);
	# blocksize - the internal block size of the hash algorithm in bytes
	def hashFile(self, filename, hasher, blocksize=8192):
		with open(filename, 'rb') as f:
			buf = f.read(blocksize)
			while len(buf) > 0:
				hasher.update(buf)
				buf = f.read(blocksize)

		return hasher.hexdigest()


	# Creates files of input parameters using dictionaries of input parameters
	def CreateParFilesFromParDicts(self, par_filename, par_dic):
		with open(par_filename, 'w') as PAR_file:
			for k, v in par_dic.iteritems():
				PAR_file.write(k + '=' + str(v) + '\n')

	# Creates dictionary of results using result file named "RES_filename"
	def CreateResultsDict(self, RES_filename):
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

	def GetLog(self):
		pass
