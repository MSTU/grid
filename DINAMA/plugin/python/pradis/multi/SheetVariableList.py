# -*- coding: cp1251 -*-
#import multi
import misc
from VariableList import *
import pradis.Report.ImportData
import pradis.multi.Variable
import pradis.multi.VariableLow

class SheetVariableList (VariableList):

	def __init__ (self, nl, pl, desc=misc.default):

		self.filePath = pl [0]

		data = pradis.Report.ImportData.ImportData ([], ['','excel','',''], 'data')
		data.openWorkBook (self.filePath)
		self.NameCells = data.readCells (pl[1])
		self.ValueCells = data.readCells (pl[2])
		self.MinCells = []
		self.MaxCells = []
		self.LowCells = []
		
		self.Low = pl [6]
		
#		print 'self.NameCells = ', self.NameCells
#		print 'self.ValueCells = ', self.ValueCells
		
		if len (self.NameCells) !=len (self.ValueCells):
			print 'ExcelVariableList: lengths are different'
			
			return
		
		if pl[3] !='' and pl[4] != '' and pl[5] !='':
			self.MinCells = data.readCells (pl[3])
			self.MaxCells = data.readCells (pl[4])
			self.LowCells = data.readCells (pl[5])
			
			if len (self.NameCells) !=len (self.MinCells):
				print 'ExcelVariableList: lengths are different'
				
				return
			
		self.Vars = []
		self.VarDict = dict()
		
		for i in xrange (len (self.NameCells)):
			name = desc+'.'+str(self.NameCells[i])
			if pl[3]!='':
				lowvar = pradis.multi.VariableLow.VariableLow ([],
					[self.LowCells[i], 0.0,0.0], desc = 'low.'+name)
				var = pradis.multi.Variable.Variable ([],
					[name, self.ValueCells[i], self.MinCells[i],self.MaxCells[i],[lowvar]], desc = name)
			else:
				var = pradis.multi.Variable.Variable ([],
					[name, self.ValueCells[i], None,None,[]], desc = name)
			
			self.Vars.append (var)
			
			
			self.VarDict [str(self.NameCells[i])] = var

#		print 'name=', self.NameCells
			
		if self.Low !='individual':
			lowvar = pradis.multi.VariableLow.VariableLow ([],
				[self.Low, 0.0,0.0], desc = desc+'.low')
			for i in self.Vars:
				i.Low = [lowvar]
			


	def Values(self):
		return self.Vars		

	def v0(self, name):
		return self.VarDict[name].Value0	
		