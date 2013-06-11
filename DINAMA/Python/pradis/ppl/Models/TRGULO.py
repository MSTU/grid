from Model import *
from structs import *
from LUGRT import LUGRT

class TRGULO (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.TRGULO"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 3:
			ErrPrnMdl (2007, mdlname, 3, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 4:
			ErrPrnMdl (2008, mdlname, 4, len (pl))
			raise af.LVPS_TException ("")

		for i in range(3):
			if nl[0].__class__ != XY:
				ErrPrnMdl (2006, mdlname, i+1, "XY")
				raise af.LVPS_TException ("")
			
		for i in range(3):
			if pl[i].__class__ != pXY:
				ErrPrnMdl (2004, mdlname, i+1, "pXY")
				raise af.LVPS_TException ("")
			
		if pl[3].__class__ != ElasticMaterial:
			ErrPrnMdl (2004, mdlname, 4, "ElasticMaterial")
			raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, [pl[0].GetList(), pl[1].GetList(), pl[2].GetList(), pl[3].GetList()])

		LUGRT (self, [],[])