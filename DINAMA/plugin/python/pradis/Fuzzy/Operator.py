from misc import *
#import Solver

# объект импорта файла 

class Operator :# (ParameterValues):

	def __init__ (self, nl, pl, desc=misc.default):
		
		self.Norm = pl[0]
		self.Expressions = pl[1]

		self.Compound = self.createCompound (self.Norm, self.Expressions)
		
		
#		solver = Solver.getSolver()
#		solver.addObject (self)
		
	def createCompound (self, norm, expr):	
		
#		if isinstance (expr, Adjective):
#			return Compound ()
		comlist = []
		for i in expr:
			(n, e) = i
			if isinstance (e, Adjective):
				comlist.append (e.adjective)
			if isinstance (e, [float,int]):
				comlist.append (Const (e))
			if type(e) == tuple: 
				(a,b) = e
				comlist.append ( self.createCompound(a, b))
		
		c = Compound (self.choiceOfNorm (norm), comlist)
		
		return c

	def choiceOfNorm (self, Norm):	
		norm ['MIN'] = Min()
		norm ['MAX'] = Max()
		
		# TODO: другие типы множеств
		
		return norm[Norm]


