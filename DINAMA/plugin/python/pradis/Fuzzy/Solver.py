# -*- coding: cp1251 -*-

import constants as constants
import misc
#global Solvers = dict()


from pradis.Fuzzy.System  import System 
from pradis.Fuzzy.GeneratorKB import GeneratorKB
import pradis.Fuzzy.System
#import pradis.Fuzzy.Report as Report
from fuzzy.Adjective import Adjective
from fuzzy.norm.AlgebraicProduct import AlgebraicProduct
from fuzzy.norm.Min import Min
import pradis.Fuzzy.Adjective
import fuzzy.operator.Compound 
import fuzzy.operator.Input

import os

class Solver:

	def __init__(self, nl, pl, desc = constants.default):#, KBfile = None):
#		pl = misc.unpackDataFromList(pl)
#		pl = misc.Expand(pl)

#		import pradis.splitters.Point2XYZs

		self.RulesList = pl[0] 
		
		self.InputList = pl[1]
		self.OutputList = pl[2]
		
		self.Report = pl[3]

		self.name = pl[4]
		self.description = pl[5]
		
#		input_list = dict()
#		for i in self.InputList:
#			input_list[i.Name] = i.Value
#			input_list.append (i.variable)

		"""
		output_list = dict()
		for i in self.OutputList:
			output_list[i.Name] =  0.0
		"""
		
		path = os.getenv('DINSYS') + '/DINAMA/sysarm/fuzzy/kb/'
#		if KBfile <> None:
#			Solver.loadController (path + KBfile+'.pickle')
		
		output_list = self.generateOutputVariableList ()

		self.calculate(input = self.InputList, output = output_list)
#		print 'solver report = ', output_list
		self.Report.reportAllVariables()
		
		if (self.name <> ''):
			self.saveKB()
			self.saveController (path + self.name+'.pickle')
		
#		self.Report.report (input_list)
#		self.Report.report (output_list)
        # hold old value if no results in next calculations
#        self.system.variables['a'].defuzzify.failsafe = 0 #output['a']

	#	misc.SetPost ():
	#	self.Report.openBrowser()
	
		misc.SetPost ('')
		misc.SetSolver('')

 
	def generateOutputVariableList (self):
		sys = System().system
		out_var_list = dict()
		for name, variable in sys.variables.items():
			if isinstance (variable, fuzzy.OutputVariable.OutputVariable):
				out_var_list[name] =  0.0
		
		return out_var_list
 
	def calculate(self,input,output):
		"""Do a complete fuzzy calculation step.
		The input dictionary contains the input values for the named variables.
		The output dictionary serves as container and provides the names of the
		variables to read."""
		sys = System().system
		sys.reset()

		self.fuzzify(sys,input)

		sys.inference()

		sys.defuzzify(output)

		return output

	def deffuzzify_fuzzify (self, variable, adj):
		import fuzzy.operator.Input
		a = fuzzy.operator.Input.Input(adj)
		delta  = 1e-6*(variable.max - variable.min)
		b = fuzzy.operator.Input.Input( pradis.Fuzzy.System.helper (fuzzy.set.Polygon.Polygon([(variable.min,0.),(variable.min+delta,1.),(variable.max, 1.0),(variable.max+delta, 0.0)]))
													)
					#fuzzy.operator.Const.Const(1.0)
		op = fuzzy.operator.Compound.Compound(Min(), a, b)
		set2 = pradis.Fuzzy.System.operate(op)
#					new_adjective = Adjective (set2.set)	
#					new_name = '.'+i.Adjective.Name 
#					variable.adjectives[new_name] = new_adjective
		f_value = set2.set.getCOG()
#		print f_value
		
		return f_value
		
		
	def fuzzify(self,sys,input):
		"""Fuzzify the inputs.
		   Фаззификация через дефаззификацию"""

#		input_list = dict()
		for i in input:
#			input_list[i.Name] = i.Value
			variable = sys.variables[i.Name]
			
			if i.fuzzy_flag: # fuzzy value
				
				if isinstance(i.Adjective, pradis.Fuzzy.Adjective.Adjective):
