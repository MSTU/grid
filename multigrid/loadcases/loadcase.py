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
import constants

class Loadcase:
	"""
	Base class for calculation case specification. It's environment in which task will calculated
	"""
	def __init__(self, scheme, solver, desc=constants.DEFAULT_LOADCASE):
		self.scheme = scheme
		self.name = desc
		self.solver = solver
		self.status = constants.DEFAULT_STATUS