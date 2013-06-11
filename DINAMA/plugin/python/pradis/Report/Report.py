# -*- coding: cp1251 -*-
#import multi
import af
import glb
import misc
import os
import math
import string
import shutil

#import scipy

#from numpy import copy



MaxValue = 1e36

# Генератор отчета
class Content:
	def __init__ (self, pict, chap, tables):	
		self.number_of_picture = pict
		self.number_of_chapter = chap
		self.number_of_tables = tables
	def pict(self):
		self.number_of_picture += 1
	def table(self):
		self.number_of_tables += 1
	def chap(self):
		self.number_of_chapter += 1
			
class Report: # (multi.ModelLC):

	def __init__ (self, nl, pl, desc=misc.default):

#		self.ma = multi.ModelLC ()
		
		
		self.objects  = pl[0]		# список объектов отчета
		self.Template_File = pl[1]  # файл шаблона
		self.viewType = pl[2]		# тип отчета (html, rtf, pdf, ...)
		self.Header = pl[3]			# заголовок 
		self.description = pl [4]   # описание отчета
		self.TextStyle=pl[5]		# Стиль текста в отчете
	
		m=0
		s=Content(0,0,0)
		data=''
		content=''

		if desc != misc.default:
			self.desc = desc
		else:
			self.desc = 'report'
		self.report_file = self.desc+'.html'
		
		sysarm=os.getenv('dinsys')+'/DINAMA/sysarm'
		fold=self.MakeDir()
		if self.Template_File=='':
			f=open(sysarm+'/web/report.html', 'r')
		else:
			f=open(self.Template_File,'r')
		flines = f.readlines()
		f.close()
		
		f=open(self.report_file,'w')
		
		
		
		for i in self.objects:
			s, content, data = i.data(fold, s, content, data)
		
		for s in flines:	
			if string.find(s,'#data#')!=-1:
				flines[m]=data
			if string.find(s,'#content#')!=-1:
				flines[m]=content
			if string.find(s,'#title#')!=-1:
				flines[m]='		<title>'+self.Header+'</title>\n'
			if string.find(s,'<LINK ')!=-1:
				flines[m]='		<LINK href="'+self.report_file+'.files/style.css" type="text/css" rel="stylesheet"/>\n'
			if string.find(s,'logo_ru')!=-1:
				flines[m]='								<img src="'+self.report_file+'.files/logo_ru.gif" align="left" alt="ЛАДУГА" width="203" height="68" hspace="0" vspace="0" border="0"/>\n'
			if string.find(s,'#Header#')!=-1:
				flines[m]='				<h2><center>'+self.Header+'</center></h2>\n				<p id="report">'+self.description+'</p>\n				<h3>Содержание</h3>\n'
			if string.find(s,'#TextStyle#')!=-1:
				if self.TextStyle!='':
					flines[m]=self.TextStyle.GetTextStyle()
				else:
					flines[m]='			<DIV>'
			m+=1		
		f.writelines(flines)
		f.close()
		
	def MakeDir(self):
		try:
			dir_name = self.report_file+'.files/'
			if not (os.access (dir_name, os.R_OK) ):
				os.makedirs(dir_name)
			sysarm=os.getenv('dinsys')+'/DINAMA/sysarm/web'
			shutil.copyfile(sysarm+'/image/style.css',dir_name+'style.css')
			shutil.copyfile(sysarm+'/image/logo_ru.gif',dir_name+'logo_ru.gif')
			shutil.copyfile(sysarm+'/image/left_margin.gif',dir_name+'left_margin.gif')
		except OSError as detail:
			print 'pradis.Report.Report: exception:', detail
		return dir_name 
		
	def Run (self):
		pass
		