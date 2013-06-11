import af
from glb import *
from OutValue import *

class DOF (af.DOF1):

	def __init__(self):
		self.this = af.DOF1 (root_list.Add())
		self.SetExternal (0)
		self.SetBase (0)

	def V (self):
		ov = OutValue()
		ov.type = 2
		ov.node = self
		return ov

	def A (self):
		ov = OutValue()
		ov.type = 3
		ov.node = self
		return ov
	
	def Copy (self, nd, d):
#		dl = nd.GetDOFList()
		if d == "x":
			sch.AddEquivalence (nd.x, self)
#			root_list.ChangeReferenceForAll (nd.x, self)
#			dl.ReplaceReference (nd.x, self)
			nd.x = self
		if d == "y":
			sch.AddEquivalence (nd.y, self)
#			root_list.ChangeReferenceForAll (nd.y, self)
#			dl.ReplaceReference (nd.y, self)
			nd.y = self
		if d == "z":
			sch.AddEquivalence (nd.z, self)
#			root_list.ChangeReferenceForAll (nd.z, self)
#			dl.ReplaceReference (nd.z, self)
			nd.z = self
		if d == "r":
			sch.AddEquivalence (nd.r, self)
#			root_list.ChangeReferenceForAll (nd.r, self)
#			dl.ReplaceReference (nd.r, self)
			nd.r = self
		if d == "rx":
			sch.AddEquivalence (nd.rx, self)
#			root_list.ChangeReferenceForAll (nd.rx, self)
#			dl.ReplaceReference (nd.rx, self)
			nd.rx = self
		if d == "ry":
			sch.AddEquivalence (nd.ry, self)
#			root_list.ChangeReferenceForAll (nd.ry, self)
#			dl.ReplaceReference (nd.ry, self)
			nd.ry = self
		if d == "rz":
			sch.AddEquivalence (nd.rz, self)
#			root_list.ChangeReferenceForAll (nd.rz, self)
#			dl.ReplaceReference (nd.rz, self)
			nd.rz = self
		if d == "T":
			sch.AddEquivalence (nd.T, self)
#			root_list.ChangeReferenceForAll (nd.rz, self)
#			dl.ReplaceReference (nd.rz, self)
			nd.T = self
		if d == "p":
			sch.AddEquivalence (nd.p, self)
#			root_list.ChangeReferenceForAll (nd.rz, self)
#			dl.ReplaceReference (nd.rz, self)
			nd.p = self
		if d == "H":
			sch.AddEquivalence (nd.H, self)
#			root_list.ChangeReferenceForAll (nd.rz, self)
#			dl.ReplaceReference (nd.rz, self)
			nd.H = self
