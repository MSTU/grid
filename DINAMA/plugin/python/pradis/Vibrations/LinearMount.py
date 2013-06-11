import af
import glb
from misc import *
from ParameterValues import *

# объект хар-к лиенйной опопры

class LinearMount:# (ParameterValues):

	def __init__ (self, nl, pl, desc= misc.default):
		
		self.values = pl
		
		self.location  = pl[0]
		self.Cx  = pl[1]
		self.Cy  = pl[2]
		self.Cz  = pl[3]

		
	def Values(self):
		return self.values		
			



