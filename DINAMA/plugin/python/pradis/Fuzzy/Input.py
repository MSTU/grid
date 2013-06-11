# -*- coding: cp1251 -*-

import constants as constants
#from misc import *
#import Solver
from fuzzy.InputVariable import InputVariable
#from fuzzy.OutputVariable import OutputVariable
#from fuzzy.Adjective import Adjective
from  pradis.Fuzzy.Fuzzify import Fuzzify 

from pradis.Fuzzy.System import System as System
# объект импорта файла 

class Input :# (ParameterValues):

	def __init__ (self, nl, pl, desc=constants.default):
		
		self.Name = pl[0] 
		self.Description = pl[1]
		self.Range = pl[2]
		self.Unit = pl[3]
		self.Fuzzify = pl[4]
		self.AdjectivesList = pl[5]
		
		(min, max) = self.Range
		ff = Fuzzify.choice (self.Fuzzify)
		self.variable = InputVariable(fuzzify=ff, description = self.Description, min=min, max=max, unit=self.Unit)	
		
		for i in self.AdjectivesList:
			self.variable.adjectives[i.Name] = i.adjective
		
#		print System()
		System().system.variables[self.Name] = self.variable
#		solver = Solver.getSolver()
#		solver.addObject (self)
		
			
			



