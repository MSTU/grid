import af
from glb import *
from Node import *
from DOF import *

class Point2DOFs:

	def __init__(self, n1, n2):
		n1[1].x.Copy (n1[0], "x")
		n1[2].x.Copy (n1[0], "y")
		n1[3].x.Copy (n1[0], "z")
		n1[4].x.Copy (n1[0], "rx")
		n1[5].x.Copy (n1[0], "ry")
		n1[6].x.Copy (n1[0], "rz")
		
