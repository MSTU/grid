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
import pickle
import Constants
from Launcher import Launcher


class PythonSolver(Launcher):
	name = "Python"

	def Run(self, lc, input_params):
		try:
			func = pickle.loads(lc.scheme)
			result = func(input_params)

			status = Constants.SUCCESS_STATUS
		except:
			status = Constants.ERROR_STATUS

		lc.status = status
		return result
