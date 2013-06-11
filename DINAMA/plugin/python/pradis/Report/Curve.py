# -*- coding: cp1251 -*-
#import multi
import misc

#import scipy

#from numpy import copy


# Кривая

class Curve: # (multi.ModelLC):

	colors = ['black', 'red', 'green', 'blue', 'magenta']
	symbols = ['None', 'circle','triangle','star','diamond','square','x']
	linestyles = ['Solid','Dash','Dot','DashDot']

#	thicknesses = [1,2,3,4,5]
	static_color = 0
	static_symbol = 0
	static_linestyle = 0
	static_thickness = 1
	
	@staticmethod
	def initStyle():
		Curve.static_color = 0
		Curve.static_symbol = 0
		Curve.static_linestyle = 0
		Curve.static_thickness = 1
	
	@staticmethod
	def generateStyle ():
		
		Curve.static_color += 1
		if Curve.static_color >=5:
			Curve.static_color = 0
			Curve.static_symbol += 1
		if Curve.static_symbol >=7:
			Curve.static_symbol = 0
			Curve.static_linestyle +=1
		if Curve.static_linestyle >=4:
			Curve.static_linestyle = 0
			Curve.static_thickness +=1

		return (Curve.colors[Curve.static_color], Curve.symbols[Curve.static_symbol], Curve.linestyles[Curve.static_linestyle], Curve.static_thickness)

	def __init__ (self, nl, pl, desc=misc.default):

#		self.ma = multi.ModelLC ()
		self.curve = pl[0]	  # кривая, reader-объект.критерий, функция
		self.legend= pl[1]    # легенда графика
		self.style = pl[2]    # стиль линии
		self.color = pl[3]    # цвет линии 
		self.thikness = pl[4] # толщина линии
		self.symbol = pl[5]   # вид маркера
		
		self.legend = self.legend.decode ('cp1251')
	    
	def GetStyle(self):
		linestyle=''
		color=''
		linewidth=0
		marker=''
		
		if self.style=='Solid': linestyle='-'
		elif self.style=='Dash': linestyle='--'
		elif self.style=='Dot': linestyle=':'
		elif self.style=='DashDot': linestyle='-.'
		
		color = self.color
		
		if self.thikness == '1px': linewidth=1
		elif self.thikness=='2px': linewidth=2
		elif self.thikness=='3px': linewidth=3
		elif self.thikness=='4px': linewidth=4
		elif self.thikness=='5px': linewidth=5
		elif type(self.thikness) == int: 
#			print '***',self.thikness
			linewidth = self.thikness
		
		if self.symbol=='None': marker='1'
		elif self.symbol=='circle': marker='o'
		elif self.symbol=='triangle': marker='^'
		elif self.symbol=='star': marker='*'
		elif self.symbol=='diamond': marker='D'
		elif self.symbol=='square': marker='s'
		elif self.symbol=='x': marker='x'
		
		#print self.curve, linestyle, color, linewidth, marker
		return self.curve, color, linestyle, linewidth, marker, self.legend
#		if desc != misc.default:
#			self.ma.SetScheme(desc)
#			self.ma.SetDescription('Report: '+desc)

	
		

		
	
		