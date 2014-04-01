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

# Лаунчер решателя. Базовый класс

class Launcher:
	# object's initialization
	def __init__(self):
		pass

	def load_data(self, lc):
		"""
		Prepares loadcase data
		"""
		return 0

	def init(self):
		pass

	def run(self, lc, input_params):
		"""
		Launching one loadcase. Takes loadcase and input parameters as input.
		Returns result of computation. Sets solution status of loadcase.
		"""
		pass

	def preexecute(self, lc):
		"""
		Execute before run
		"""
		pass