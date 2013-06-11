# -*- coding: cp1251 -*-
#import multi
import af
import glb
import misc
import os
import math
import string
from ReportObject import *
#import scipy

#from numpy import copy



class prettyfloat(float):
	format = '%.3f'
	
	@staticmethod
	def defaultFormat():
		format = '%.3f'
		
	def __repr__(self):
#		if type(self) == float:
		return prettyfloat.format % self
#		else:
#			return str(self)

# Объект Таблица

class Table (ReportObject):

	def __init__ (self, nl, pl, desc=misc.default):

		self.description = pl[0]  # описание таблицы (подпись)
		self.values = pl[1] 	  # значения таблицы (построчно) 
		
		if desc != misc.default:
			self.name = desc
		else:
			self.name = ""
			
	def GetTable(self):
		tr=''
#		print self.values
		for m in self.values:
			td=''
#			print m
			for i in m:
#				print i
				td =td+'<td>'+Table.formatPrint(i)+'</td>'
#				td =td+'<td>'+str(i)+'</td>'
			tr=tr+'<tr>'+td+'</tr>'
		return tr
		#for m in range(string.count(self.values,';')):
		#	td=''
		#	mval = self.values[:string.find(self.values,';')].split(',')
		#	for i in range(string.count(self.values[:string.find(self.values,';')],',')):
		#		td = td +'<td>'+mval[i]+'</td>'
		#	tr=tr+'<tr>'+td+'</tr>'
		#	self.values=self.values[string.find(self.values,';')+1:]
		#return tr
		

	def data(self, fold, s, content, data):
		s.table()
#		print s
		content +='				<a href=\"#'+self.name+'\">Таблица '+str(s.number_of_tables)+'. '+self.description+'</a><br>\n'
		data += '				<a name=\"'+self.name+'\"></a><br>\n				<table>'+self.GetTable()+'</table>\n				<DIV class="table">Таблица '+str(s.number_of_tables)+'. '+self.description+'</DIV><br>\n'
		return s, content, data
	
				
	@staticmethod
	def formatPrint (x):
		if type(x) == dict:
			y=dict()
			txt = ''
			for key,item in x.items():
				nkey = key.decode ('cp1251')
				if type(item) == float:
					y[nkey]= prettyfloat(item)
					txt += nkey +':'+ str (prettyfloat(item))+'<br>'
#					print key, x[key]
				else:
					y[nkey]= item
					txt +=  nkey +':'+ str (item)+'<br>'
				
			return txt.encode ('cp1251')
		elif type(x) == float:
			y = prettyfloat(x)
			return prettyfloat.format % y
#			return str(y)
		return str(x)



