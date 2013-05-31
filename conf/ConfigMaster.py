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

# класс конфигурации мастер-узла

import Pyro4.util
import Pyro4
import sys

MASTER_IP_ADDRESS = 'localhost'
PORT = 9000

class ConfigMaster:
	# инициализация объекта
	def __init__(self):
		sys.excepthook=Pyro4.util.excepthook
		Pyro4.config.DETAILED_TRACEBACK = False
		Pyro4.config.COMPRESSION = False
		Pyro4.config.ONEWAY_THREADED = False
		Pyro4.config.HMAC_KEY = None
		Pyro4.config.HOST = MASTER_IP_ADDRESS

