import misc
import random

class VariableLow:

	def __init__ (self, nl, pl, desc=misc.default):

		self.lowName = pl[0]
		self.a1 = pl[1]
		self.a2 = pl[2]
		
		self.gen = random.Random(0.0)
		

#		self.Type = pl[3]	

	def low (self, var):
	
		print 'var = ', var
		print 'low = ', self.lowName
		x = 0.0
		if self.lowName == 'constant':
			x = var.Value0
		elif self.lowName == 'uniform':
			a = self.a1 #var.Min
			b = self.a2 #var.Max
			x = self.gen.uniform (a,b)
			
#		print 'sample = ', x
		
		return x
		
	