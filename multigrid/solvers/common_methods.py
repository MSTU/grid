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

# These are common methods used by most of the solvers
import debug

logger = debug.logger

def create_file_from_list(stringList, filename):
	"""
	Creates a file named "filename" using list of strings "stringList"

	"""
	try:
		f = open(filename, "w")
	except IOError:
		logger.error("Can not create file \"" + filename + "\"")
		return None
	for line in stringList:
		f.write(line)
	f.close()