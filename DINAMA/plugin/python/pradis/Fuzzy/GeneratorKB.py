# -*- coding: cp1251 -*-
#import multi
#import misc


# Singleton
import fuzzy.System
import fuzzy.InputVariable
import os
import codecs

class GeneratorKB(object):

	def __init__ (self, system):
		
		self.system = system
		self.text = ''
	
	def save (self, path):
		
		file = open (path, 'w')
		file.write ( self.text)
	
	def add (self, path):

		os.system (os.getenv ('DINSYS') +'/DINAMA/pradis32/armdoc.exe -a ' + path)
	
	def download_template	(self):
		file = open (os.getenv ('DINSYS') +'/DINAMA/sysarm/fuzzy/fuzzy_template.xml', 'r')
		text = file.read()
		text = text.decode('utf8')
		
		return text
		
	def generate (self, name, description):
		
		self.text = self.download_template ()
#		description = self.system
		parameterlist = ""
		
		for varname1, value in self.system.variables.items():
			varname = varname1.decode ('cp1251')
			if isinstance(value, fuzzy.InputVariable.InputVariable):
				
				a = '		<parameter name="'+varname+'" type="" default="None"> \n \
				<description>\n\
					<russian>Четкое значение для '.decode ('utf8')+varname+'</russian>\n\
					<english></english>\n\
				</description>\n\
				</parameter>\n\
				'	
				
				list_adj = []
				
				for adj_name, adj_value in value.adjectives.items():
					list_adj.append (adj_name.decode ('cp1251'))
				
				b = '		<parameter name="'+varname+'_fuzzy" type="string" default="'+list_adj[0]+'"> \n \
					<description>\n\
					<russian>Нечеткое значение для '.decode ('utf8')+varname+' ['+', '.join (list_adj)+']</russian>\n\
					<english></english>\n\
					</description>\n\
					</parameter>\n\
					'	
				
				c = '		<parameter name="'+varname+'_morphology" type="string" default="None">  \n\
					<description>\n\
					<russian>Морфологическое значение для '.decode ('utf8')+varname+' [None, Very, NotVery, Less, Over, Not]</russian>\n\
					<english></english>\n\
					</description>\n\
					</parameter>\n\
					'	

				d = '		<parameter name="'+varname+'_priority" type="float" default="1.0">  \n\
					<description>\n\
					<russian>Приоритет для '.decode ('utf8')+varname+'</russian>\n\
					<english></english>\n\
					</description>\n\
					</parameter>\n\
					'	
				
				parameterlist += a+b+c+d#.decode ('utf8')# +b.decode ('utf8')+c.decode ('utf8')+d.decode ('utf8')
#				parameterlist = 'тест'.decode ('utf8') #unicode('тест', "cp1251")
#				print parameterlist
			
		e = '		<parameter name="KBfile" type="string" default="'+name+'"> \n \
				<description>\n\
					<russian>Название базы знаний</russian>\n\
					<english></english>\n\
				</description>\n\
				</parameter>\n\
				'.decode ('utf8')	
		f = '		<parameter name="ReportTemplate_File" type="string" default=""> \n \
				<description>\n\
					<russian>Файл шаблона отчета</russian>\n\
					<english></english>\n\
				</description>\n\
				</parameter>\n\
				'.decode ('utf8')	
		parameterlist = parameterlist + e + f
#		print self.text
#		self.text = self.text.encode("UTF-8")
#		self.text = self.text.decode ("cp1251")
		self.text = self.text.replace ('$name$', name) #.encode("cp1251"))
#		print self.text
#		description = description.decode ("cp1251")
#		parameterlist = parameterlist.encode ("cp1251")

#		parameterlist = parameterlist.encode ("UTF-8")
		description = description.decode('cp1251')
#		print description
		self.text = self.text.replace ('$description$', description)
		

		self.text = self.text.replace ('$parameterlist$', parameterlist)#.encode("cp1251"))
		self.text = self.text.encode('cp1251')

		
		return self.text

