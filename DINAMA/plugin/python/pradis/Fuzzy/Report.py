# -*- coding: cp1251 -*-

import constants as constants
import os

import pradis.Report.Report
import pradis.Report.Table
import pradis.Report.Curve
import pradis.Report.Diagram
from pradis.Fuzzy.System import System as System
import pradis.Fuzzy.System
import sys
import fuzzy.doc.structure.dot.dot
import fuzzy.InputVariable

import sys, os
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])),os.path.pardir))

try:
	# If the package has been installed correctly, this should work:
	import Gnuplot, Gnuplot.funcutils
except ImportError:
	print "Sorry, you need Gnuplot.py (http://gnuplot-py.sourceforge.net) to use this."
	sys.exit(1)


class Report:

	Appendix_count = 0
	def __init__(self, nl, pl, desc = constants.default):
#		pl = misc.unpackDataFromList(pl)
#		pl = misc.Expand(pl)
		self.desc = desc
		Report.Appendix_count = 0
#		import pradis.splitters.Point2XYZs

		self.Template_File = pl[0]

		self.Class = pl[1]

		self.px = '600'
		self.py = '800'
		self.steps = 100
		self.extDiagramm   = []
		# hold old value if no results in next calculations
#		System().variables['a'].defuzzify.failsafe = 0 #output['a']
		self.setExtDiagrams (pl [2])

	def setExtDiagrams(self, d_list):
		
		for i in d_list:
			Report.Appendix_count+=1
			(c, x_min, x_max) = i
			if type(c) == tuple:
				(s, name) = c
				adj = pradis.Fuzzy.System.operate(s)
				self.addExtDiagram(adj, x_min, x_max, name)
			if type(c)==list:
				c_list = []
				xi = self.generateXi (x_min, x_max)
				for i in c:
					(s, name) = i
					adj = pradis.Fuzzy.System.operate(s)
					Curve1 = self.plotAdjective (adj,x_min,x_max, name)
					c_list.append (Curve1)

				Diagram1 = pradis.Report.Diagram.Diagram([], ['Appendix '+str(Report.Appendix_count), xi, c_list, self.px, self.py, 'linear', 'linear', 'upper_right', 'yes'], desc = 'Appendix')
				self.extDiagramm.append(Diagram1)	
				

	def openBrowser():
		pass

	def reportAllVariables (self):

#		print 'report:'#, output
		for name,result in System().system.variables.items():
#			print name, '=', result
			self.printVariable(name)
#			self.plotVariable(name)
		report_file = self.writeHTML()
		import webbrowser
		url = 'file://'+os.path.realpath(report_file)
		webbrowser.open(url)

#		raw_input()

	def report (self, output):

#		print 'report:'#, output
		for name,result in output.items():
#			print name, '=', result
			self.printVariable(name)
			self.plotVariable(name)
		#print 'rules:'
		"""
		for name,rule in System().system.rules.items():
			print name, rule
			f=sys.stdout
			fuzzy.doc.structure.dot.dot.print_header(f,"XXX")
			fuzzy.doc.structure.dot.dot.print_dot(rule,f,System().system,"")
			fuzzy.doc.structure.dot.dot.print_footer(f)
		"""
		"""
		if self.Class==None:
			self.write ('', self.Template_File)
#			self.createDoc (self.Template_File)
#			self.createDot (self.Template_File)
		elif not( callable(self.Class)):
			self.createDoc (self.Template_File)
		else:
			self.Class (output, self.Template_File)
		"""
	def writeHTML(self):

		pradis.Report.Curve.Curve.initStyle()
		#TextStyle1 = pradis.Report.TextStyle.TextStyle([], ['Arial', '100%'])
		table1 = self.generateVariablesTable ('InputVariables', fuzzy.InputVariable.InputVariable)
		diagrams1 = self.generateVariablePics (fuzzy.InputVariable.InputVariable)
		diagrams2 = self.generateVariablePics (fuzzy.OutputVariable.OutputVariable)
		diagrams3 = self.extDiagramm
		table2 = self.generateVariablesTable ('OutputVariables', fuzzy.OutputVariable.OutputVariable)

		report_list = [table1]
		report_list.extend (diagrams1)
		report_list.append (table2)
		report_list.extend (diagrams2)
		if len(diagrams3):
			report_list.extend (diagrams3)
