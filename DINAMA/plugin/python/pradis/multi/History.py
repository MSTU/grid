# -*- coding: cp1251 -*-

#mport glb
#mport misc
#mport os

class History :

	def __init__ (self):

		self.column = []
		self.flc = []
		self.values = dict()
		self.scheme =""
		self.desc = ""
		self.fl = ""
		
	def SetScheme(self, desc):
		self.scheme = desc
		
	def SetDescription(self, desc):
		self.desc = desc
		
		
	def SetLoadcasesCriteria (self, fl):
		self.flc = []
		
		for i in fl:
			for j in i.criteria:
#				print 'flc=', i.Name+"."+j+"|"
				cr = j.strip()
				if cr!=" " and cr!="":
					self.flc.append (i.Name+"."+j)

		
	def initHistory(self):
		self.values = dict()

		fdOUT = open(self.GetHistoryFile(),"w");

		print >>fdOUT, self.desc
		print >>fdOUT
		name = "Iteration"
		line  = name.ljust(41)
		
		for i in self.column:
			name = i.ljust(41)
			line = line + name
		
		for i in self.flc:
			name = i.ljust(41)
			line = line + name
		
		print >>fdOUT, line
		fdOUT.close()
	
	def AddExtParameter (self,name):
		self.column.append (name)
	
	def SetExtParameterValue (self,j, value):
		self.values [str(j)] = value

		
	# установка значений критериев Loadcase
	def SetLoadcaseValue (self,ma):
		for j in self.flc:
			self.values [str(j)] = ma.f(j)

		print ma.GetResult()
		
	def GetHistoryFile(self):
		return self.scheme + ".hst"
		
	def writeHistory(self, iteration):

		fdOUT = open(self.GetHistoryFile(),"a");
###########	
		line  = str(iteration).ljust(41)
		
#		print 'History:'
#		print self.column
#		print self.values
		
		
		for i in self.column:
			
			name = str(self.values[i]).ljust(41)
			line = line + name
		
		for i in self.flc:
			name = str(self.values[i]).ljust(41)
			line = line + name

		
		
		print >>fdOUT, line
		fdOUT.close()

		


