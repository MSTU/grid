from Image import *

class NGRTS (Image):
	def __init__ (self, model, pgoparams, lp):
		self.this = Image (model, "mechanics.NGRTS", pgoparams, lp)
