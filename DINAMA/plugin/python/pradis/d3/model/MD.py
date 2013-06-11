# coding=Windows-1251
#HELP<model name="MD" module="d3" ext="3" par="2" adr="3">   
#HELP	<description>
#HELP		<russian>Модель MD продолжение описания модели</russian>
#HELP		<english>Description MD continue description</english>
#HELP	</description>
#HELP	<nodelist>
#HELP		<node name="NODE1" type="DOF"></node>
#HELP	</nodelist>
#HELP	<parameterlist>
#HELP		<parameter name="ParName1" type="real"></parameter>
#HELP	</parameterlist>
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

