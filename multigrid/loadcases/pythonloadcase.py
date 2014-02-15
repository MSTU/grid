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
from loadcase import Loadcase
from solvers.pythonsolver import PythonSolver
import cloudpickle

class PythonLoadcase(Loadcase):
	"""
	Loadcase for PythonSolver.
	"""
	def __init__(self, scheme, desc=constants.DEFAULT_LOADCASE):
		func_dump = cloudpickle.dumps(scheme)
		Loadcase.__init__(self, func_dump, PythonSolver.name, desc)