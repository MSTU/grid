import multi
import af
import glb
import misc
import os

class Convolution:

	def __init__ (self, nl, pl, desc=misc.default):

		self.Name = pl[0]
		self.Method = pl[1]
		self.Criteria = pl[2]
		self.Weights = pl[3]
#		self.Type = pl[3]	

	def value(self, x, ma):
			i = 0
			v = 0.0
			for func in self.Criteria:
				if (i>=self.Weights.length()):
					w = self.Weights[i]
				else:
					w = 1.0

				if (self.Method == 'additive'):
					v = v + w*func(x,ma)
				elif (self.Method == 'multiplicative'):
					if (w>0):
						v = v * w*func(x,ma)
					elif(w<0):
						vt = func(x,ma)
						if (vt!=0.0):
							v = v/abs(w)/vt
				elif (self.Method == 'min'):
					v = 