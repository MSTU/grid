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

# ����� ��� �������� ���������� ������

class Loadcase:
	def __init__(self, nl, pl, desc = "grid_Loadcase"):
		scheme_name = pl[0]
		result_name = pl[1]
		criteria_list = pl[2]
		solver = pl[3]

		self.Name = desc        # ��� ���������� ������
		self.Scheme = scheme_name    # ��� ����� (�.�. ������, ����� ��������� ����� �������� �� ����� �����������)
		self.ResultFile = result_name    # ��� ����� ����������� (�.�. ������, ����� �� ���������)
		vl = criteria_list                # ������ ���������, �������� �� ����������� (�.�. ������, ����� �������� ��� ��������)

		self.Solver = solver            # �������� ��������

		self.SolverParameters = []
		#		self.OpenSign = pl[4]
		#		self.CloseSign = pl[5]
		self.inData = None
		self.status = 0
		self.log = ""
