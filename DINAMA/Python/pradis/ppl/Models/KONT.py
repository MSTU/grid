from Model import *
from structs import *
from TNOK import TNOK

class KONT (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.KONT"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnMdl (2007, mdlname, 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 7:
			ErrPrnMdl (2008, mdlname, 7, len (pl))
			raise af.LVPS_TException ("")

		if nl[0].__class__ != XY:
			ErrPrnMdl (2006, mdlname, 1, "XY")
			raise af.LVPS_TException ("")
			
		if nl[1].__class__ != Point2d:
			ErrPrnMdl (2006, mdlname, 2, "Point2d")
			raise af.LVPS_TException ("")

		for i in range(2):	
			if pl[i].__class__ != pXY:
				ErrPrnMdl (2004, mdlname, i+1, "pXY")
				raise af.LVPS_TException ("")
			
		for i in range(4):	
			if pl[i+2].__class__ != int and pl[i+2].__class__ != long and pl[i+2].__class__ != float:
				ErrPrnMdl (2004, mdlname, i+3, "float")
				raise af.LVPS_TException ("")
			
		if pl[6].__class__ != Diagram:
			ErrPrnMdl (2004, mdlname, 7, "Diagram")
			raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, [pl[0].GetList(), pl[1].GetList(), pl[2:6], pl[6].GetTable()])

		TNOK(self,[],[])