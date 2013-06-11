class ContactForceModel:
	
	def __init__ (self, num, pl):
		self.Number = num
		self.pl = pl
		
	def GetList (self):
		par = self.pl
		par.insert (0, self.Number)
		return par