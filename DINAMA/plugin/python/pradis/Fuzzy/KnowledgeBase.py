# -*- coding: cp1251 -*-

import constants as constants
import misc
#global Solvers = dict()


from pradis.Fuzzy.System  import System 
import pradis.Fuzzy.Parameter 
import pradis.Fuzzy.Report
import pradis.Fuzzy.Solver
from pradis.Fuzzy.GeneratorKB import GeneratorKB
import pradis.Fuzzy.System
#import pradis.Fuzzy.Report as Report
from fuzzy.Adjective import Adjective
from fuzzy.norm.AlgebraicProduct import AlgebraicProduct
from fuzzy.norm.Min import Min
import pradis.Fuzzy.Adjective
import fuzzy.operator.Compound 
import fuzzy.operator.Input

import sysarm as Sysarm

import os

class KnowledgeBase:

	def __init__(self, nl, pl, desc = constants.default):

		n = len (pl)
		nvar = int (n/4)  # по 4 параметра на каждую переменную
		nadd = nvar * 4   # с этого номера начинаются дополнительные параметры объекта
		
		self.KBfile = pl[nadd] 
		self.ReportTemplate = pl [nadd+1]
		
		par_list = self.generate_parameter_list (pl, nvar)
		
		report = pradis.Fuzzy.Report.Report ([], [self.ReportTemplate, None, []], desc = desc)
		pl_solver = [[], par_list, [], report, '','']
		solver = pradis.Fuzzy.Solver.Solver ([], pl_solver)#, KBfile = self.KBfile)
		

	def generate_parameter_list (self, pl, nvar):
		
		par_list = []
		model = self.loadKB ()
		
		for i in range (nvar):
			
			name = model.GetParameterName(i*4)
			desc = model.GetParameterRuDescription(i*4)
			
			adj = self.createAdjective (name, pl[i*4+1], pl[i*4+2], pl[i*4+3])
			
			par = pradis.Fuzzy.Parameter.Parameter ([], [name, desc, pl[i*4], adj], desc = name)
			par_list.append (par)
			
		return par_list

	def createAdjective (self, var_name, adj_name, morph, priority):
		sys = System().system
		variable = sys.variables[var_name]
		adj = variable.adjectives[adj_name]
		
		return self.createMorph (adj, morph)
		
	def createMorph (self, adj, morph):
		import pradis.Fuzzy.base
		if morph == 'None':
			return adj
		if morph == 'Very':
			return pradis.Fuzzy.base.Very (adj)
		if morph == 'NotVery':
			return pradis.Fuzzy.base.NotVery (adj)
		if morph == 'Over':
			return pradis.Fuzzy.base.Over (adj)
		if morph == 'Less':
			return pradis.Fuzzy.base.Less (adj)
		if morph == 'Not':
			return pradis.Fuzzy.base.Not (adj)



			
	def loadKB(self):
		obj = Sysarm.PythonObject ()
#		sysarm = Sysarm.Sysarm ()
		path = os.getenv ('DINSYS')+'/DINAMA/sysarm/'
		xmldata = open (path + 'XML/KnowledgeBases/Object/'+self.KBfile+'.xml', 'r').read()
		sr = Sysarm.SysarmReader ()
#		sr.Read('',sysarm)
		sr.ReadObject (xmldata, obj)
	
		pradis.Fuzzy.Solver.Solver.loadController (path + 'fuzzy/kb/'+self.KBfile+'.pickle')
	
		return obj
		
	