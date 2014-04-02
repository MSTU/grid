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
from multigrid import constants

import launcher
from multigrid.loadcase import Loadcase


class PradisLoadcase(Loadcase):
	"""
	Loadcase for PradisSolver.
	"""

	def __init__(self, scheme, result_file, criteria_list, solver_params, open_sign, close_sign,
				 desc=constants.DEFAULT_LOADCASE):
		Loadcase.__init__(self, scheme, PRADISSolver.name, desc)

		self.result_file = result_file
		self.criteria_list = criteria_list
		self.solver_params = solver_params
		self.open_sign = open_sign
		self.close_sign = close_sign


class PRADISSolver(launcher.Launcher):
	name = "PRADISDynamic"

	def __init__(self):
		pass


	# запуск расчеты схемы (с установленнымм параметрами)
	def run(self, scheme):
		pass

	# запуск расчета схемы и инициализация ее параметрами
	def RunW(self, scheme, parameters):
		pass

	# получить статус задачи (решается, решена нормально, ошибка)
	def Status(self):
		pass

	# получить значение функции
	def GetValue(self, functionName):
		pass

	# установить временной слой
	def SetLayer(self, layer):
		pass

	# получить число временных слоев
	def GetLayerCount(self):
		pass

	# получить словарь пар функция-значение
	def GetFunctionsDict(self):
		pass


	def GetLog(self):
		pass
	
