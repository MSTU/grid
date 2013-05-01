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

import solvers.Launcher as Launcher
import Monitor

# Python решатель. Расчет функции на Python 

class PythonSolver(Launcher.Launcher):
	# инициализация объекта
	def __init__(self):
		self.name = "Python"
		#		self.value = None
		self.monitor = Monitor.Monitor("host.log")

	# подговка данных к расчету 
	def LoadData(self, lc):

		lc.inData = lc.Scheme

		return 0


	def Init(self):
		pass

	# запуск расчета схемы и инициализация ее параметрами
	def Run(self, lc, ma):

		if callable(lc.Scheme):
			value = lc.Scheme(ma)

			res = dict()
			res[lc.Name] = [value]
			ma.AddResults(res)

			lc.Status = 0
		else:
			lc.Status = -1

			lc.log = self.GetLog()
		return lc.Status


	# получить статус задачи (решается, решена нормально, ошибка)
	def Status(self):
		return 0

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
		return ""
	
