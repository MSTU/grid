from Model import *
from structs import *

class SV3KTU (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.SV3KTU"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 3:
			ErrPrnMdl (2007, mdlname, 3, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 4:
			ErrPrnMdl (2008, mdlname, 4, len (pl))
			raise af.LVPS_TException ("")

		for i in range(2):
			if nl[0].__class__ != XYZ:
				ErrPrnMdl (2006, mdlname, i+1, "XYZ")
				raise af.LVPS_TException ("")
			
		if nl[2].__class__ != DOF and nl[2].__class__ != DOF1:
			ErrPrnMdl (2006, mdlname, i+3, "dof1")
			raise af.LVPS_TException ("")
			
		for i in range(2):
			if pl[i].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, i+1, "pXYZ")
				raise af.LVPS_TException ("")
			
		if pl[2].__class__ != int and pl[2].__class__ != long and pl[2].__class__ != float:
			ErrPrnMdl (2004, mdlname, 3, "float")
			raise af.LVPS_TException ("")
			
		if pl[3].__class__ != Diagram:
			ErrPrnMdl (2004, mdlname, 4, "Diagram")
			raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, [pl[0].GetList(), pl[1].GetList(), pl[2], pl[3].GetTable()])
