import af
from glb import *
from Node import *
from DOF import *

class XYZ (Node):

	def __init__(self):
		self.this = Node (root_list.Add())
		l = af.TList (self.SetDOFList ())
		self.x = DOF ()
		l.Add (self.x)
		self.y = DOF ()
		l.Add (self.y)
		self.z = DOF ()
		l.Add (self.z)

	def associate (self, node, type):
		self.x.Copy (node, "x")
		self.y.Copy (node, "y")
		self.z.Copy (node, "z")
