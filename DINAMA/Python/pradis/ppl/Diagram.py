class Diagram:
	def __init__ (self, x, y):
		self.xlist = [x]
		self.ylist = [y]
	
	def Add (self, x, y):
		i = len (self.xlist) - 1
		while self.xlist [i] > x and i >= 0:
			i = i - 1
		else:
			self.xlist.insert (i + 1, x)
			self.ylist.insert (i + 1, y)
			
	def AddList (self, l):
		i = 0
		while i+2 <= len(l):
			self.Add (l[i], l[i+1])
			l = l + 2
			
	def GetTable (self):
		tbl = []
		for i in range (len (self.xlist)):
			tbl.append (self.xlist[i])
			tbl.append (self.ylist[i])
		return tbl
