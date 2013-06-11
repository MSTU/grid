from Model import *
from misc import *
from structs import *

class KN3EF (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.KN3EF"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnMdl (2007, mdlname, 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) < 17:
			ErrPrnMdl (2010, mdlname, 17, len (pl))
			raise af.LVPS_TException ("")

		for i in range(2):
			if nl[i].__class__ != Point:
				ErrPrnMdl (2006, mdlname, i+1, "Point")
				raise af.LVPS_TException ("")
			
		for i in range(5):
			if pl[i].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, i+1, "pXYZ")
				raise af.LVPS_TException ("")

		if pl[5].__class__ != int and pl[5].__class__ != long and pl[5].__class__ != float:
			ErrPrnMdl (2004, mdlname, 6, "float")
			raise af.LVPS_TException ("")
			
		for i in range(4):
			if pl[i+6].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, i+7, "pXYZ")
				raise af.LVPS_TException ("")

		if pl[10].__class__ != int and pl[10].__class__ != long:
			ErrPrnMdl (2004, mdlname, 11, "int")
			raise af.LVPS_TException ("")
			
		if pl[11].__class__ != int and pl[11].__class__ != long:
			ErrPrnMdl (2004, mdlname, 12, "int")
			raise af.LVPS_TException ("")

		for i in range(pl[10]+pl[11]):
			if pl[12+i].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, 13+i, "pXYZ")
				raise af.LVPS_TException ("")
			
		for i in range(len(pl)-12-pl[10]-pl[11]):
			if pl[12+pl[10]+pl[11]+i].__class__ != ContactForceModel:
				ErrPrnMdl (2004, mdlname, 13+pl[10]+pl[11]+i, "ContactForceModel")
				raise af.LVPS_TException ("")
			
		par = []
		for n in range(5):
			Append (par, pl[n].GetList())
		par.append (pl[5])
		for n in range(4):
			Append (par, pl[n+6].GetList())
		par.append (pl[10])
		par.append (pl[11])
		for i in range(len(pl)-12):
			Append (par, pl[12+i].GetList())
				
		self.this = Model (mdlname, nl, par)
