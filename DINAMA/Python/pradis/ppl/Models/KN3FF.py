from Model import *
from misc import *
from structs import *

class KN3FF (Model):
	def __init__ (self, nl, pl):

		pl = misc.Expand (pl)

		mdlname = "mechanics.KN3FF"
	
		if nl.__class__ != list and nl.__class__ != tuple or pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnMdl (2005, mdlname)
			raise af.LVPS_TException ("")
			
		if len (nl) != 2:
			ErrPrnMdl (2007, mdlname, 2, len (nl))
			raise af.LVPS_TException ("")

		if len (pl) < 21:
			ErrPrnMdl (2010, mdlname, 21, len (pl))
			raise af.LVPS_TException ("")

		for i in range(2):
			if nl[i].__class__ != Point:
				ErrPrnMdl (2006, mdlname, i+1, "Point")
				raise af.LVPS_TException ("")
			
		for i in range(4):
			if pl[i].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, i+1, "pXYZ")
				raise af.LVPS_TException ("")

		if pl[4].__class__ != int and pl[4].__class__ != long:
			ErrPrnMdl (2004, mdlname, 5, "int")
			raise af.LVPS_TException ("")
		a1 = pl[4]
			
		if pl[5].__class__ != int and pl[5].__class__ != long:
			ErrPrnMdl (2004, mdlname, 6, "int")
			raise af.LVPS_TException ("")
		b1 = pl[5]

		for i in range(a1+b1):
			if pl[6+i].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, 7+i, "pXYZ")
				raise af.LVPS_TException ("")
			
		d = 6 + a1 + b1
				
		for i in range(4):
			if pl[d+i].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, i+d+1, "pXYZ")
				raise af.LVPS_TException ("")

		if pl[4+d].__class__ != int and pl[4+d].__class__ != long:
			ErrPrnMdl (2004, mdlname, 5+d, "int")
			raise af.LVPS_TException ("")
		a2 = pl[4+d]
			
		if pl[5+d].__class__ != int and pl[5+d].__class__ != long:
			ErrPrnMdl (2004, mdlname, 6+d, "int")
			raise af.LVPS_TException ("")
		b2 = pl[5+d]

		for i in range(a2 + b2):
			if pl[d+6+i].__class__ != pXYZ:
				ErrPrnMdl (2004, mdlname, 7+i+d, "pXYZ")
				raise af.LVPS_TException ("")
			
		for i in range(len(pl)-12-a1-a2-b1-b2):
			if pl[12+a1+a2+b1+b2+i].__class__ != ContactForceModel:
				ErrPrnMdl (2004, mdlname, 13+a1+a2+b1+b2+i, "ContactForceModel")
				raise af.LVPS_TException ("")
			
		par = []
		for n in range(4):
			Append (par, pl[n].GetList())
		par.append (pl[4])
		par.append (pl[5])
		for n in range(a1+b1):
			Append (par, pl[n+6].GetList())
		for n in range(4):
			Append (par, pl[n+d].GetList())
		par.append (pl[4+d])
		par.append (pl[5+d])
		for n in range(a2+b2):
			Append (par, pl[n+6+d].GetList())
		for i in range(len(pl)-12-a1-a2-b1-b2):
			Append (par, pl[12+i+a1+a2+b1+b2].GetList())
				
		self.this = Model (mdlname, nl, par)
