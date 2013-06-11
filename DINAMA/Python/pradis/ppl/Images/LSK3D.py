from Image import *
from structs import *

class LSK3D (Image):
	def __init__ (self, model, pl, lp):
		pl = misc.Expand (pl)

		pgoname = "mechanics.LSK3D"
	
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
			
		if len (pl) != 4:
			ErrPrnPGO (2008, pgoname, 4, len (pl))
			raise af.LVPS_TException ("")

		for i in range(3):
			if pl[i].__class__ != pXYZ:
				ErrPrnPGO (2004, pgoname, i+1, "pXYZ")
				raise af.LVPS_TException ("")
			
		for i in range(len(pl)-3):
			if pl[i+3].__class__ != int and pl[i+3].__class__ != long and pl[i+3].__class__ != float:
				ErrPrnPGO (2004, pgoname, i+4, "float")
				raise af.LVPS_TException ("")
			
		par = []
		for i in range(3):
			misc.Append (par, pl[i].GetList())
		misc.Append (par, pl[3:])
				
		self.this = Image (model, pgoname, par, lp)
