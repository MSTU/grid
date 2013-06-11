# -*- coding: cp1251 -*-
#import multi
import af
import glb
import misc
import os
import math

#import scipy

#from numpy import copy



# Читатель  из файлов DAT, hst,  xls, txt и прочее

class Reader: # (multi.ModelLC):

	def __init__ (self, nl, pl, desc=misc.default):

#		self.ma = multi.ModelLC ()
		self.file = pl[0]		# путь к файлу из которого берем данные
		
		# ? задавать ли имена критериев, которые читаем из файла? или другие параметры?
	
		

		
		
		self.Run()
#		misc.SetSolver ("")
#		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")
		
#		misc.SetPostFile(self.ma.GetHistoryFile())
					
				
	def Run (self):
	
		# читаем файл в:
		values = [0,0,1,1]
		curve = Curve ([], [values, 'style', 'red', '1', 'none'], desc = 'curve name')
		self.curves['curve name'] = curve # пример кривой
	
		pass
		
	def f (self, name, layer = -1):
	
		# возвращает значение критерия name на слое layer (если -1, то на последнем слое)
	
		return 0.0