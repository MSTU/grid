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

import re # ��� ������������� ���������� ���������
import subprocess # ��� ������ �������� ��������� ������ Windows
import os # ���
import Constants
import solvers.Launcher as Launcher


class ModelicaSolver(Launcher.Launcher):
	# ������������� �������
	def __init__(self):
		self.name = "ModelicaDynamic"

	# �������� ������ � �������
	def LoadData(self, lc):
		return 0

	# �������� ������ *.mo � *.mos � ����� � ������ ���������� ������ Loadcase.Name.
	# ��������� exe-����� � �� �������
	def Compile(self, MOSfile, MOfile):

		MO_filename = self.GetMOfilename(MOSfile)
		MOS_filename = MO_filename + 's'

		# �������� ������ *.mo � *.mos
		self.CreateFileFromStringList(MOSfile, MOS_filename, 'mos')
		self.CreateFileFromStringList(MOfile, MO_filename, 'mo')

		command = '%OPENMODELICAHOME%/bin/omc.exe ' + MOS_filename
		#startupinfo = subprocess.STARTUPINFO()
		#startupinfo.dwFlags = subprocess.STARTF_USESHOWWINDOW
		print 'compiling...'
		subprocess.call(["cmd", "/C", command])#, startupinfo=startupinfo)
		print 'compiled'

	# ������ ������� ����� � ������������� �� �����������
	# scheme - ���� � ����� ������ (mos, mo, py, sch)
	# ������� ���������� � �� ��������
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
		# ��������, ���������� �� ��� exe-���� ������ ��� ���
		if (os.path.isfile(model_name + '.exe')):
			pass
		else:
			self.Compile(MOS_file, MO_file) # ��������� exe-����� �� mos-�����		

		PAR_filename = 'pl.txt'
		RES_filename = 'results.plt'

		# �������� ������ ������� ���������� �� �������� ������� ����������
		self.CreateParFilesFromParDicts(PAR_filename, parameters.GetParameters())

		command = model_name + '.exe -overrideFile ' + PAR_filename + ' -r ' + RES_filename
		#startupinfo = subprocess.STARTUPINFO()
		#startupinfo.dwFlags = subprocess.STARTF_USESHOWWINDOW
		print 'executing'
		subprocess.call(["cmd", "/C", command])#, startupinfo=startupinfo)
		print 'executed'

		# ��������� ������� �������� ����������
		self.CreateResultsDict(RES_filename, parameters)
		print parameters.GetResults()

		os.chdir(cwd)
		return Constants.TASK_SUCCESS

	# ���������� ��� ������, ����������� �� mos-����� (simulate(model_name))
	# simulate(model_name, ...)
	def GetModelName(self, MOS_file):
		for line in MOS_file:
			if (not line.startswith('simulate')):
				pass
			else:
				model_name = re.split('[(,]', line)[1]
				return model_name

	# ���������� ��� mo-�����, ����������� � mos-����� (loadFile("mo_filename"))
	def GetMOfilename(self, MOS_file):
		for line in MOS_file:
			if (not line.startswith('loadFile')):
				pass
			else:
				MO_filename = re.split('"', line)[1]

		return MO_filename


	# ������� ���� � ��������� filename ������� format �� ������ ����� stringList
	# ������ ���������� ���������� stringList: ['loadModel(Modelica);\n', 'getErrorString();\n', ...]
	def CreateFileFromStringList(self, stringList, filename, format):
		# �������� �����
		f = open(filename, 'w+')
		for line in stringList:
			f.write(line)
		f.close()

	# ��������� ������ ������� ���������� �� �������� ������� ���������� ma1, ma2, ...
	def CreateParFilesFromParDicts(self, par_filename, par_dic):

		filename = par_filename

		PAR_file = open(filename, 'w+')
		for k, v in par_dic.iteritems():
			PAR_file.write(k + '=' + str(v) + '\n')
		PAR_file.close()

	# �������� ������� ����������� �� ����� ����������� RES_filename
	# ��� ������� ���������� parameters
	# RES_filename - ��� ����� �����������	
	def CreateResultsDict(self, RES_filename, parameters):
		layers = 0 # ���������� ��������� �����
		curvesNumber = 0 #���������� �������� ����������
		result_dict = dict() #������� �����������
		value_list = list() #������ �������� ��� �������� ��������� ���������

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
			tmp = list(value_list[1:-1]) #������ ������ � ��������� ��������,
			#�.�. value_list[������] = value_list[������+1],
			#� value_list[���������] = value_list[���������-1]
			result_dict[key] = tmp
			del value_list[:] #�������� ���������� ����� ������
		f.close()

		parameters.SetResults(result_dict)
		parameters.SetStatus(Constants.TASK_SUCCESS)

	def GetLog(self):
		pass
