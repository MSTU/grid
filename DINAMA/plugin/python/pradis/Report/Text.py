# -*- coding: cp1251 -*-
#import multi
import af
import glb
import misc
import os
import math
from ReportObject import *

#import scipy

#from numpy import copy



MaxValue = 1e36

# Объект Текст

class Text(ReportObject): # (multi.ModelLC):

	def __init__ (self, nl, pl, desc=misc.default):

		self.Type = pl[0]		  # тип текста
		self.description = pl[1]  # описание текста (заголовок)
		self.text  = pl[2]	      # текст
	

		if self.Type=='Text':
			self.name=''
		else:
			self.name=desc
	
	def data(self, fold, s, content, data):
		if self.name=='':
			data += '				<DIV class="txt">'+self.text+'</DIV>\n'
		else:
			s.chap()
			content +='				<a href=\"#'+self.name+'\">'+str(s.number_of_chapter)+'. '+self.description+'</a><br>\n'
			data += '				<a name=\"'+self.name+'\"></a><br>\n				<h3 class="chap">'+str(s.number_of_chapter)+'. '+self.description+'</h3>\n				<DIV class="txt">'+self.text+'</DIV><br>\n'
		return s, content, data
	