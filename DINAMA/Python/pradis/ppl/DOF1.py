import af
from glb import *
from Node import *
from OutValue import *
#test
from DOF import *

class DOF1 (Node):

	def __init__(self):
		self.this = Node (root_list.Add())
#		l = self.GetDOFList ()
#		self.x = af.DOF1 (l.Add())

		l = af.TList (self.SetDOFList ())
		self.x = DOF ()
		l.Add (self.x)


		
		self.x.SetExternal (0)
		self.x.SetBase (0)

	def V (self):
		ov = OutValue()
		ov.type = 2
		ov.node = self.x
		return ov

	def A (self):
		ov = OutValue()
		ov.type = 3
		ov.node = self.x
		return ov
	
	def associate (self, node, type):
#		print 'x=',node
		self.x.Copy (node, "x")
