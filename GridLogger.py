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

import logging
import random


class GridLogger:

	filename = "log.txt"
	defaultlvl = logging.INFO

	def __init__(self, filename):
		self.filename = filename

		self.logger = logging.getLogger("Grid")
		self.logger.setLevel(logging.INFO)

		handler = logging.FileHandler(filename + ".txt")
		handler.setLevel(logging.INFO)

		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

		handler.setFormatter(formatter)

		self.logger.addHandler(handler)

	def Log(self, lvl, message):
		self.logger.log(lvl, message)