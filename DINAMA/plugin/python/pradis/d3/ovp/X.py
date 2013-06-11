# coding=Windows-1251
#HELP<ovp name="X" module="d3" out="1" par="1" sys="1">   
#HELP<description><russian>"ПРВП X"</russian><english>"Description X"</english></description>
#HELP<modulelist>
#HELP<module name="d3">
#HELP	<description><russian>"Описание модуля"</russian><english>"Module description"</english></description>
#HELP</module>
#HELP</modulelist>
#HELP	<nodelist>
#HELP		<node>
#HELP<description><russian></russian><english></english></description>
#HELP		</node>
#HELP	</nodelist>
#HELP	<parameterlist>
#HELP		<parameter>
#HELP<description><russian></russian><english></english></description>
#HELP		</parameter>
#HELP	</parameterlist>
#HELP</ovp> 

from pradis.ppl.ovp import *

class X(ovp):

	
    def Execute(COMMON, XOUT, PAR, WRK, DOF):
		XOUT[1] = PAR[1]*DOF[1]
		res = return_result(COMMON, XOUT, WRK)
		return res

