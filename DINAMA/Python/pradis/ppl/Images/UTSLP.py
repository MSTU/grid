from Image import *

class UTSLP (Image):
	def __init__ (self, model, pgoparams, lp):
		self.this = Image (model, "mechanics.UTSLP", pgoparams, lp)
