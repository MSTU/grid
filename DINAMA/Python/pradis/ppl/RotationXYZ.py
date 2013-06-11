import af
from glb import *
from Node import *
from DOF import *

class RotationXYZ (Node):

	def __init__(self):
		self.this = Node (root_list.Add())
		l = af.TList (self.SetDOFList ())
		self.rx = DOF ()
		l.Add (self.rx)
		self.ry = DOF ()
		l.Add (self.ry)
		self.rz = DOF ()
		l.Add (self.rz)
