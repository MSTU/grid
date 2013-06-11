from Image import *
from misc import *
from structs import *

class ELPSMD (Image):
	def __init__ (self, model, pl, lp):
		pl = misc.Expand (pl)

		pgoname = "mechanics.ELPSMD"
	
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
			
		if len (pl) != 6:
			ErrPrnPGO (2008, pgoname, 6, len (pl))
			raise af.LVPS_TException ("")

		for i in range(2):
			if pl[i].__class__ != pXY:
				ErrPrnPGO (2004, pgoname, i+1, "pXY")
				raise af.LVPS_TException ("")
			
		for i in range(4):
			if pl[i+2].__class__ != int and pl[i+2].__class__ != long and pl[i+2].__class__ != float:
				ErrPrnPGO (2004, pgoname, i+3, "float")
				raise af.LVPS_TException ("")
			
		par = []
		for i in range(2):
			Append (par, pl[i].GetList())
		Append (par, pl[2:])
				
		self.this = Image (model, pgoname, par, lp)
