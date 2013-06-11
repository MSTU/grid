# -*- coding: cp1251 -*-
#import multi
#import af
#import glb
import misc
import os
import string
import math
from pradis.Report.ImportData import *
from ReportObject import *
from Curve import *
from pylab import *
import numpy
import matplotlib
import matplotlib.pyplot as plt
#import scipy
MaxValue = 1e36

# Объект Диаграма

class Diagram (ReportObject): # (multi.ModelLC):

	def __init__ (self, nl, pl, desc=misc.default):

		self.description = pl[0] 	# описание диаграммы (подпись)
		self.x  = pl[1]				# переменная оси x
		self.y = pl[2]  			# список кривых, reader-объектов, функций
		self.height=pl[3]			# высота картинки
		self.widht=pl[4]			# ширина картинки
		self.axisX= pl[5] 			# вид шкалы X
		self.axisY= pl[6]			# вид шкалы Y
		self.loclegend=pl[7]		# положеие легенды
		self.grid = pl[8]			# сетка
		       
       	    
		if desc != misc.default:
			self.name = desc
		else:
			self.name = ""
		
	
	def GetDiagram(self, fold):	
		
		if isinstance(self.x,Curve):
			self.x=self.x.GetStyle()[0]
		elif isinstance(self.x,ImportData):
			self.x=self.x.ImpData()
		
		if self.axisX=='log10':
			plt.semilogx()
		if self.axisY=='log10':
			plt.semilogy()
			
		for n in range(len(self.y)):		
			if isinstance(self.y[n],Curve):
				y, col, ls, lw, mark, lg= self.y[n].GetStyle()	
				#print self.x, y
				plt.plot(self.x, y, color = col, linestyle=ls, linewidth=lw, marker=mark, label=lg)
			elif isinstance(self.y[n],ImportData):
				y = self.y[n].ImpData()
				plt.plot(self.x,y)
			else:
				#print self.x,self.y[n]
				plt.plot(self.x,self.y[n])
			
		if self.grid=='yes': plt.grid(True)
		plt.legend(loc=self.loclegend.replace('_',' '))
		
		#поддержка кириллицы
		rcParams['font.serif']="Verdana, Arial"
		rcParams['font.sans-serif']="Tahoma, Arial"
		rcParams['font.cursive']="Courier New, Arial"
		rcParams['font.fantasy']="Comic Sans MS, Arial"
		rcParams['font.monospace']="Arial"
		
		#plt.xlabel(self.axisX)
		#plt.ylabel(self.axisY)
		
		plt.savefig(fold+self.description+'.png', dpi=100)
		plt.clf()
		return fold+self.description+'.png' 
		
	def data(self, fold, s, content, data):
		s.pict()
		content +='				<a href=\"#'+self.name+'\">Рисунок '+str(s.number_of_picture)+'. '+self.description+'</a><br>\n'
		data += '				<a name=\"'+self.name+'\"></a><br>\n				<IMG height="'+self.height+'" src=\"'+self.GetDiagram(fold)+'\"width="'+self.widht+'"/><br>\n 				<DIV class="diagram">Рисунок '+str(s.number_of_picture)+'. '+self.description+'</DIV><br>\n'
		return s, content, data

	