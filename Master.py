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
import conf.ConfigMaster as ConfigMaster
import GridLogger


class Master():
	# ������������� �������
	def __init__(self, config=None):
		if config is None:
			self.config = ConfigMaster.ConfigMaster()
		else:
			self.config = config
		self.logger = GridLogger.GridLogger("master")

	#������ �������� � �������
	def RunTask(self, task):
		pass

	#���� �������� ���� �����, ����� ���������������� ����
	def RegisterHost(self, host_uri):
		pass

	#���� ��������� ���� ����� ������� � ������� � ���������� ��� �������� ������
	def WaitAll(self, clientId):
		pass

	def Wait(self, clientId, taskId):
		pass

	def RunBalancer(self):
		pass

