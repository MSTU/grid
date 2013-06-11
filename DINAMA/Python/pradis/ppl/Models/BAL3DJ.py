from Model import *
from structs import *
from D3LAB import D3LAB

class BAL3DJ (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.BAL3DJ"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnMdl (2007, mdlname, 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) != 6:
			ErrPrnMdl (2008, mdlname, 6, len (pl))
			raise af.LVPS_TException ("")

		if nl[0].__class__ != Point:
			ErrPrnMdl (2006, mdlname, 1, "Point")
			raise af.LVPS_TException ("")
			
		if nl[1].__class__ != Point:
			ErrPrnMdl (2006, mdlname, 2, "Point")
			raise af.LVPS_TException ("")
			
		if pl[0].__class__ != pXYZ:
			ErrPrnMdl (2004, mdlname, 1, "pXYZ")
			raise af.LVPS_TException ("")
			
		if pl[1].__class__ != pXYZ:
			ErrPrnMdl (2004, mdlname, 2, "pXYZ")
			raise af.LVPS_TException ("")
			
		if pl[2].__class__ != pXYZ:
			ErrPrnMdl (2004, mdlname, 3, "pXYZ")
			raise af.LVPS_TException ("")
			
		if pl[3].__class__ != InertiaMoment:
			ErrPrnMdl (2004, mdlname, 4, "InertiaMoment")
			raise af.LVPS_TException ("")
			
		if pl[4].__class__ != int and pl[4].__class__ != long and pl[4].__class__ != float:
			ErrPrnMdl (2004, mdlname, 5, "float")
			raise af.LVPS_TException ("")
			
		if pl[5].__class__ != ElasticMaterial:
			ErrPrnMdl (2004, mdlname, 6, "Material")
			raise af.LVPS_TException ("")
			
		self.this = Model (mdlname, nl, [pl[0].GetList(), pl[1].GetList(), pl[2].GetList(), pl[3].GetList(), pl[4], pl[5].GetList()])

		D3LAB (self, [], [])
		