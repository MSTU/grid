# -*- coding: cp1251 -*-

from pradis.Fuzzy.System  import System as System
import constants as constants
import pradis.Fuzzy.System
from fuzzy.Adjective import Adjective
# объект импорта файла 

class Parameter :# (ParameterValues):

	def __init__ (self, nl, pl, desc=constants.default):
		
		self.Name = pl[0] 
		self.Description = pl[1]
		self.Value = pl[2]
		self.Adjective = pl[3]
		self.fuzzy_flag = False
		self.desc = desc
		
		if self.Value == None and self.Adjective<>None:
			self.fuzzy_flag = True
			"""
			self.Value = dict()
			if isinstance(self.Adjective, Adjective):
				self.Value[self.Adjective.Name] = self.Adjective.adjective
			else: #if isinstence(self.Adjective, fuzzy.operate.operate):
				set = pradis.Fuzzy.System.operate(self.Adjective)
#				set = Set.choice (self.Set, self.Values)
				sys = System().system
				variable = sys.variables[self.Name]
		
				adjective = Adjective (set)	
				name = self.Name+'.'+desc
				variable.adjectives[name] = adjective
				self.Value[name] = adjective
			"""
		
#		self.variable = {self.Name:self.Value}
		
		
			
			



