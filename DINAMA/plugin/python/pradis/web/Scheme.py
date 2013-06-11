# -*- coding: cp1251 -*-

from  pradis.web.Sysarm import *
from  pradis.web.Component import *




class Scheme:

	def __init__(self):

		self.componentList = []
		
#		self.parameterList["schemeName"] = "default"
#		self.parameterList["homeDir"] = "."

	# системная папкп решателя
		self.systemDir = systemDir
		
	# системная папка web сервера
		self.webDir = webDir

	
		self.schemeName = "default"
		self.homeDir = "."
		

#	dynamic parameters
		self.parameterList = dict()
		self.parameterList["author"] = ""
		self.parameterList["creationDate"] = "07.11.2012:00.00.00"
		self.parameterList["changeDate"] = "07.11.2012"
		
		# 	
	def solve(self):
	
		self.writelogs()
			
		
		return 0

#	get report path		
	def report(self):
	
		return "Report1.html"

	def addComponent(self, comp):
		self.componentList.append (comp)
		
#	set dynamic parameter		
	def set (self, name, value):
		self.parameterList[name] = value
	
#	get dynamic parameter
	def get (self, name):
		return self.parameterList[name] 
	
	def init(self):
	
		
		pass
	
	# записать логи	
	def writelogs (self):
		f=open(self.homeDir+'/log.txt', 'w')
		
		text = ""
		text +=  "schemeName = "+ self.schemeName
		
		text += "\nhomeDir = "+ self.homeDir
		
		for k, i in self.parameterList.iteritems():
			text += "\n"+k+" = "+str(i)
		
		for  i in self.componentList:
			text += "\n"+str(i)
		
		print>> f, text
		f.close()
		
		fr=open(self.webDir+'/report.html', 'r')
		report = fr.read()
		text = text.replace ("\n", "<p>")
		report = report.replace ("#content#", text)
		
	# замена переменных в шаблоне	
		for k, i in self.parameterList.iteritems():
			print k, i
		
			report = report.replace ("#"+k+"#", str(i))
			
	# открыть файл отчета 
		#schemeName
		fw=open(self.homeDir+'/Report1.html', 'w')
		print>> fw, report
		
		fw.close()

	
	
	