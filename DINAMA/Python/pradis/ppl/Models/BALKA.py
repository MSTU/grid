from Model import *
from structs import *
from AKLAB import AKLAB

class BALKA (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.BALKA"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnMdl (2007, mdlname, 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 7:
			ErrPrnMdl (2008, mdlname, 7, len (pl))
			raise af.LVPS_TException ("")

		if nl[0].__class__ != Point2d:
			ErrPrnMdl (2006, mdlname, 1, "Point2d")
			raise af.LVPS_TException ("")
			
		if nl[1].__class__ != Point2d:
			ErrPrnMdl (2006, mdlname, 2, "Point2d")
			raise af.LVPS_TException ("")
			
		if pl[0].__class__ != pXY:
			ErrPrnMdl (2004, mdlname, 1, "pXY")
			raise af.LVPS_TException ("")
			
		if pl[1].__class__ != pXY:
			ErrPrnMdl (2004, mdlname, 2, "pXY")
			raise af.LVPS_TException ("")
			
		if pl[2].__class__ != int and pl[2].__class__ != long and pl[2].__class__ != float:
			ErrPrnMdl (2004, mdlname, 3, "float")
			raise af.LVPS_TException ("")
			
		if pl[3].__class__ != int and pl[3].__class__ != long and pl[3].__class__ != float:
			ErrPrnMdl (2004, mdlname, 4, "float")
			raise af.LVPS_TException ("")
			
		if pl[4].__class__ != int and pl[4].__class__ != long and pl[4].__class__ != float:
			ErrPrnMdl (2004, mdlname, 5, "float")
			raise af.LVPS_TException ("")
			
		if pl[5].__class__ != int and pl[5].__class__ != long and pl[5].__class__ != float:
			ErrPrnMdl (2004, mdlname, 6, "float")
			raise af.LVPS_TException ("")
			
		if pl[6].__class__ != int and pl[6].__class__ != long and pl[6].__class__ != float:
			ErrPrnMdl (2004, mdlname, 7, "float")
			raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, [pl[0].GetList(), pl[1].GetList(), pl[2:]])
		
		AKLAB (self, [], [])
