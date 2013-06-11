import af
from glb import *
from Node import *
from DOF import *


class XY2X_Y:

	def __init__(self, n1, n2):
		n1[1].x.Copy (n1[0], "x")
		n1[2].x.Copy (n1[0], "y")
		

#		n2.x.Copy (n1, "x")
#		n3.x.Copy (n1, "y")
#  	n1.x.Copy (n2, "x")
#	  n1.y.Copy (n3, "x")
