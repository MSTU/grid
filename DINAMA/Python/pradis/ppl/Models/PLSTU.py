from Model import *
from structs import *
from UTSLP import UTSLP

class PLSTU (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.PLSTU"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 6:
			ErrPrnMdl (2007, mdlname, 8, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) < 5 or len (pl) > 6:
			ErrPrnMdl (2009, mdlname, 5, 6, len (pl))
			raise af.LVPS_TException ("")

		for i in range(3):
			if nl[i].__class__ != XYZ:
				ErrPrnMdl (2006, mdlname, 1, "XYZ")
				raise af.LVPS_TException ("")
			
		for i in range(3):
			if nl[i+3].__class__ != DOF and nl[i+3].__class__ != DOF1:
				ErrPrnMdl (2006, mdlname, i+4, "dof1")
				raise af.LVPS_TException ("")
			
		for i in range(3):
			if pl[i].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, i+1, "pXYZ")
				raise af.LVPS_TException ("")
			
		if pl[3].__class__ != int and pl[3].__class__ != long and pl[3].__class__ != float:
			ErrPrnMdl (2004, mdlname, 4, "float")
			raise af.LVPS_TException ("")
			
		if pl[4].__class__ != ElasticMaterial:
			ErrPrnMdl (2004, mdlname, 5, "ElasticMaterial")
			raise af.LVPS_TException ("")

		if len(pl) > 5	:
			if pl[5].__class__ != int and pl[5].__class__ != long and pl[5].__class__ != float:
				ErrPrnMdl (2004, mdlname, 6, "float")
				raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, [pl[0].GetList(), pl[1].GetList(), 
						 pl[2].GetList(), pl[3].GetList(),
						 pl[4], pl[5].GetList(), pl[5:]])

		UTSLP(self,[],[])