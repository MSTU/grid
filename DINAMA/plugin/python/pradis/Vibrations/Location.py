import af
import glb
from misc import *
from ParameterValues import *

# ������ ����������� �� ��������� ����

class Location:# (ParameterValues):

	def __init__ (self, nl, pl, desc= misc.default):
		
		self.values = pl

		self.gX  = pl[0]
		self.gY  = pl[1]
		self.gZ  = pl[2]
		
		
	def Values(self):
		return self.values		
			



