from Image import *

class LUGRT (Image):
	def __init__ (self, model, pgoparams, lp):
		self.this = Image (model, "mechanics.LUGRT", pgoparams, lp)
