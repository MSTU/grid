from Image import *

class PPGRT (Image):
	def __init__ (self, model, pgoparams, lp):
		self.this = Image (model, "mechanics.PPGRT", pgoparams, lp)
