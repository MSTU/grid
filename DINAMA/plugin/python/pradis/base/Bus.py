import af
import misc
from glb import *
from Node import *
from DOF import *

class Bus:

	def __init__(self, n1, n2, desc = misc.default):
	
		bus_node = n1[0]
		node = n1[1]
		
		name = n2[0]
		type = n2[1]
		

		if (hasattr (bus_node, name)==0):
			setattr (bus_node, name, node)
		else:
			nn = getattr (bus_node, name)
			
#			print 'nn=', str(nn.__name__)

#	todo: type checking			
#			if (nn.__name__ != node.__name__):
#	nodes are not the same
#				raise Exception.TypeError ("Type of the node <" 
#				+name+"> from the bus != type of the node "+node+" ("+type+")\nPlease check types of the nodes")			
				
#			print 'ass=', str(node),'  ', type
#			raw_input
			nn.associate (node, type)
		
#		n1[1].x.Copy (n1[0], "x")
#		n1[2].x.Copy (n1[0], "y")
#		n1[3].x.Copy (n1[0], "z")
		
#	def associate (self, node, type)
		