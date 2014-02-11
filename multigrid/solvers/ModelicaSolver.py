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

import re # для использования регулярных выражений
import subprocess # для вызова скриптов командных строк
import os # для навигации по каталогам
import sys # для определения типа операционной системы
import hashlib # для чтения хэша файла

import Constants
import Launcher
import debug


class ModelicaSolver(Launcher.Launcher):
	name = "ModelicaDynamic"

	def __init__(self):
		self.MOS_filename = 'script.mos' # Host will use this name to create its own MOS file
		self.logger = debug.logger

	# preparing of data for calculation
	# writes dictionary in Loadcase variable inData
	# keys are mos and mo filenames; values are lists of the file strings
	def load_data(self, lc):
		files_dict = dict() #files dictionary, where keys are filenames and values are list of file strings
		with open(lc.scheme, 'r') as f:
			mos = f.readlines()
		files_dict[self.MOS_filename] = mos
		files_dict.update(self.CreateMOfilesDict(lc.scheme))
		lc.inData = files_dict

	# Создание файлов *.mo и *.mos в папке с именем расчетного случая Loadcase.Name.
	# Получение exe-файла с их помощью
	def compile(self, MOS_filename):
		if sys.platform.startswith('win'):
			command = '%OPENMODELICAHOME%/bin/omc.exe ' + MOS_filename
			self.logger.info("Begin compiling")
			subprocess.call(["cmd", "/C", command])#, startupinfo=startupinfo)
			self.logger.info("End compiling")
		elif sys.platform.startswith('linux'):
			self.logger.info("Begin compiling")
			subprocess.call(["omc", MOS_filename])
			self.logger.info("End compiling")
		else:
			self.logger.info("Can't determine platform")
			return Constants.ERROR_STATUS

	def run(self, loadcase, input_params):
		cwd = os.getcwd()
		#if not os.path.exists(id): os.makedirs(id)
		#os.chdir(id)
		if not os.path.exists(loadcase.name): os.makedirs(loadcase.name)
		os.chdir(loadcase.name)

		# Host creates all required files
		for k, v in loadcase.inData.iteritems():
			self.CreateFileFromList(v, k)

		class_name = self.GetClassName(self.MOS_filename)
		''' something for checking file's checksum
		if sys.platform.startswith('win'):
			# Проверка, существует ли уже exe-файл модели или нет
			if (os.path.isfile(class_name + '.exe')):
				pass
			else:
				self.Compile(self.MOS_filename) # получение exe-файла по mos-файлу
				hash = self.hashFile(class_name + '.exe', hashlib.sha256())
				with open(class_name + '.txt', 'w') as h:
					h.write(hash)
		elif sys.platform.startswith('linux'):
			if (os.path.isfile(class_name)):
				pass
			else:
				self.Compile(self.MOS_filename) # получение exe-файла по mos-файлу
				hash = self.hashFile(class_name + '.exe', hashlib.sha256())
				with open(class_name + '.txt', 'w') as h:
					h.write(hash)
		else:
			print 'can not determine your platform'
			return Constants.TASK_ERROR
		'''

		PAR_filename = 'pl.txt'
		RES_filename = 'results.plt'

		# создание файлов входных параметров по словарям входных параметров
		self.CreateParFilesFromParDicts(PAR_filename, input_params)

		if sys.platform.startswith('win'):
			if (os.path.isfile(class_name + '.exe')):
				pass
			else:
				self.compile(self.MOS_filename) # получение exe-файла по mos-файлу
			command = class_name + '.exe -overrideFile ' + PAR_filename + ' -r ' + RES_filename
			self.logger.info("Begin executing")
			subprocess.call(["cmd", "/C", command])#, startupinfo=startupinfo)
			self.logger.info("End executing")

		elif sys.platform.startswith('linux'):
			if (os.path.isfile(class_name)):
				pass
			else:
				self.compile(self.MOS_filename) # получение exe-файла по mos-файлу
			command = ['-overrideFile'] + [PAR_filename] + ['-r'] + [RES_filename]
			self.logger.info("Begin executing")
			subprocess.call(["./" + class_name] + command)
			self.logger.info("End executing")

		else:
			self.logger.info("Can't determine platform")
			return Constants.ERROR_STATUS

		# получение словаря выходных параметров
		result = self.CreateResultsDict(RES_filename)
		loadcase.status = Constants.SUCCESS_STATUS

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

	# Возвращает имя класса, прочитанное из mos-файла (simulate(className, ...))
	# Необходимо для получения кода модели на языке C, его компиляции и запуска
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

	# Returns a dictionary, where keys are mo filenames and values are list of mo file strings
	# dictionary is created using mos file located at MOS_file_path
	def CreateMOfilesDict(self, MOS_file_path):
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

	# Создает файл с названием filename по списку строк stringList
	# Пример содержания переменной stringList: ['loadModel(Modelica);\n', 'getErrorString();\n', ...]
	def CreateFileFromList(self, stringList, filename):
		# Создание файла
		with open(filename, 'w') as f:
			for line in stringList:
				f.write(line)

	# Генерация файлов входных параметров по словарям входных параметров ma1, ma2, ...
	def CreateParFilesFromParDicts(self, par_filename, par_dic):
		with open(par_filename, 'w') as PAR_file:
			for k, v in par_dic.iteritems():
				PAR_file.write(k + '=' + str(v) + '\n')

	# Создание словаря результатов по файлу результатов RES_filename
	# для входных параметров parameters
	# RES_filename - имя файла результатов
	def CreateResultsDict(self, RES_filename):
		curvesNumber = 0 #количество выходных переменных
		result_dict = dict() #словарь результатов
		value_list = list() #список значений для текущего выходного параметра
		print os.getcwd()

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
				tmp = list(value_list[:-1]) #убрали последний элемент,
				#т.к. value_list[последний] = value_list[последний-1]
				result_dict[key] = tmp
				del value_list[:] #очистить содержимое всего списка

		#MA_object.SetLayer(len(tmp))
		return result_dict

	def GetLog(self):
		pass
