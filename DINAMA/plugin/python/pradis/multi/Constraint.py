import multi
import af
import glb
import misc
import os

class Constraint:

	def __init__ (self, nl, pl, desc=misc.default):

		self.Name = pl[0]
		self.Method = pl[1]
		self.Argument1 = pl[2]
		self.Argument2 = pl[3]
#		self.Type = pl[3]	

	def value (self, x, ma):
		v = 0.0
		if (self.Method == '='):
			v = (self.Argument1(x,ma) - self.Argument2(x,ma))**2
		elif (self.Method == '>'):
			v = (self.Argument2(x,ma) - self.Argument1(x,ma))
		elif (self.Method == '<'):
			v = (self.Argument1(x,ma) - self.Argument2(x,ma))
		elif (self.Method == '<>'):
			v = (self.Argument2(x,ma) - self.Argument1(x,ma))
			if (v<1e-10):
				v = 1e10
			else:
				v = 1.0 / v
		
		return v
			