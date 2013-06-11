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
from Host import Host
from Master import Master


class LocalMaster(Master):
	# ������������� �������
	def __init__(self, config=None):
		Master.__init__(self)
		self.ready_tasks = []
		self.host = Host()

	#������ �������� � �������
	def RunTask(self, task):
		self.ready_tasks.append(self.host.RunTask(task))

	#���� ��������� ���� ����� ������� � ������� � ���������� ��� �������� ������
	def Wait(self, clientId):
		return self.ready_tasks

