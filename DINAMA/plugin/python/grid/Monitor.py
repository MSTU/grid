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

# Монитор сервера

class Monitor:
	def __init__(self):
		pass

	# возвращает список задач 
	def GetTaskList(self):
		pass

	# возвращает список хостов
	def GetHosts(self):
		pass

	# получить статус сервера
	def Status(self):
		pass

	# вовращает список событий
	def GetEventsList(self):
		pass