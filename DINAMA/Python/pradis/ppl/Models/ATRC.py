from Model import *
from structs import *

class ATRC (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.ATRC"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnMdl (2007, mdlname, 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 3:
			ErrPrnMdl (2008, mdlname, 3, len (pl))
			raise af.LVPS_TException ("")

		if nl[0].__class__ != DOF and nl[0].__class__ != DOF1:
			ErrPrnMdl (2006, mdlname, 1, "dof1")
			raise af.LVPS_TException ("")
			
		if nl[1].__class__ != DOF and nl[1].__class__ != DOF1:
			ErrPrnMdl (2006, mdlname, 2, "dof1")
			raise af.LVPS_TException ("")
			
		if pl[0].__class__ != TrapeziumData:
			ErrPrnMdl (2004, mdlname, 1, "TrapeziumData")
			raise af.LVPS_TException ("")
			
		if pl[1].__class__ != int and pl[1].__class__ != long and pl[1].__class__ != float:
			ErrPrnMdl (2004, mdlname, 2, "float")
			raise af.LVPS_TException ("")
			
		if pl[2].__class__ != int and pl[2].__class__ != long and pl[2].__class__ != float:
			ErrPrnMdl (2004, mdlname, 3, "float")
			raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, [pl[0].GetList(), pl[1:]])
