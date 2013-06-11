# -*- coding: cp1251 -*-
#import multi
import af
import glb
import misc
import os
import math
import string
import shutil


lskeys = []
#aLauncher=Launcher([],[])	

lsdyna_bat = 'lsdyna.bat'


def add_key (k):
	lskeys.append (k)


# Генератор и запускатель k файла 
			
class Launcher: # (multi.ModelLC):

	def __init__ (self, nl, pl, desc=misc.default):

#		self.ma = multi.ModelLC ()
		
		
		self.keys  = pl[0]	# список ключей 
		self.Output_File = pl[1] # .k файл 
		self.Title = pl[2]	# заголовок 
		self.Keyword = pl[3]	# ключ keyword
		data=self.data ()

		if desc != misc.default:
			self.name = desc
			
		pradis32=os.getenv('dinsys')+'/DINAMA/pradis32'

		f=open(self.Output_File,'w')
		
		for i in lskeys:
			data = i.data(data)
		
		data +='*END\n'
		f.write(data)
		
		misc.solverName = ''
		misc.postName = ''
		
#		os.spawnve(os.P_WAIT, misc.solverName, [pradis32+lsdyna_bat, self.Output_File], os.environ) 
		
	def data (self):
		s = '*KEYWORD\n*TITLE\n'+self.Title+'\n'
		return s
	
	def Run (self):
		pass

	
#Launcher aLauncher = Launcher ()