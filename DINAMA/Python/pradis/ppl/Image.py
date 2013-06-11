import af
import glb
import misc
from structs import *
from Model import *

class Image (af.Image):

	def __init__ (self, model, pgo, pgoparams, lp, desc=misc.default):

		if lp.__class__ != list and lp.__class__ != tuple:
			ErrPrnPGO (2024, pgo)
			raise af.LVPS_TException ("")

		if len (lp) == 0:
			lp = ['YELLOW','gold',1.0]

		if lp[0].__class__ != str:
			ErrPrnPGO (2025, pgo, 1, "STR")
			raise af.LVPS_TException ("")

		if lp[2].__class__ != int and lp[2].__class__ != long and lp[2].__class__ != float:
			ErrPrnPGO (2025, pgo, 2, "float")
			raise af.LVPS_TException ("")

		if lp[1].__class__ != str:
			ErrPrnPGO (2025, pgo, 3, "STR")
			raise af.LVPS_TException ("")

		ilist = glb.sch.GetImageList()
		self.this = af.Image (ilist.Add())
		if desc != misc.default:
			self.SetDescription(desc)
		self.SetObjectName (pgo)

		ddd = dir(model)
		ismdl = 1
		if ddd.count("GetName") == 0:
			ismdl = 0
		if ismdl == 1:
			if model.GetName() != "Model":
				ismdl = 0
	
		if ismdl == 1:
			self.SetImageModel (model)

		misc.AddParameters (self, pgoparams)
		layer = af.Layer (self.SetLayerParameters())
		layer.SetColor (lp[0])
		layer.SetMaterial (lp[1])
		layer.SetTransparency (lp[2])
	