#		Table1 = pradis.Report.Table.Table([], ['Name of Table', '[[1,2,3],[1,2,3],[4,6,7]]', ])
#		Table2 = pradis.Report.Table.Table([], ['Name of Table', '[[1,2,3],[1,2,3],[4,6,7]]', ])
#		Diagram1 = pradis.Report.Diagram.Diagram([], ['Name of Diagram', [1,2,3,10], [Curve1,Curve2 ], '600', '800', 'linear', 'linear', 'upper_right', yes])
#		Diagram2 = pradis.Report.Diagram.Diagram([], ['Name2', ImportData1, [ImportData2], '450', '640', 'linear', 'linear', 'best', no])

#		print report_list

		Report1 = pradis.Report.Report.Report([], [report_list, self.Template_File, 'html', '', '', '', ''] , desc =  self.desc)

		return Report1.report_file

	def addExtDiagram (self, set, x_min, x_max, name):
		xi = self.generateXi(x_min, x_max)
#		curve_list = []
#		Report.Appendix_count +=1
#		for set in list_set:
		Curve1 = self.plotAdjective (set,x_min,x_max, name)
#		curve_list.append (Curve1)
		Diagram1 = pradis.Report.Diagram.Diagram([], [name, xi, Curve1, self.px, self.py, 'linear', 'linear', 'upper_right', 'yes'], desc = name)

		self.extDiagramm.append(Diagram1)

	def generateVariablePics (self, var_type):

		d_list = []
		for name,result in System().system.variables.items():
			variable = System().system.variables[name]
			if isinstance (variable, var_type):
				d_list.append (self.plotVariableDiagram(name))

		return d_list

	def generateVariablesTable (self, table_name, var_type):

		vl = [['Name','Value','Adjections', 'Range', 'unit',  'Description']]
		for name,result in System().system.variables.items():
			variable = System().system.variables[name]
			if isinstance (variable, var_type):

#				a_list = []
				a_str = ''
				for aname,adjective in variable.adjectives.items():
					if aname.startswith ('.'):
#						continue
						pass
					
					a_str =a_str + aname +', '
				if a_str <>'':
					a_str = a_str [0:-2]
# 				print type(variable.getValue()), variable.getValue()
				vl.append ([name, variable.getValue(), a_str, (variable.min, variable.max), variable.unit, variable.description ])


		return pradis.Report.Table.Table([], [table_name, vl,None ], desc = table_name)

	def write (self, output, file):
#		f  = open (file, "w")
		(filepath, filename) = os.path.split(file)
#		self.createDoc (filepath)
#		self.createDot (filepath)

	def createDoc(self, directory):
		from fuzzy.doc.plot.gnuplot import doc
		d = doc.Doc(directory)
		d.createDoc(System().system)
		d.overscan=0
		print 'Report:', d
		from fuzzy.doc.plot.gnuplot import doc
		doc = doc.Doc("../doc")
		doc.createDoc(System().system)
#		doc.create2DPlot(System().system,"Tin","Tout")

#		d.create3DPlot(System(),"Phi","dPhi_dT","a",{"X":0.,"dX_dT":0.})

	def createDot(self, directory):
		import fuzzy.doc.structure.dot.dot
		import subprocess
		for name,rule in System().system.rules.items():
			cmd = "dot -T png -o '%s/Rule %s.png'" % (directory,name)
			f = subprocess.Popen(cmd, shell=True, bufsize=32768, stdin=subprocess.PIPE).stdin
			fuzzy.doc.structure.dot.dot.print_header(f,"XXX")
			fuzzy.doc.structure.dot.dot.print_dot(rule,f,System().system,"")
			fuzzy.doc.structure.dot.dot.print_footer(f)
		cmd = "dot -T png -o '%s/System.png'" % directory
		f = subprocess.Popen(cmd, shell=True, bufsize=32768, stdin=subprocess.PIPE).stdin
		fuzzy.doc.structure.dot.dot.printDot(System().system,f)

	def boundaries (self, c):
		xmin = 1e-38
		xmax = -1e-38

		import fuzzy.Variable
#		import fuzzy.Set
		return (c.min, c.max)
		if isinstance (c, fuzzy.Variable.Variable):
			return (c.min, c.max)

		if isinstance (c, fuzzy.Set):
			x = c.getValuesX ()
			for y in x:
				if y<xmin:
					xmin = y
				if y>xmax:
					xmax = y

			return (xmin,xmax)

	def printVariable (self, var_name):
		variable = System().system.variables[var_name]
		print var_name +' = ' + str(variable.getValue())

	def plotVariable (self, var_name):

		variable = System().system.variables[var_name]
