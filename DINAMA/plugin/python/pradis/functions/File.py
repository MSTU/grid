import af
import glb

import misc
from Data import *

class File(Data):

	def __init__ (self, nl, pl, desc=misc.default):
		self.Name = desc
		par = misc.Expand (pl)
		file = par[0]
		if file=="":
			return
		flag = 0
#		if length (par)>1:
#			flag = par[1]
		if flag==1:
			self.values = self.load(file)
			Data.__init__ (self, self.Name, self.values)
		else:
			Data.__init__ (self, self.Name, '\n$INCLUDE: '+file)

	def load(self, file):
# TODO:	
		return ''
		
	def Values(self):
		return self.values



