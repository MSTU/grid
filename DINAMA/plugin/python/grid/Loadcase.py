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
# класс для описания расчетного случая

class Loadcase:
	def __init__(self, nl, pl, desc = Constants.DEFAULT_LOADCASE):
		scheme_name = pl[0]
		result_name = pl[1]
		self.functions_list = [cloudpickle.dumps(func) for func in pl[2]]
		self.criteria_list = pl[3]   # список критериев, читаемых из результатов (м.б. пустым, тогда читаются все критерии)
		solver = pl[4]

		self.Name = desc        # имя расчетного случая
		self.Scheme = scheme_name    # имя схемы (м.б. пустым, тогда результат сразу читается из файла результатов)
		self.ResultFile = result_name    # имя файла результатов (м.б. пустым, тогда по умолчанию)
#		self.vl = criteria_list                # список критериев, читаемых из результатов (м.б. пустым, тогда читаются все критерии)

		self.Solver = solver            # название решателя

		self.SolverParameters = []
		self.OpenSign = pl[5]
		self.CloseSign = pl[6]
		self.inData = None
		self.status = 0
		self.log = ""
