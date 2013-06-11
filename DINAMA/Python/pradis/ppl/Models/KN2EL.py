from Model import *
from structs import *
from LE2NK import LE2NK

class KN2EL (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.KN2EL"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnMdl (2007, mdlname, 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 8:
			ErrPrnMdl (2008, mdlname, 8, len (pl))
			raise af.LVPS_TException ("")

		for i in range(2):
			if nl[i].__class__ != Point2d:
				ErrPrnMdl (2006, mdlname, i+1, "Point2d")
				raise af.LVPS_TException ("")

		for i in range(3):	
			if pl[i].__class__ != pXY:
				ErrPrnMdl (2004, mdlname, i+1, "pXY")
				raise af.LVPS_TException ("")
			
		for i in range(3):	
			if pl[i+3].__class__ != int and pl[i+3].__class__ != long and pl[i+3].__class__ != float:
				ErrPrnMdl (2004, mdlname, i+4, "float")
				raise af.LVPS_TException ("")
			
		if pl[6].__class__ != pXY:
			ErrPrnMdl (2004, mdlname, 7, "pXY")
			raise af.LVPS_TException ("")
			
		if pl[7].__class__ != Diagram:
			ErrPrnMdl (2004, mdlname, 8, "Diagram")
			raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, [pl[0].GetList(), pl[1].GetList(), pl[2].GetList(),
						 pl[3:6], pl[6].GetList(), pl[7].GetTable()])

		LE2NK (self, [], [])