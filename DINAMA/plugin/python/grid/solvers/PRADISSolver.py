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

# Лаунчер решателя. Базовый класс

class PRADISSolver(Launcher):
	# инициализация объекта
	def __init__(self):
		self.name = "PRADISDynamic"


	# запуск расчеты схемы (с установленнымм параметрами)
	def Run(self, scheme):
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
	
