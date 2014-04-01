# -*- coding: cp1251 -*-

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
import pickle

import constants


class Task:
	def __init__(self, loadcases, input_params):
		self.id = None
		self.loadcases = loadcases
		self.input_params = pickle.dumps(input_params)
		self.result = dict()
		self.status = constants.DEFAULT_STATUS

	# task status is least loadcase status
	def recalc_status(self):
		for loadcase in self.loadcases:
			if self.status > loadcase.status:
				self.status = loadcase.status

	def __repr__(self):
		return "Task: loadcases = %r, status = %s " % (self.loadcases, self.status)