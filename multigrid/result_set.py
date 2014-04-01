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

# ����� ���������� � ����������� ������

class ResultSet:
	# ������������� �������
	def __init__(self):
		self.result = []  # ������� ������� ����������
		self.status = 0

	#		self.layer = -1

	# �������� �������� ������� �� ������ ����
	def get_value(self, layer=-1):
		if (layer >= len(self.result)):
			return self.result[-1]
		return self.result[layer]

	# �������� �������� ������� �� ������ ����
	def get_value_list(self):
		return self.result

	# �������� ����� ��������� �����
	def get_layer_count(self):
		len(self.result)

	def get_status(self):
		return self.status

	def set_status(self, status):
		self.status = status
	