# ***************************************************************************
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
from multigrid import constants
from solvers.solversloadcase import SolversLoadcase


class AnsysLoadcase(SolversLoadcase):
	"""
	Loadcase for ANSYS solvers.

	scheme: string
		Path to input file
	desc: string
		Loadcase name (this is the name of the directory, where all files will be saved)
	criteria_list: list
		List of result parameters, which will be included in result dict
	solver_params : string
		String of options which will pass to ANSYS solvers.
		Example of string of options for ANSYS CFX Solver:
		"-v -output-summary-option 0 -save -name CFX_solution"

	"""
	def __init__(self, scheme, solver, desc=constants.DEFAULT_LOADCASE, criteria_list=None, solver_params=None, need_filetransfer=False):
		SolversLoadcase.__init__(self, scheme, solver, desc, criteria_list, solver_params, need_filetransfer)
