from Model import *
from misc import *
from structs import *

class KN3EP (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.KN3EP"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnMdl (2007, mdlname, 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) < 11 or len (pl) > 22:
			ErrPrnMdl (2009, mdlname, 11, 22, len (pl))
			raise af.LVPS_TException ("")

		for i in range(2):
			if nl[i].__class__ != Point:
				ErrPrnMdl (2006, mdlname, i+1, "Point")
				raise af.LVPS_TException ("")
			
		for n in range(5):
			if pl[n].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, n+1, "pXYZ")
				raise af.LVPS_TException ("")

		if pl[5].__class__ != int and pl[5].__class__ != long and pl[5].__class__ != float:
			ErrPrnMdl (2004, mdlname, 6, "float")
			raise af.LVPS_TException ("")
			
		for i in range(4):
			if pl[i+6].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, i+7, "pXYZ")
				raise af.LVPS_TException ("")

		for i in range(len(pl)-10):
			if pl[i+10].__class__ != ContactForceModel:
				ErrPrnMdl (2004, mdlname, i+11, "ContactForceModel")
				raise af.LVPS_TException ("")
			
		par = []
		for i in range(5):
			Append (par, pl[i].GetList())
		par.append (pl[5])
		for i in range(4):
			Append (par, pl[i+6].GetList())
		for i in range(len(pl)-10):
			Append (par, pl[10+i].GetList())
				
		self.this = Model (mdlname, nl, par)
