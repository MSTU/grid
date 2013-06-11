import af
from OutValue import *

class Node (af.Node):

	def V (self):
		ov = OutValue()
		ov.type = 2
		ov.node = self
		return ov

	def A (self):
		ov = OutValue()
		ov.type = 3
		ov.node = self
		return ov
	
