import af
import glb
from misc import *
from ParameterValues import *

# объект простой модели ДВС

class SimpleICE:# (ParameterValues):

	def __init__ (self, nl, pl, desc= misc.default):
		
		self.values = pl
		
		self.F  = pl[0]
		self.T  = pl[1]
		self.m  = pl[2]
		self.J  = pl[3]
		self.Cg  = pl[4]
		self.Oz  = pl[5]
		self.xz  = pl[6]
		
	def Values(self):
		return self.values		
			



