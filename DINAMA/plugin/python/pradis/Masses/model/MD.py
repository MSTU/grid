# coding=Windows-1251
#HELP<model name="MD" module="Masses" ext="1" par="1" adr="3">   
#HELP	<description>
#HELP		<russian>
#HELP 		Поступательная составляющая инерционных свойств твердого тела 
#HELP		</russian>
#HELP		<english>The description of M3D image</english>
#HELP	</description>
#HELP	<nodelist>
#HELP		<node name="Node1" type="XYZ"></node>
#HELP	</nodelist>
#HELP	<parameterlist>
#HELP		<parameter name="M" type="real" default="1.0">
#HELP			<description>
#HELP				<russian>Масса</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="M2" type="real" default="1.0">
#HELP			<description>
#HELP				<russian>Масса2</russian>
#HELP				<english>Inertia coefficient (mass)</english>
#HELP			</description>
#HELP		</parameter>
#HELP	</parameterlist>
#HELP	<worklist>
#HELP	</worklist>
#HELP	<statelist>
#HELP	</statelist>
#HELP	<image2d icon = "Masses.M3D" symbol = "
#HELP  Line -20 -20 0 20 #000080 2 1:
#HELP  Line -20 -10 -20 0 #000080 2 1:
#HELP  .PortSym -40 -10 1 0:
#HELP  Line 0 0 -20 0 #000080 2 1:
#HELP  Line -20 -20 20 0 #000080 2 1:
#HELP  Line 0 -20 0 20 #000080 2 1:
#HELP  
#HELP  Text -17 -16 8 #000080 0 %ap;3D%ap;
#HELP  
#HELP  "/>	
#HELP</model> 

from pradis.ppl.model import *
from PradisLog import *
from array import *

class MD (model):

	
	def Execute(COMMON, I, Y, X, V, A, PAR, NEW, OLD, WRK):
		if COMMON.NEWINT == 1:                       
			pl = PradisLog()
			ERR = 0

			if PAR[1] < 0.:
				ERR = 1
				if COMMON.SYSPRN > 0.:
					a = array ('d', [1., 0., 1., PAR[1]])
					pl.perr (1003, 4, a.buffer_info()[0])

			if PAR[2] < 0.:
				ERR = 1
				if COMMON.SYSPRN > 0.:
					a = array ('d', [2., 0., 2., PAR[2]])
					pl.perr (1003, 4, a.buffer_info()[0])

			if ERR == 1:
				if COMMON.CODE < 100.:
					COMMON.CODE = 100.

				res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
				return res


		I[1]  =  A[1] * PAR[1]
		I[2]  =  A[2] * PAR[1]
		I[3]  =  A[3] * PAR[2]

		Y[1]  =  PAR[1]
		Y[2]  =  0.  
		Y[3]  =  0.  
		Y[4]  =  0.  
		Y[5]  =  PAR[1]
		Y[6]  =  0.  
		Y[7]  =  0.  
		Y[8]  =  0.  
		Y[9]  =  PAR[2]

		res = return_result(COMMON, I, Y, X, V, A, NEW, OLD, WRK)
		return res

