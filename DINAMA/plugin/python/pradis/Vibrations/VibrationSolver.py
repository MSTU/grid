# -*- coding: cp1251 -*-
#import multi
import af
import glb
import misc
import os
import math

#import scipy

#from numpy import copy




class VibrationSolver:# (multi.ModelLC):

	def __init__ (self, nl, pl, desc=misc.default):

#		self.ma = multi.ModelLC ()

		self.method = pl[0]
		self.ice = pl[1]
		self.mounts  = pl[2]
		self.locations  = pl[3]
		self.report  = [pl[4]] # ???
		
		
#		if desc != misc.default:
#			self.ma.SetScheme(desc)
#			self.ma.SetDescription('VibrationSolver: '+desc)

	
#		fl = misc.Expand (fl)
		
		
#		for i in self.names:
#			self.ma.AddParameter (str(i)+'.Mean')
#			self.ma.AddExtParameter (str(i)+'.Mean')
		
#		self.createNormX()		
		
		
		self.Run()
		self.generateReports()
		misc.SetSolver ("")
		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")
		
#		misc.SetPostFile(self.ma.GetHistoryFile())
					
			
	def generateReports(self):
		for i in self.report:
			# установаить свойства отчета
			# ...
		
			i.Run ()
	
	
	
	def Run (self):
		"""				
		self.ma.SetFilePostfix ('.vibration')
		self.ma.initHistory()

		
		if self.method == 'point':
			j = 0
			for i in self.samples:
				y  = 777 #mean (i)
# mean calculation y=mean(x)	
				print 'y=',y
				self.ma.SetParameterValue (j, str(y))
				self.ma.SetExtParameterValue (j, str(y))
				j = j+1
			
			self.ma.writeHistory(0)
		else:
			nlayers = len(self.samples[0])
			
# создать список list из nlayers пустых элементов			
			
			for k in xrange (nlayers):
				j = 0
				for i in self.samples:
					y  = 777 #mean (i[0:k])
# mean calculation y=mean(x)	
					self.ma.SetParameterValue (j, str(y))
					self.ma.SetExtParameterValue (j, str(y))
					j = j+1
				self.ma.writeHistory(k)
				
		"""		
