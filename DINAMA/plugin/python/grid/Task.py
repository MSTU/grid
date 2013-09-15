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
class Task:
	# инициализация объекта
	def __init__(self, lc, ma):
		self.lc = lc    # список расчетных случаев
		self.ma = ma    # объект ModelAnalysis

	def GetLoadcase(self):
		return self.lc

	def SetLoadcase(self, lc):
		self.lc = lc

	def SetModelAnalysis(self, ma):
		self.ma = ma

	def GetModelAnalysis(self):
		return self.ma

	def SetClientId(self, clientId):
		self.clientId = clientId

	def DetClientId(self):
		return self.clientId

