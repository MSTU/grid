from Model import *
from structs import *
from LRTET import LRTET

class TETRL (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.TETRL"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 4:
			ErrPrnMdl (2007, mdlname, 4, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 5:
			ErrPrnMdl (2008, mdlname, 5, len (pl))
			raise af.LVPS_TException ("")

		for i in range(4):
			if nl[0].__class__ != XYZ:
				ErrPrnMdl (2006, mdlname, i+1, "XYZ")
				raise af.LVPS_TException ("")
			
		for i in range(4):
			if pl[i].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, i+1, "pXYZ")
				raise af.LVPS_TException ("")
			
		if pl[4].__class__ != ElasticMaterial:
			ErrPrnMdl (2004, mdlname, 5, "ElasticMaterial")
			raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, [pl[0].GetList(), pl[1].GetList(), 
						 pl[2].GetList(), pl[3].GetList(), pl[4].GetList()])

		LRTET (self, [], [])