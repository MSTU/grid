from Model import *
from structs import *

class KNCLT (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.KNCLT"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 3:
			ErrPrnMdl (2007, mdlname, 3, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 9:
			ErrPrnMdl (2008, mdlname, 9, len (pl))
			raise af.LVPS_TException ("")

		for i in range(3):
			if nl[i].__class__ != XYZ:
				ErrPrnMdl (2006, mdlname, i+1, "XYZ")
				raise af.LVPS_TException ("")

		for i in range(3):	
			if pl[i].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, i+1, "pXYZ")
				raise af.LVPS_TException ("")
			
		for i in range(6):	
			if pl[i+3].__class__ != int and pl[i+3].__class__ != long and pl[i+3].__class__ != float:
				ErrPrnMdl (2004, mdlname, i+4, "float")
				raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, [pl[0].GetList(), pl[1].GetList(), pl[2].GetList(), pl[3:]])
