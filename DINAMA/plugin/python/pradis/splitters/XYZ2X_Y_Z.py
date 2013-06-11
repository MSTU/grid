import af
import misc
from glb import *
from Node import *
from DOF import *

class XYZ2X_Y_Z:

	def __init__(self, n1, n2, desc = misc.default):
		n1[1].x.Copy (n1[0], "x")
		n1[2].x.Copy (n1[0], "y")
		n1[3].x.Copy (n1[0], "z")
		
