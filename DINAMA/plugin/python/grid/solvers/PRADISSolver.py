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

import Launcher

# ������� ��������. ������� �����

class PRADISSolver(Launcher):
	# ������������� �������
	def __init__(self):
		self.name = "PRADISDynamic"


	# ������ ������� ����� (� �������������� �����������)
	def Run(self, scheme):
		pass

	# ������ ������� ����� � ������������� �� �����������
	def RunW(self, scheme, parameters):
		pass

	# �������� ������ ������ (��������, ������ ���������, ������)
	def Status(self):
		pass

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
		pass
	
