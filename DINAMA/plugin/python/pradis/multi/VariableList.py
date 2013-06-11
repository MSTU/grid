# -*- coding: cp1251 -*-
import misc
from ParameterValues import *


class VariableList (ParameterValues):

	def __init__ (self, nl, pl, desc=misc.default):

		self.Vars = pl[0]
#		self.Type = pl[3]	

	def Values(self):
		return self.Vars		
