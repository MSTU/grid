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

class SolversLoadcase(Loadcase):
	"""
	Loadcase for solvers with execution parameters.

	scheme: string
		Path to input file
	desc: string
		Loadcase name (this is the name of the directory, where all files will be saved)
	criteria_list: list
		List of result parameters, which will be included in result dict
	solver_params : dictionary or string
		Dictionary or string of options which will pass to solvers.
	"""
	def __init__(self, scheme, solver, desc, need_filetransfer, criteria_list, solver_params):
		Loadcase.__init__(self, scheme, solver, desc, need_filetransfer)

		self.criteria_list = criteria_list
		self.solver_params = solver_params
