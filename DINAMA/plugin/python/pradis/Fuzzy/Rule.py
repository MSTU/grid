# -*- coding: cp1251 -*-

import constants as constants
#import Solver
from pradis.Fuzzy.System import System as System
import pradis.Fuzzy.Adjective
from fuzzy.Rule import Rule as fRule
from fuzzy.operator.Compound import Compound
from fuzzy.operator.Input import Input
from fuzzy.operator.Not import Not
from fuzzy.operator.Const import Const
from pradis.Fuzzy.Norm import Norm as Norm

from fuzzy.Adjective import Adjective
# объект импорта файла 

class Rule :# (ParameterValues):

	def __init__ (self, nl, pl, desc=constants.default):
		
		
		self.Name = pl[0] 
		self.ValueList = pl[1] 
		
		self.Norm = pl[2]
		self.Expressions = pl[3]

		self.Certainty = pl[4] 			
		self.CertaintyNorm = pl[5]
		
		norm = Norm.choice (self.Norm)
		cl = self.createCompound ( norm, self.Expressions)
		
		operator = cl#Compound (self.Norm, *cl)
#		print 'cl=',cl
		CertaintyNorm = Norm.choice(self.CertaintyNorm) #self.choiceOfNorm (self.CertaintyNorm)
		
		
		
		self.rules = []
		for i in self.ValueList:
#			var = System().system.variables['output_temperature'].adjectives [i.Name] 
#			print 'var = ', var
#			print 'i.adjective = ', i.adjective
			rule = fRule(adjective=i.adjective, operator=operator, certainty=self.Certainty, CER=CertaintyNorm)
#			rule = fRule(adjective=var, operator=operator, certainty=self.Certainty, CER=CertaintyNorm)
			self.rules.append(rule)
			System().system.rules[self.Name+'.'+i.Name] = rule
		
		
#		solver = Solver.getSolver()
#		solver.addObject (self)
		
	def createCompound (self, norm, expr):	
		
#		if isinstance (expr, Adjective):
#			return Compound ()
		comlist = []
		
#		print '1:', expr
		
		
		for i in expr:
#			print 'i=',i

			if isinstance (i, pradis.Fuzzy.Adjective.Adjective):
				#comlist.append ( fuzzy.operator.Input.Input(e.adjective)  )
#				print 'Adjective'
				comlist.append ( Input(i.adjective) )
#				print 1
			if isinstance (i, Compound):
				#comlist.append ( fuzzy.operator.Input.Input(e.adjective)  )
#				print 'Adjective'
				comlist.append ( i)
#				print 1
			elif type(i) == tuple: 
#				print 'tuple'
				(a,b) = i
				#comlist.append ( Compound (a, *self.createCompound(b)))
				if type(a) == fuzzy.operator.Not.Not:
					comlist.append ( fuzzy.operator.Not.Not (self.createCompound(None,b)))
				else:
					comlist.append ( self.createCompound(a,b))
#				print 2
#			elif type(i) == list:
#				cl = createCompound  (i)
#				comlist.append ( Compound (n, *cl))
			elif isinstance (i, float) or isinstance (i, int):
				#comlist.append (Const (i))
				comlist.append ( Const (i))
#				print 3
#			print 4
		if len (comlist)==1:
			return comlist [0]
		else:
			return Compound(norm, *comlist)
		
		return comlist


	def createListVars (self, expr):	
		
		comlist = []		
		
		for i in expr:
			if isinstance (i, Adjective):
				comlist.append ( fuzzy.operator.Input.Input(e.adjective)  )
			elif type(i) == tuple: 
#				print 'tuple'
				(a,b) = i
				comlist.append ( Compaund (a, *self.createCompound(b)))
			elif type(e) == list:
				cl = createListVars  (e)
				comlist.append ( Compound (n, *cl))
			elif isinstance (e, float) or isinstance (e, int):
				comlist.append (Compound(n, Const (e)))
#			elif type(e) == tuple: 
#				print 'tuple'
#				(a,b) = e
#				comlist.append ( self.createCompound(a, b))
		
		
#		print 2222222222
		return comlist

		
		
		
		