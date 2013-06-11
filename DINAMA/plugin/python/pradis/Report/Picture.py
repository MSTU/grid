# -*- coding: cp1251 -*-
#import multi
import af
import glb
import misc
import os
import math
import shutil
from ReportObject import *

#import scipy

#from numpy import copy



MaxValue = 1e36

# Объект Картинка

class Picture(ReportObject): # (multi.ModelLC):

	def __init__ (self, nl, pl, desc=misc.default):

		
		self.description = pl[0]  # описание картинки (подпись)
		self.file  = pl[1]		  # путь к файлу картинки
		self.height = pl[2]		  # высота изображения
		self.widht = pl[3]		  # ширина изображения

	
		if desc != misc.default:
			self.name = desc
		else:
			self.name = ""
	
	def GetPicture(self, fold):
		format_of_file=self.file[self.file.rfind('.'):]
		shutil.copyfile(self.file,fold+'image_'+self.name[-1]+format_of_file)
		return fold+'image_'+self.name[-1]+format_of_file
	
	def data(self, fold, s, content, data):
		s.pict()
		content +='				<a href=\"#'+self.name+'\">Рисунок '+str(s.number_of_picture)+'. '+self.description+'</a><br>\n'
		data += '				<a name=\"'+self.name+'\"></a><br>\n				<IMG height="'+self.height+'" src=\"'+self.GetPicture(fold)+'\"width="'+self.widht+'"/><br>\n				<DIV class="picture">Рисунок '+str(s.number_of_picture)+'. '+self.description+'</DIV><br>\n'
		return s, content, data
	
		
				