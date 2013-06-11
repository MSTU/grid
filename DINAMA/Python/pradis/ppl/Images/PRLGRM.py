from Image import *
from structs import *

class PRLGRM (Image):
	def __init__ (self, model, pl, lp):
		pl = misc.Expand (pl)

		pgoname = "mechanics.PRLGRM"
	
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

		for i in range(4):
			if pl[i].__class__ != pXYZ:
				ErrPrnPGO (2004, pgoname, i+1, "pXYZ")
				raise af.LVPS_TException ("")
			
		par = []
		for i in range(4):
			Append (par, pl[i].GetList())
				
		self.this = Image (model, pgoname, par, lp)
