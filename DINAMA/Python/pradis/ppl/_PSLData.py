import af
import glb
#from OutValue import *
import misc

class PSLData (af.Include):

	def __init__ (self, filename, desc= misc.default):
		glb.sch.SetIncludeList()
		sl = glb.sch.GetIncludeList()
		self.this = af.Include(sl.Add())
		if (desc!=misc.default):
			self.SetDescription(desc)
		self.SetIncludeType(1)
		self.SetFile((filename))
		
			



