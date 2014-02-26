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
import sys
import os
import re
import debug

logger = debug.logger

# Determines ANSYS version
def get_ansys_version():
	if sys.platform.startswith('win'):
		pass
	elif sys.platform.startswith('linux'):
		if(os.path.isdir("/ansys_inc")):
			dir_list = os.listdir("/ansys_inc")
			for line in dir_list:
				temp = re.search("v[\d]+", line)
				if temp is not None:
					version = temp.group(0)[1:]
					return version
		else:
			logger.error("ERROR: Сan not locate your ANSYS installation directory")

	else:
		logger.error("ERROR: Сan not determine your platform")
		return ""