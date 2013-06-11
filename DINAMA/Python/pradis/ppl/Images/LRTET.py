from Image import *

class LRTET (Image):
	def __init__ (self, model, pgoparams, lp):
		self.this = Image (model, "mechanics.LRTET", pgoparams, lp)
