import af
import glb
import base
import sys
import misc
from File import *

class Facet(File):

	def __init__ (self, nl, pl, desc=misc.default):
		self.Name = desc
		par = misc.Expand (pl)
		file = par[0]
		
		facet = base.Facet ()
		self.facet = facet
		facet.SetObjectName(desc)
		file_name = sys.argv[0]
		file_name = file_name.replace(".py", "")
		facet.SetTaskName (file_name)
		facet.SetScheme (glb.sch.GetDescription())
		facet.SetDeflection (par[1])
		facet.SetRelative (par[2])
		facet.SetAngle (par[3])
		facet.SetFacet (file)
		
		File.__init__ (self, nl, [facet.GetMeshFile()], desc=desc)

