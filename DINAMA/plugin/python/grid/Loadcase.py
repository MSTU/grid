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
import cloudpickle

import Constants
# ����� ��� �������� ���������� ������

class Loadcase:
	def __init__(self, nl, pl, desc = Constants.DEFAULT_LOADCASE):
		scheme_name = pl[0]
		result_name = pl[1]
		self.functions_list = [cloudpickle.dumps(func) for func in pl[2]]
		self.criteria_list = pl[3]   # ������ ���������, �������� �� ����������� (�.�. ������, ����� �������� ��� ��������)
		solver = pl[4]

		self.Name = desc        # ��� ���������� ������
		self.Scheme = scheme_name    # ��� ����� (�.�. ������, ����� ��������� ����� �������� �� ����� �����������)
		self.ResultFile = result_name    # ��� ����� ����������� (�.�. ������, ����� �� ���������)
#		self.vl = criteria_list                # ������ ���������, �������� �� ����������� (�.�. ������, ����� �������� ��� ��������)

		self.Solver = solver            # �������� ��������

		self.SolverParameters = []
		self.OpenSign = pl[5]
		self.CloseSign = pl[6]
		self.inData = None
		self.status = 0
		self.log = ""
