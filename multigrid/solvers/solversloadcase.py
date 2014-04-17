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
from multigrid.loadcase import Loadcase
from multigrid.conf import configclient

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
	def __init__(self, scheme, solver, desc, is_filetransfer, transfer_params, criteria_list=None, solver_params=None):
		Loadcase.__init__(self, scheme, solver, desc)

		self.criteria_list = criteria_list
		self.solver_params = solver_params
		self.is_filetransfer = is_filetransfer
		self.transfer_params = transfer_params
		if self.is_filetransfer and not self.transfer_params:
			self.transfer_params = {'host': configclient.IP_ADDRESS}
