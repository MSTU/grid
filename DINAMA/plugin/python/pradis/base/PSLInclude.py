import af
import glb
from misc import *



class PSLInclude (af.Include):

	def __init__ (self, nl, pl, desc= misc.default):
		glb.sch.SetIncludeList()
		sl = glb.sch.GetIncludeList()
		self.this = af.Include(sl.Add())
		if (desc!=misc.default):
			self.SetDescription(desc)
		type = pl[1]
		if type == 'psl_data':
			type = 1
		else:
			type = 2
		self.SetIncludeType(type)
		self.SetFile((pl[0]))
		
			



