import af
from glb import root_list

class Range (af.Range):

	def __init__ (self, ovp, min, max):
		self.this = af.Range (root_list.Add())
		self.SetOutVariable (ovp)
		self.SetMin (min)
		self.SetMax (max)

