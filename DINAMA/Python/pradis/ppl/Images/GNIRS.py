from Image import *

class GNIRS (Image):
	def __init__ (self, model, pgoparams, lp):
		self.this = Image (model, "mechanics.GNIRS", pgoparams, lp)
