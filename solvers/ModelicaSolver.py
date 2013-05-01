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
import subprocess # для вызова скриптов командной строки Windows
import os # для
import Constants
import solvers.Launcher as Launcher


class ModelicaSolver(Launcher.Launcher):
	# инициализация объекта
	def __init__(self):
		self.name = "ModelicaDynamic"

	# подговка данных к расчету
	def LoadData(self, lc):
		return 0

	# Создание файлов *.mo и *.mos в папке с именем расчетного случая Loadcase.Name.
	# Получение exe-файла с их помощью
	def Compile(self, MOSfile, MOfile):

		MO_filename = self.GetMOfilename(MOSfile)
		MOS_filename = MO_filename + 's'

		# Создание файлов *.mo и *.mos
		self.CreateFileFromStringList(MOSfile, MOS_filename, 'mos')
		self.CreateFileFromStringList(MOfile, MO_filename, 'mo')

		command = '%OPENMODELICAHOME%/bin/omc.exe ' + MOS_filename
		#startupinfo = subprocess.STARTUPINFO()
		#startupinfo.dwFlags = subprocess.STARTF_USESHOWWINDOW
		print 'compiling...'
		subprocess.call(["cmd", "/C", command])#, startupinfo=startupinfo)
		print 'compiled'

	# запуск расчета схемы и инициализация ее параметрами
	# scheme - путь к файлу задачи (mos, mo, py, sch)
	# словарь параметров и их значений
	def Run(self, loadcase, parameters):
		scheme = loadcase.Scheme
		dir_name = loadcase.Name
		#dir_path = dir_name + '/'
		if not os.path.exists(dir_name): os.makedirs(dir_name)

		MOS = open(scheme, 'r')
		MOS_file = MOS.readlines()
		MOS.close()

		model_name = self.GetModelName(MOS_file)
		MO_filename = self.GetMOfilename(MOS_file)

		MO_filepath = scheme.rpartition('/')[0] + '/' + MO_filename

		MO = open(MO_filepath, 'r')
		MO_file = MO.readlines()
		MO.close()

		cwd = os.getcwd()
		os.chdir(dir_name)
		# Проверка, существует ли уже exe-файл модели или нет
		if (os.path.isfile(model_name + '.exe')):
			pass
		else:
			self.Compile(MOS_file, MO_file) # получение exe-файла по mos-файлу		

		PAR_filename = 'pl.txt'
		RES_filename = 'results.plt'

		# создание файлов входных параметров по словарям входных параметров
		self.CreateParFilesFromParDicts(PAR_filename, parameters.GetParameters())

		command = model_name + '.exe -overrideFile ' + PAR_filename + ' -r ' + RES_filename
		#startupinfo = subprocess.STARTUPINFO()
		#startupinfo.dwFlags = subprocess.STARTF_USESHOWWINDOW
		print 'executing'
		subprocess.call(["cmd", "/C", command])#, startupinfo=startupinfo)
		print 'executed'

		# получение словаря выходных параметров
		self.CreateResultsDict(RES_filename, parameters)
		print parameters.GetResults()

		os.chdir(cwd)
		return Constants.TASK_SUCCESS

	# Возвращает имя модели, прочитанное из mos-файла (simulate(model_name))
	# simulate(model_name, ...)
	def GetModelName(self, MOS_file):
		for line in MOS_file:
			if (not line.startswith('simulate')):
				pass
			else:
				model_name = re.split('[(,]', line)[1]
				return model_name

	# Возвращает имя mo-файла, прочитанное в mos-файле (loadFile("mo_filename"))
	def GetMOfilename(self, MOS_file):
		for line in MOS_file:
			if (not line.startswith('loadFile')):
				pass
			else:
				MO_filename = re.split('"', line)[1]

		return MO_filename


	# Создает файл с названием filename формата format по списку строк stringList
	# Пример содержания переменной stringList: ['loadModel(Modelica);\n', 'getErrorString();\n', ...]
	def CreateFileFromStringList(self, stringList, filename, format):
		# Создание файла
		f = open(filename, 'w+')
		for line in stringList:
			f.write(line)
		f.close()

	# Генерация файлов входных параметров по словарям входных параметров ma1, ma2, ...
	def CreateParFilesFromParDicts(self, par_filename, par_dic):

		filename = par_filename

		PAR_file = open(filename, 'w+')
		for k, v in par_dic.iteritems():
			PAR_file.write(k + '=' + str(v) + '\n')
		PAR_file.close()

	# Создание словаря результатов по файлу результатов RES_filename
	# для входных параметров parameters
	# RES_filename - имя файла результатов	
	def CreateResultsDict(self, RES_filename, parameters):
		layers = 0 # количество временных слоев
		curvesNumber = 0 #количество выходных переменных
		result_dict = dict() #словарь результатов
		value_list = list() #список значений для текущего выходного параметра

		f = open(RES_filename, 'r')
		for line in f:
			if (not line.startswith('DataSet: ')):
				continue
			curvesNumber += 1
			key = re.split('DataSet: ', line)[1][:-1]
			for line in f:
				if (line != '\n'):
					layers += 1
					parameters.SetLayer(layers)
					value_list.append(float(re.split('[\d.e-], ', line)[1][:-1]))
				else:
					break
			tmp = list(value_list[1:-1]) #убрали первый и последний элементы,
			#т.к. value_list[первый] = value_list[первый+1],
			#а value_list[последний] = value_list[последний-1]
			result_dict[key] = tmp
			del value_list[:] #очистить содержимое всего списка
		f.close()

		parameters.SetResults(result_dict)
		parameters.SetStatus(Constants.TASK_SUCCESS)

	def GetLog(self):
		pass
