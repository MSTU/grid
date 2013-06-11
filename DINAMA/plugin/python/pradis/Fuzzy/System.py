# -*- coding: cp1251 -*-
#import multi
#import misc


# Singleton
import fuzzy.System

class System(object):
    system = fuzzy.System.System()		
    def __new__(cls):
        if not hasattr(cls, 'instance'):
             cls.instance = super(System, cls).__new__(cls)
        return cls.instance

#	def __init__ (self):
#		import fuzzy.System
#		self.system = fuzzy.System.System()		
		
#	def system (self):
#		return self.system

class helper(object):
	"""A helper class to hold a set and its plotitems together.
		It is used like an unnamed struct.
	"""
	def __init__(self,set):
		"""Set given values"""
		self.set = set
		
def define_const(value):
	"""Define a constant value with its plotitem. 
		Its just defines the constant value at the x-value 0 and 60."""
	return helper(value)

import fuzzy.set.Set
		
def operate(operator):
	
	from fuzzy.operator.Compound import Compound
	from fuzzy.operator.Input import Input
	from fuzzy.operator.Const import Const
	from fuzzy.operator.Not import Not
	from fuzzy.set.operations import norm,merge
	import pradis.Fuzzy.Adjective
	
	if operator == None:
		p = define_const(0.0)
	elif isinstance (operator, Compound ):
		
		if len (operator.inputs) == 2:
			a = operator.inputs[0] #inputs
			b = operator.inputs[1]
			x = operate(a)
			y = operate(b)
#			print x,y
			if isinstance(y.set,fuzzy.set.Set.Set):
				p = helper(merge(operator.norm, x.set, y.set,1.0))
			else: # for float
				p = helper(norm(operator.norm,x.set,y.set))

#			p = helper (merge(operator.norm, x.set, y.set,1.0))
			
#			print 'p1=',p
		else:
			a = operator.inputs[0]
			x = operate(a)
			for i in operator.inputs[1:]:
				y = operate(i)
				x = merge(operator.norm, x.set, y.set,1.0)
			p = helper(x)
	elif isinstance(operator, Input):
		p = operator.adjective
		
	elif isinstance(operator, pradis.Fuzzy.Adjective.Adjective):
		p = operator.adjective
	elif isinstance (operator, Const):
		p =  define_const(operator.value)
	elif isinstance (operator, Not):
		a = operator.input
		x = operate(a)
		
		from pradis.Fuzzy.norm_Not import norm_Not 
		p = helper(merge(norm_Not(), x.set, x.set, 1.0))
#		print 'p2=',p
		
	else:
		print 'operator=', operator
		a = operator.inputs[0]
		b = operator.inputs[1]
		x = operate(a)
		y = operate(b)
		
		if isinstance(y.set,fuzzy.set.Set.Set):
			p = helper(merge(operator.operatorNorm, x.set, y.set,1.0))
		else: # for float
			p = helper(norm(operator.operatorNorm,x.set,y.set))
		print 'p3=',p
	return p
		
		
			