import af
from glb import *
from Node import *
from DOF import *

class Point2d2XY_R:

	def __init__(self, n1, n2):
		n1[1].x.Copy (n1[0], "x")
		n1[1].y.Copy (n1[0], "y")
		n1[2].x.Copy (n1[0], "r")
		
