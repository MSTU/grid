# -*- coding: cp1251 -*-

from pradis.web.Parameter import *


class Model:

	def __init__(self, name):

		self.name = name
		self.parameterList = []
		

#	set dynamic parameter		
	def add_par (self, par):
		self.parameterList.append(par)
	
#	get dynamic parameter
	def getParameterList  (self):
		return self.parameterList
