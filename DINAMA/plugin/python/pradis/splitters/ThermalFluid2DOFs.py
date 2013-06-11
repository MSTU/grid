import af
from glb import *
from Node import *
from DOF import *
from misc import *

class ThermalFluid2DOFs:

	def __init__(self, n1, n2, desc = misc.default):
		n1[1].x.Copy (n1[0], "p")
		n1[2].x.Copy (n1[0], "T")
#		n1[3].x.Copy (n1[0], "H")
		
