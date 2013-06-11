from Model import *
from structs import *
from KOLB import KOLB

class BLOK (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.BLOK"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 8:
			ErrPrnMdl (2007, mdlname, 8, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 9:
			ErrPrnMdl (2008, mdlname, 9, len (pl))
			raise af.LVPS_TException ("")

		for i in range(8):
			if nl[i].__class__ != XYZ:
				ErrPrnMdl (2006, mdlname, i+1, "XYZ")
				raise af.LVPS_TException ("")

		for i in range(8):	
			if pl[i].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, i+1, "pXYZ")
				raise af.LVPS_TException ("")
		
		if pl[8].__class__ != ElasticMaterial:
			ErrPrnMdl (2004, mdlname, 9, "ElasticMaterial")
			raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, [pl[0].GetList(), pl[1].GetList(), pl[2].GetList(),
						 pl[3].GetList(), pl[4].GetList(), pl[5].GetList(),
						 pl[6].GetList(), pl[7].GetList(), pl[8].GetList()])

		KOLB(self,[],[])