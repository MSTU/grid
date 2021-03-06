from Model import *
from structs import *

class BELT (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.BELT"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnMdl (2007, mdlname, 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 5:
			ErrPrnMdl (2008, mdlname, 5, len (pl))
			raise af.LVPS_TException ("")

		if nl[0].__class__ != XYZ:
			ErrPrnMdl (2006, mdlname, 1, "XYZ")
			raise af.LVPS_TException ("")
			
		if nl[1].__class__ != XYZ:
			ErrPrnMdl (2006, mdlname, 2, "XYZ")
			raise af.LVPS_TException ("")
			
		if pl[0].__class__ != pXYZ:
			ErrPrnMdl (2004, mdlname, 1, "pXYZ")
			raise af.LVPS_TException ("")
			
		if pl[1].__class__ != pXYZ:
			ErrPrnMdl (2004, mdlname, 2, "pXYZ")
			raise af.LVPS_TException ("")
			
		if pl[2].__class__ != int and pl[2].__class__ != long and pl[2].__class__ != float:
			ErrPrnMdl (2004, mdlname, 3, "float")
			raise af.LVPS_TException ("")
			
		if pl[3].__class__ != int and pl[3].__class__ != long and pl[3].__class__ != float:
			ErrPrnMdl (2004, mdlname, 4, "float")
			raise af.LVPS_TException ("")
			
		if pl[4].__class__ != Diagram:
			ErrPrnMdl (2004, mdlname, 5, "Diagram")
			raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, [pl[0].GetList(), pl[1].GetList(), pl[2:4], pl[4].GetTable()])
