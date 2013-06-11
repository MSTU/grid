# coding=Windows-1251
#HELP<model name="Equal" module="Mathematics" alias="EQUAL" ext="3" par="1" vpr = "0" adr="2" ign ="3">   
#HELP	<description>
#HELP		<russian>
#HELP 		Функция равенства сигналов 
#HELP		</russian>
#HELP		<english>The description of M3D image</english>
#HELP	</description>
#HELP	<nodelist>
#HELP		<node name="a" type="base.DOF1">
#HELP			<description>
#HELP				<russian>Сигнал a</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP		<node name="b" type="base.DOF1">
#HELP			<description>
#HELP				<russian>Сигнал b</russian>
#HELP				<english>The description of M3D image</english>
#HELP			</description>
#HELP   	</node>
#HELP	</nodelist>
#HELP	<parameterlist>
#HELP		<parameter name="k" type="real" default="1">
#HELP			<description>
#HELP				<russian>Паразитный параметр</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP	</parameterlist>
#HELP	<worklist>
#HELP	</worklist>
#HELP	<statelist>
#HELP	</statelist>
#HELP	<image2d icon = "Mathematics.Equal" symbol = ""/>	
#HELP</model> 

from pradis.ppl.model import *
#from PradisLog import *
from array import *

class EQUAL (model):

	
	def Execute(COMMON, I, Y, X, V, A, PAR, NEW, OLD, WRK):
		if COMMON.NEWINT == 1:                       
#			pl = PradisLog()
			ERR = 0



			if ERR == 1:
				if COMMON.CODE < 100.:
					COMMON.CODE = 100.

				res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
				return res

		s1 = -V[2]+V[1]
		s2 = V[3]
		q = s2-s1
				
		I[1]  =  0.0
		I[2]  =  0.0
		I[3]  =  q

		for i in xrange(3**2):
			Y[i+1] = 0.0
		
		
		Y[1+2*3]  =  -1.0
		Y[2+2*3]  =  1.0
		Y[3+2*3]  =  1.0
		

		res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
		return res

