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
import pickle
import Constants
import Launcher


class PythonSolver(Launcher.Launcher):
	name = "Python"

	def LoadData(self, lc):
		lc.inData = lc.scheme
		return 0

	def Init(self):
		pass

	# запуск расчета схемы и инициализация ее параметрами
	def Run(self, lc, task):
		try:
			func = pickle.loads(lc.scheme)
			value = func(task.input_params)

			task.result_params = value
			task.status = Constants.TASK_SUCCESS
		except:
			task.status = Constants.TASK_ERROR

		return task.status


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
	
