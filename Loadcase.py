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

# класс для описания расчетного случая

class Loadcase:
	def __init__(self, nl, pl, desc = "grid_Loadcase"):
		scheme_name = pl[0]
		result_name = pl[1]
		criteria_list = pl[2]
		solver = pl[3]

		self.Name = desc        # имя расчетного случая
		self.Scheme = scheme_name    # имя схемы (м.б. пустым, тогда результат сразу читается из файла результатов)
		self.ResultFile = result_name    # имя файла результатов (м.б. пустым, тогда по умолчанию)
		vl = criteria_list                # список критериев, читаемых из результатов (м.б. пустым, тогда читаются все критерии)

		self.Solver = solver            # название решателя

		self.SolverParameters = []
		#		self.OpenSign = pl[4]
		#		self.CloseSign = pl[5]
		self.inData = None
		self.status = 0
		self.log = ""
