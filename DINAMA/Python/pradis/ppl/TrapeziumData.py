class TrapeziumData:
	
	def __init__ (self, min, max, t0, t1, t2, t3):
		self.min = min
		self.max = max
		self.t0 = t0 
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		
	def GetList (self):
		return [self.min, self.max, self.t0, self.t1, self.t2, self.t3]
		