#					print 11111, i.Adjective.Name
					value = self.deffuzzify_fuzzify (variable, i.Adjective.adjective)
				if isinstance(i.Adjective, fuzzy.Adjective.Adjective):
#					print 11111, i.Adjective.Name
					value = self.deffuzzify_fuzzify (variable, i.Adjective)

				else: #if isinstence(self.Adjective, fuzzy.operate.operate):
#					print 22222, i.Adjective
					set = pradis.Fuzzy.System.operate(i.Adjective)
					value = self.deffuzzify_fuzzify (variable, set)
#					f_value = set.set.getCOG()
#					print value
					adjective = Adjective (set.set)	
					name = '.'+i.Name
					variable.adjectives[name] = adjective
					self.debugPlot(variable)
					
				variable.setValue(value)
#				print 'value = ' , variable.getValue()
				
			else:
				variable.setValue(i.Value)
		
		
	def fuzzify_1(self,sys,input):
		"""Fuzzify the inputs.
		   Фаззификация по всем кривым"""

#		input_list = dict()
		for i in input:
#			input_list[i.Name] = i.Value
			variable = sys.variables[i.Name]
			
			if i.fuzzy_flag: # fuzzy value
				value = dict()
				if isinstance(i.Adjective, pradis.Fuzzy.Adjective.Adjective):
#					print 11111, i.Adjective.Name
					value[i.Adjective.Name] = i.Adjective.adjective
#					value = self.deffuzzify_fuzzify (variable, i.Adjective.adjective)

				else: #if isinstence(self.Adjective, fuzzy.operate.operate):
#					print 22222, i.Adjective
					set = pradis.Fuzzy.System.operate(i.Adjective)
					f_value = set.set.getCOG()
					print f_value
					
					adjective = Adjective (set.set)	
					name = '.'+i.Name
										
					for name_adj, adj in variable.adjectives.items():
						op = fuzzy.operator.Compound.Compound (adj.COM, fuzzy.operator.Input.Input(adj), fuzzy.operator.Input.Input(adjective))
						set2 = pradis.Fuzzy.System.operate(op)
						
						new_adjective = Adjective (set2.set)	
						new_name = '.'+name_adj 
						
						variable.adjectives [new_name] = new_adjective
						value[new_name] = new_adjective
						
						
					variable.adjectives[name] = adjective
					value[name] = adjective
					
				variable.setValue(value)
				
				#############
				from fuzzy.norm.AlgebraicSum import AlgebraicSum
				import fuzzy.defuzzify.COG
				INF = AlgebraicProduct()
				ACC = AlgebraicSum()
				COM = AlgebraicSum()
				CER = AlgebraicProduct()
    		
				defuzzify  = fuzzy.defuzzify.COG.COG(INF=INF,ACC=ACC,failsafe = variable.min)				
				
				print 'defuzzify = ', defuzzify.getValue(variable)
					##### plot debug
				
				self.debugPlot(variable)
					##### print debug
					
				
				
			else:
				variable.setValue(i.Value)

	def debugPlot (self, var):
		x_min = var.min
		x_max = var.max
		d_list = []
		for name, adj in var.adjectives.items():
			if name.startswith ('.'):
				d_list.append ( (fuzzy.operator.Input.Input(adj), name) ) 
		if len(d_list)>0:
			self.Report.setExtDiagrams ([(d_list,  x_min, x_max)])

 
	def saveController(self, filename):
		
		import cPickle
		file = open(filename,"wb")
		cPickle.dump(System().system,file,1)
		file.close()

	@staticmethod
	def loadController(filename):
		
		import cPickle
		file = open(filename,"rb")
		System().system = cPickle.load(file)
		file.close()
		
		
	def saveKB(self):
		
		gen = GeneratorKB (System().system)
		
		text = gen.generate (self.name, self.description)
		
		path = self.name+'.xml'
		gen.save (path)
		gen.add (path)
#		raw_input()
		
		

		
		
	
		
		
		
		
		