from Model import *
from structs import *
from KALUK import KALUK

class KULAK (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.KULAK"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnMdl (2007, mdlname, 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 14:
			ErrPrnMdl (2008, mdlname, 14, len (pl))
			raise af.LVPS_TException ("")

		for i in range(2):
			if nl[i].__class__ != Point2d:
				ErrPrnMdl (2006, mdlname, i+1, "Point2d")
				raise af.LVPS_TException ("")
			
		if pl[0].__class__ != XYF:
			ErrPrnMdl (2004, mdlname, 1, "XYF")
			raise af.LVPS_TException ("")
			
		for i in range(4):
			if pl[i+1].__class__ != int and pl[i+1].__class__ != long and pl[i+1].__class__ != float:
				ErrPrnMdl (2004, mdlname, i+2, "float")
				raise af.LVPS_TException ("")
			
		if pl[5].__class__ != XYF:
			ErrPrnMdl (2004, mdlname, 6, "XYF")
			raise af.LVPS_TException ("")
			
		for i in range(7):
			if pl[i+6].__class__ != int and pl[i+6].__class__ != long and pl[i+6].__class__ != float:
				ErrPrnMdl (2004, mdlname, i+7, "float")
				raise af.LVPS_TException ("")
			
		if pl[13].__class__ != Diagram:
			ErrPrnMdl (2004, mdlname, 14, "Diagram")
			raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, [pl[0].GetList(), pl[1:5], pl[5].GetList(), pl[6:13], pl[13].GetTable()])

		KALUK (self, [], [])