from Model import *
from misc import *
from structs import *

class KN3TP (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.KN3TP"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnMdl (2007, mdlname, 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) < 6 or len (pl) > 17:
			ErrPrnMdl (2009, mdlname, 6, 17, len (pl))
			raise af.LVPS_TException ("")

		if nl[0].__class__ != XYZ:
			ErrPrnMdl (2006, mdlname, 1, "XYZ")
			raise af.LVPS_TException ("")
			
		if nl[1].__class__ != Point:
			ErrPrnMdl (2006, mdlname, 2, "Point")
			raise af.LVPS_TException ("")
			
		for n in range(5):
			if pl[n].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, n+1, "pXYZ")
				raise af.LVPS_TException ("")
			
		for i in range(len(pl)-5):
			if pl[i+5].__class__ != ContactForceModel:
				ErrPrnMdl (2004, mdlname, i+6, "ContactForceModel")
				raise af.LVPS_TException ("")
			
		par = []
		for i in range(len(pl)):
			Append (par, pl[i].GetList())
				
		self.this = Model (mdlname, nl, par)
