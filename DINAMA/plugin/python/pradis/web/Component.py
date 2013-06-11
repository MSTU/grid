# -*- coding: cp1251 -*-

from pradis.web.Model import *
from pradis.web.Parameter import *


class Component:

	def __init__(self, name, model):

		self.name = name
		self.model = model
		self.parameterList = dict()
		

#	set dynamic parameter		
	def set (self, name, value):
		self.parameterList[name] = value
	
#	get dynamic parameter
	def get (self, name):
		return self.parameterList[name] 

		
	def init(self):
		pass
	
	
	