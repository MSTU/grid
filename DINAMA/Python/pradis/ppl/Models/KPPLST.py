from Model import *
from structs import *

class KPPLST (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.KPPLST"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnMdl (2007, mdlname, 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 5:
			ErrPrnMdl (2008, mdlname, 5, len (pl))
			raise af.LVPS_TException ("")

		for i in range(2):
			if nl[i].__class__ != DOF and nl[i].__class__ != DOF1:
				ErrPrnMdl (2006, mdlname, i+1, "dof1")
				raise af.LVPS_TException ("")
			
		for i in range(2):
			if pl[i].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, i+1, "pXYZ")
				raise af.LVPS_TException ("")
			
		for i in range(3):
			if pl[i+2].__class__ != int and pl[i+2].__class__ != long and pl[i+2].__class__ != float:
				ErrPrnMdl (2004, mdlname, i+3, "float")
				raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, [pl[0].GetList(), pl[1].GetList(), pl[2:]])
