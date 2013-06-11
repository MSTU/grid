from Image import *
from structs import *

class KONTUR (Image):
	def __init__ (self, model, pl, lp):
		pl = misc.Expand (pl)

		pgoname = "mechanics.KONTUR"
	
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
			
		if len (pl) < 2:
			ErrPrnPGO (2017, pgoname, 2, len (pl))
			raise af.LVPS_TException ("")

		for i in range(len(pl)):
			if pl[i].__class__ != pXY:
				ErrPrnPGO (2004, pgoname, i+1, "pXY")
				raise af.LVPS_TException ("")
			
		par = []
		for i in range(len(pl)):
			Append (par, pl[i].GetList())
				
		self.this = Image (model, pgoname, par, lp)
