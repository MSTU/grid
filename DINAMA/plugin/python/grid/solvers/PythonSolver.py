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
import pickle

from grid.solvers.Launcher import Launcher

class PythonSolver(Launcher):
	def __init__(self):
		Launcher.__init__(self)
		self.name = "Python"

	# �������� ������ � ������� 
	def LoadData(self, lc):
		lc.inData = lc.Scheme
		return 0


	def Init(self):
		pass

	# ������ ������� ����� � ������������� �� �����������
	def Run(self, lc, ma):
		#if callable(lc.functions_list[0]):    #lc.Scheme):
		#	value = lc.functions_list[0](ma) #lc.Scheme(ma)    - ��� �������� Python ������� ������� � ���� functions_list

		#	res = dict()
		#	res[lc.Name] = [value]
		#	ma.AddResults(res)

		#	lc.Status = 0
		#else:
		#	lc.Status = -1

		#	lc.log = self.GetLog()
		#return lc.Status
		func = pickle.loads(lc.functions_list[0])
		value = func(ma)

		res = dict()
		res[lc.Name] = [value]
		ma.AddResults(res)

		lc.Status = 0
		return lc.Status



	# �������� ������ ������ (��������, ������ ���������, ������)
	def Status(self):
		return 0

	# �������� �������� �������
	def GetValue(self, functionName):
		pass

	# ���������� ��������� ����
	def SetLayer(self, layer):
		pass

	# �������� ����� ��������� �����
	def GetLayerCount(self):
		pass

	# �������� ������� ��� �������-��������
	def GetFunctionsDict(self):
		pass


	def GetLog(self):
		return ""
	
