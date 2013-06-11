from Model import *
from misc import *
from structs import *

class KN3EE (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.KN3EE"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnMdl (2007, mdlname, 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) < 13 or len (pl) > 24:
			ErrPrnMdl (2009, mdlname, 13, 24, len (pl))
			raise af.LVPS_TException ("")

		for i in range(2):
			if nl[i].__class__ != Point:
				ErrPrnMdl (2006, mdlname, i+1, "Point")
				raise af.LVPS_TException ("")
			
		for i in range(2):
			for n in range(5):
				if pl[n+6*i].__class__ != pXYZ:
					ErrPrnMdl (2004, mdlname, n+6*i+1, "pXYZ")
					raise af.LVPS_TException ("")
			if pl[6*i+5].__class__ != int and pl[6*i+5].__class__ != long and pl[6*i+5].__class__ != float:
				ErrPrnMdl (2004, mdlname, 6*i+6, "float")
				raise af.LVPS_TException ("")
			
		for i in range(len(pl)-12):
			if pl[i+12].__class__ != ContactForceModel:
				ErrPrnMdl (2004, mdlname, i+13, "ContactForceModel")
				raise af.LVPS_TException ("")
			
		par = []
		for i in range(2):
			for n in range(5):
				Append (par, pl[i*6+n].GetList())
			par.append (pl[i*6+5])
		for i in range(len(pl)-12):
			Append (par, pl[12+i].GetList())
				
		self.this = Model (mdlname, nl, par)
