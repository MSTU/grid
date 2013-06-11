from Image import *
from misc import *
from structs import *

class KAR3D (Image):
	def __init__ (self, model, pl, lp):
		pl = misc.Expand (pl)

		pgoname = "mechanics.KAR3D"
	
		ddd = dir(model)
		if ddd.count("GetName") == 0:
			ErrPrnPGO (2023, pgoname)
			raise af.LVPS_TException ("")
	
		if model.GetName() != "Model":
			ErrPrnPGO (2023, pgoname)
			raise af.LVPS_TException ("")

		if pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnPGO (2022, pgoname)
			raise af.LVPS_TException ("")
			
		if len (pl) < 3:
			ErrPrnPGO (2017, pgoname, 3, len (pl))
			raise af.LVPS_TException ("")

		if pl[0].__class__ != int and pl[0].__class__ != long and pl[0].__class__ != float:
			ErrPrnPGO (2004, pgoname, 1, "float")
			raise af.LVPS_TException ("")
			
		for i in range(len(pl)-1):
			if pl[i+1].__class__ != pXYZ:
				ErrPrnPGO (2004, pgoname, i+2, "pXYZ")
				raise af.LVPS_TException ("")
			
		par = [pl[0]]
		for i in range(len(pl)-1):
			Append (par, pl[i+1].GetList())
				
		self.this = Image (model, pgoname, par, lp)
