#import multi
#import af
#import glb
#import misc
#import os

class Loadcase (multi.Loadcase):

	def __init__ (self, nl, pl, desc="misc.default"):

		self.lc = multi.Loadcase()
		self.lc.Name = desc
		self.lc.Scheme = pl[0]
		self.lc.ResultFile = pl[1]
		vl = pl[2]
#		print 'cr = ', vl

		vl = misc.Expand(vl)

		self.lc.Solver = pl[3]
		self.lc.OpenSign = pl[4]
		self.lc.CloseSign = pl[5]
		
		print 'vl=',vl
		for i in vl:
			print 'i=',i
			self.lc.AddCritery (i)
		
