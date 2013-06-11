from Model import *
from structs import *

class VNKS (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.VNKS"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 4:
			ErrPrnMdl (2007, mdlname, 4, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 5:
			ErrPrnMdl (2008, mdlname, 5, len (pl))
			raise af.LVPS_TException ("")

		if nl[0].__class__ != DOF and nl[0].__class__ != DOF1:
			ErrPrnMdl (2006, mdlname, 1, "dof1")
			raise af.LVPS_TException ("")
			
		if nl[1].__class__ != XY:
			ErrPrnMdl (2006, mdlname, 2, "XY")
			raise af.LVPS_TException ("")
			
		if nl[2].__class__ != DOF and nl[2].__class__ != DOF1:
			ErrPrnMdl (2006, mdlname, 3, "dof1")
			raise af.LVPS_TException ("")
			
		if nl[3].__class__ != XY:
			ErrPrnMdl (2006, mdlname, 4, "XY")
			raise af.LVPS_TException ("")
			
		for i in range(3):
			if pl[i].__class__ != pXY:
				ErrPrnMdl (2004, mdlname, i+1, "pXY")
				raise af.LVPS_TException ("")
			
		for i in range(2):
			if pl[i+3].__class__ != int and pl[i+3].__class__ != long and pl[i+3].__class__ != float:
				ErrPrnMdl (2004, mdlname, i+4, "float")
				raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, [pl[0].GetList(), pl[1].GetList(), pl[2].GetList(), pl[3:]])
