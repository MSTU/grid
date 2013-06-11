from Model import *
from structs import *

class VWN3D (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.VWN3D"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 1:
			ErrPrnMdl (2007, mdlname, 1, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 4:
			ErrPrnMdl (2008, mdlname, 4, len (pl))
			raise af.LVPS_TException ("")

		for i in range(1):
			if nl[0].__class__ != Point:
				ErrPrnMdl (2006, mdlname, i+1, "Point")
				raise af.LVPS_TException ("")
			
		for i in range(3):
			if pl[i].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, i+1, "pXYZ")
				raise af.LVPS_TException ("")
			
		if pl[3].__class__ != int and pl[3].__class__ != long and pl[3].__class__ != float:
			ErrPrnMdl (2004, mdlname, 4, "float")
			raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, [pl[0].GetList(), pl[1].GetList(), pl[2].GetList(), pl[3]])