#		print variable.min
		(x_min,x_max) = self.boundaries (variable)
#		print x_min,x_max
		(filepath, filename) = os.path.split(self.Template_File)
		for name,adjective in variable.adjectives.items():
			# get precomputed adjective set membership
			c = adjective.set #.getMembership()
#			print name, ' = ', c
			fn = var_name+'.'+name
			self.Template_File
			self.plot (c, x_min,x_max,fn, fn)

	def generateXi(self, x_min, x_max):

		xi = [ i*(x_max-x_min)/float(self.steps) + x_min for i in range(self.steps) ]
		xi.append (x_max)
		return xi

	# plot variable by MatPlotLib
	def plotVariableDiagram (self, var_name, services_var = True ):

		variable = System().system.variables[var_name]
#		print variable.min
		(x_min,x_max) = self.boundaries (variable)
#		print x_min,x_max
		xi = self.generateXi (x_min, x_max)
		c_list = []
		for name,adjective in variable.adjectives.items():
			if not (services_var) and name.startswith ('.') :
				continue

			Curve1 = self.plotAdjective (adjective,x_min,x_max, name)
			c_list.append (Curve1)

		Diagram1 = pradis.Report.Diagram.Diagram([], [var_name, xi, c_list, self.px, self.py, 'linear', 'linear', 'upper_right', 'yes'], desc = var_name)

		return Diagram1

	def plotAdjective (self, adj, x_min,x_max, name):
		c = adj.set #.getMembership()
		return self.plotSetDiagram (c,x_min, x_max, name)


	def plotSetDiagram (self, set, x_min,x_max, name):

		steps = 100
		# make array in range x_min,x_max
		xi = self.generateXi(x_min, x_max)
		y = self.dataSet (set, xi)
		(color,symbol,linestyle,thickness) = pradis.Report.Curve.Curve.generateStyle()

#			print (color,symbol,linestyle,thickness)

		Curve1 = pradis.Report.Curve.Curve([], [y, name, linestyle, color, thickness, symbol])

		return Curve1


	def dataSet(self, c,xi):

		yc=[]
		for x in xi:
			yc.append (c(x))

		return yc


	def getGnuplot(self,x_min,x_max):
		"""Get a preconfigured Gnuplot instance for plotting."""
		# A straightforward use of gnuplot.  The `debug=1' switch is used
		# in these examples so that the commands that are sent to gnuplot
		# are also output on stderr.
		g = Gnuplot.Gnuplot(debug=0)
		g(' set style fill solid 0.5 border')
		g('set style data filledcurves y1=0')
		g('set noautoscale xy')
		g('set xrange [%f:%f]' % (x_min,x_max))
		g('set yrange [-0.2:1.2]')
		g.xlabel('x')
		g.ylabel('y')
		return g

	def plot(self, c,x_min,x_max, title,filename, gnuplot=None,interactive=False):
		"""Demonstrate a complement plot"""
#		import fuzzy.set.operations

#		filename = self.Template_File
		set_c = c#fuzzy.set.operations.complement(c,set)
#		(x_min,x_max) = self.boundaries (set_c)
		steps = 50
		# make array in range x_min,x_max
		x = [ i*(x_max-x_min)/float(steps) + x_min for i in range(steps) ]
#		print 'x=',x
		set_c = c#fuzzy.set.operations.complement(c,set)

		g = gnuplot or self.getGnuplot(x_min,x_max)
		g.title(title)

		print "Plot %s ... " % title
		if interactive == False:
			g("set terminal png small truecolor nocrop")
			g("set output '%s.png'" % filename)

		if isinstance(set_c,fuzzy.set.Polygon.Polygon):
			p = set_c.points
			if len(p) == 0:
				raise Exception("Polygon with 0 points found.")
			if p[0][0] > x_min:
				p.insert(0,(x_min,p[0][1]))
			if p[-1][0] < x_max:
				p.append((x_max,p[-1][1]))
#			print '===========', p

			g.plot(p)
		else:
			g.plot(Gnuplot.funcutils.compute_Data(x,set_c))
		if interactive == True:
			raw_input('Please press return to continue...\n')
		if gnuplot is None:
			g.close()
		g = None
