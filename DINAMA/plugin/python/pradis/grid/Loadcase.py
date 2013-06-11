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

import constants
# класс для описания расчетного случая
from ParameterValues import *

import grid.Loadcase

class Loadcase (ParameterValues):
	def __init__(self, nl, pl, desc = constants.default):
	
		self.lc = grid.Loadcase.Loadcase (nl,pl,desc)
#		scheme_name = pl[0]
#		result_name = pl[1]
#		criteria_list = pl[2]
#		solver = pl[3]
	
	def Values (self):
		return self.lc