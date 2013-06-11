from Model import *
from structs import *

class KBASE (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.KBASE"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 1:
			ErrPrnMdl (2007, mdlname, 1, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 1:
			ErrPrnMdl (2008, mdlname, 1, len (pl))
			raise af.LVPS_TException ("")

		if nl[0].__class__ != XYZ:
			ErrPrnMdl (2006, mdlname, 1, "XYZ")
			raise af.LVPS_TException ("")
			
		if pl[0].__class__ != pXYZ:
			ErrPrnMdl (2004, mdlname, 1, "pXYZ")
			raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, pl[0].GetList())
