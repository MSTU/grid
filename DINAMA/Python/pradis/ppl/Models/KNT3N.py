from Model import *
from structs import *

class KNT3N (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.KNT3N"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 1:
			ErrPrnMdl (2007, mdlname, 1, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 6:
			ErrPrnMdl (2008, mdlname, 6, len (pl))
			raise af.LVPS_TException ("")

		if nl[0].__class__ != XYZ and nl[0].__class__ != RotationXYZ:
			ErrPrnMdl (2006, mdlname, 1, "XYZ")
			raise af.LVPS_TException ("")
			
		for i in range(3):
			if pl[i].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, i+1, "pXYZ")
				raise af.LVPS_TException ("")
			
		for i in range(3):
			if pl[i+3].__class__ != int and pl[i+3].__class__ != long and pl[i+3].__class__ != float:
				ErrPrnMdl (2004, mdlname, i+4, "float")
				raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, [pl[0].GetList(),pl[1].GetList(), pl[2].GetList(), pl[3:]])
