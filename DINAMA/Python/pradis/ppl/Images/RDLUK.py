from Image import *

class RDLUK (Image):
	def __init__ (self, model, pgoparams, lp):
		self.this = Image (model, "mechanics.RDLUK", pgoparams, lp)
