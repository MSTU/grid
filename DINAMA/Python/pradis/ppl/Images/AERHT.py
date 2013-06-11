from Image import *

class AERHT (Image):
	def __init__ (self, model, pgoparams, lp):
		self.this = Image (model, "mechanics.AERHT", pgoparams, lp)
