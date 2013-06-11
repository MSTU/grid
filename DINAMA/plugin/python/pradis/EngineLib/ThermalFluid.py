import af
from glb import *
from Node import *
from DOF import *


class ThermalFluid(Node):
	

	def __init__(self):
		self.this = Node (root_list.Add())
		l = af.TList (self.SetDOFList ())
		self.p = DOF ()
		l.Add (self.p)
		self.T = DOF ()
		l.Add (self.T)
#		self.H = DOF ()
#		l.Add (self.H)

	def associate (self, node, type):
		self.p.Copy (node, "p")
		self.T.Copy (node, "T")
#		self.H.Copy (node, "H")
