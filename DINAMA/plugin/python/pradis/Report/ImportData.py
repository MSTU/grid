# -*- coding: cp1251 -*-
#import af
#import glb
import xlrd 
import string
from misc import *
from ParameterValues import *

class ImportData (ParameterValues):

	def __init__ (self, nl, pl, desc= misc.default):
		
		
		self.file_path = pl[0]
		self.file_format = pl[1]
		self.xcells = pl[2]
		self.ycells = pl[3]
		
		if self.file_path<>'':
			self.rb = xlrd.open_workbook(self.file_path, formatting_info=True)
#	далее закачка данных из файла и запись их в values в формате [x1,y1,x2,y2,..,xn,yn]		
			self.ix = self.readCells(self.xcells)
			if self.ycells <> '':
				self.iy = self.readCells(self.ycells)
				self.values = self.xy (self.ix, self.iy)
	
	def readCells(self, scells):
		self.values =[]
		if self.file_format == 'excel':
			xcells = '$'+scells+'\n'     #дополняю строку ограничивающими символами  для исключения частных случаев функции XYCells()
#			if self.ycells<>'':
#				ycells = '$'+self.ycells+'\n'
			
	   		def XYCells(str, symbol_of_begin='$',symbol_of_end='\n'):    #определям координаты ячейки
				str = string.upper(str)
				i=0
				col=0
				row=0
				degree1=0
				degree2=0
				letter=False
				digit=True
				while str[string.index(str,symbol_of_end)-1-i]!=symbol_of_begin:	
					if ord(str[string.index(str,symbol_of_end)-1-i])<=57 and ord(str[string.index(str,symbol_of_end)-1-i])>=48 and digit:
						a = int(str[string.index(str,symbol_of_end)-1-i])
						row+=a*10**degree1
						degree1+=1
#						print 'digit', row
						letter=True 
					elif ord(str[string.index(str,symbol_of_end)-1-i])<=90 and ord(str[string.index(str,symbol_of_end)-1-i])>=65 and letter:
						a = str[string.index(str,symbol_of_end)-1-i]
#						print 'string', a
						col += int((ord(a)-64)*26**degree2)
						degree2+=1
#						print col
						digit=False
					else: 
						print 'Error(1)'  #ошибка сообщяет, не влияет на работу. т.е. при asdafA5 будет брать только A5.
						break
					i+=1
				return col, row

			def Choice(str):	#4 варианта ввода: A1 , A1:A2, лист3!A1, лист3!A1:A2
				if string.find(str,'!')==-1 and string.find(str,':')==-1:
					return XYCells(str)+XYCells(str)   
				if string.find(str,'!')==-1 and string.find(str,':')!=-1:
					return XYCells(str,'$',':')+ XYCells(str,':')
				if string.find(str,'!')!=-1 and string.find(str,':')==-1:
					return XYCells(str,'!')+XYCells(str,'!')
				if string.find(str,'!')!=-1 and string.find(str,':')!=-1:
					return XYCells(str,'!',':') + XYCells(str,':')
    	
			x1,x2,x3,x4 = Choice(xcells)
			#y1,y2,y3,y4 = Choice(ycells)	
#			print x1,x2,x3,x4
	   		#print y1,y2,y3,y4

#	   		rb = xlrd.open_workbook(self.file_path, formatting_info=True)

			def NumSheet(str):  #номер листа
				if string.find(str,'!')!=-1:
					num_sheet=0
					i=0
					degree=0
					while str[i]!='!':
						if ord(str[string.index(str,'!')-1-i])<=57 and ord(str[string.index(str,'!')-1-i])>=48:
							a = (int(str[string.index(str,'!')-1-i]))*10**degree
							degree+=1
							num_sheet = a-1
						i+=1
				else: 
					num_sheet=0
				return num_sheet	
		
    	
			xsheet = self.rb.sheet_by_index(NumSheet(xcells))
			#ysheet = rb.sheet_by_index(NumSheet(ycells))
			if x2 == x4:       #строка
				xcells=[]
				for i in range(x3-x1+1):
					xcells += [xsheet.cell_value(x2-1,x1-1+i)]
				#print xcells
			elif x1 == x3:     #столбец
				xcells=[]
				xcells = xsheet.col_values(x1-1,x2-1,x4)
				#print xcells
			#if y2 == y4:        #строка
			#	ycells=[]
			#	for i in range(y3-y1+1):
			#		ycells += [ysheet.cell_value(y2-1,y1-1+i)]
				#print ycells
			#elif y1 == y3:        #столбец
			#	ycells=[]
			#	ycells = ysheet.col_values(y1-1,y2-1,y4)
				#print ycells       	
    	
			#for i in range(min(len(xcells),len(ycells))):   #срез по мин длине масива
			#	self.values+=[xcells[i],ycells[i]]
#			print 'xcells=',xcells
			
			return xcells
		
		if self.file_format == 'txt':
			f = open(self.file_path, 'r')
			c = []
			l=[]
			i=0
			c = f.readline()
			while c != [] :
				i += 1
				c = f.readline()
				l=string.split(c)
				if l==[]: break
				if (i>=int(self.xcells[2])) & (i <=int(self.xcells[4])):
					self.values=self.values+[l[int(self.xcells[0])-1],l[int(self.ycells[0])-1]]	
			print self.values
			f.close()
			return self.values
			
			
		
	def Values(self):
		return self.values		
			
	def diagram (self, iy):
		
		list = []
		y = iy.Values()
		for i in range (len(y)):
			list.append (self.values[i])
			list.append (y[i])
		
		return list

	def xy (self, ix, iy):
		
		list = []
		
		for i in range (len(iy)):
			list.append (ix[i])
			list.append (iy[i])
		
		return list
		
		
	def openWorkBook (self, filePath):
		self.rb = xlrd.open_workbook(filePath, formatting_info=True)
		return self.rb



