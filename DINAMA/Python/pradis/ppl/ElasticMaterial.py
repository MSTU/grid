class ElasticMaterial:

	def __init__ (self, m, k, r):
		self.l = [m, k, r]
		
	def GetList (self):
		return self.l
		