from Image import *
from structs import *

class ELP3D (Image):
	def __init__ (self, model, pl, lp):
		pl = misc.Expand (pl)

		pgoname = "mechanics.ELP3D"
	
		if pl.__class__ != list and pl.__class__ != tuple:
			ErrPrnPGO (2022, pgoname)
			raise af.LVPS_TException ("")
		
		ddd = dir(model)
		ismdl = 1
		if ddd.count("GetName") == 0:
			ismdl = 0
		if ismdl == 1:
			if model.GetName() != "Model":
				ismdl = 0
	
		if ismdl == 0:
			if len(pl) != 5:
				ErrPrnPGO (2008, 5, len(pl))
				raise af.LVPS_TException ("")
			for i in range(3):
				if pl[i].__class__ != pXYZ:
					ErrPrnPGO (2004, i+1, "pXYZ")
					raise af.LVPS_TException ("")
			for i in range(len(pl)-3):
				if pl[i+3].__class__ != int and pl[i+3].__class__ != long and pl[i+3].__class__ != float:
					ErrPrnPGO (2004, i+4, "float")
					raise af.LVPS_TException ("")
			par = [pl[0].GetList(), pl[1].GetList(), pl[2].GetList(), pl[3:]]
		else:
				
			if len(pl) != 3:
				ErrPrnPGO (2008, 3, len(pl))
				raise af.LVPS_TException ("")
			for i in range(1):
				if pl[i].__class__ != pXYZ:
					ErrPrnPGO (2004, i+1, "pXYZ")
					raise af.LVPS_TException ("")
			for i in range(len(pl)-1):
				if pl[i+1].__class__ != int and pl[i+1].__class__ != long and pl[i+1].__class__ != float:
					ErrPrnPGO (2004, i+2, "float")
					raise af.LVPS_TException ("")
			par = [pl[0].GetList(), pl[1:]]
		
		self.this = Image (model, pgoname, par, lp)
