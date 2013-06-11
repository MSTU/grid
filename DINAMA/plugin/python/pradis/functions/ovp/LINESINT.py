# coding=Windows-1251
#HELP<ovp name="LinesInt" module="functions" alias="" priority="5" out="1" par="8" vpr="0" vps="0" wrs="0" wrk="1" wrp="0" sys="12">
#HELP	<description>
#HELP		<russian>Программа для определения пересечений линий</russian>
#HELP		<english>Subroutine for line intersection definition</english>
#HELP	</description>
#HELP	<nodelist>
#HELP		<node name="Node1OfLine1" type="base.Point2d">
#HELP			<description>
#HELP				<russian>Узел 1 отрезка 1</russian>
#HELP				<english>Node 1 of line 1</english>
#HELP			</description>
#HELP		</node>
#HELP		<node name="Node2OfLine1" type="base.Point2d">
#HELP			<description>
#HELP				<russian>Узел 2 отрезка 1</russian>
#HELP				<english>Node 2 of line 1</english>
#HELP			</description>
#HELP		</node>
#HELP		<node name="Node1OfLine2" type="base.Point2d">
#HELP			<description>
#HELP				<russian>Узел 1 отрезка 2</russian>
#HELP				<english>Node 1 of line 2</english>
#HELP			</description>
#HELP		</node>
#HELP		<node name="Node2OfLine2" type="base.Point2d">
#HELP			<description>
#HELP				<russian>Узел 2 отрезка 2</russian>
#HELP				<english>Node 2 of line 2</english>
#HELP			</description>
#HELP		</node>
#HELP	</nodelist>
#HELP	<parameterlist>
#HELP		<parameter name="Point1ofLine1" type="base.pXY" default="0.,0.">
#HELP			<description>
#HELP				<russian>Начальные координаты узла 1 отрезка 1</russian>
#HELP				<english>Initial coordinates of point 1 of line1</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="Point2ofLine1" type="base.pXY" default="1.,0.">
#HELP			<description>
#HELP				<russian>Начальные координаты узла 2 отрезка 1</russian>
#HELP				<english>Initial coordinates of point 2 of line1</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="Point1ofLine2" type="base.pXY" default="0.,0.">
#HELP			<description>
#HELP				<russian>Начальные координаты узла 1 отрезка 2</russian>
#HELP				<english>Initial coordinates of point 1 of line2</english>
#HELP			</description>
#HELP		</parameter>
#HELP		<parameter name="Point2ofLine2" type="base.pXY" default="0.,1.">
#HELP			<description>
#HELP				<russian>Начальные координаты узла 2 отрезка 2</russian>
#HELP				<english>Initial coordinates of point 2 of line2</english>
#HELP			</description>
#HELP		</parameter>
#HELP	</parameterlist>
#HELP	<image2d icon = "functions.LinesInt" symbol = "    .PortSym -30 -30 1 0:
#HELP    .PortSym 30 -30 2 0:
#HELP    .PortSym -30 30 3 0:
#HELP    .PortSym 30 30 4 0:
#HELP    Line -20 -40 40 0 #000080 2 1:
#HELP    Line 20 -40 0 80 #000080 2 1:
#HELP    Line -20 40 40 0 #000080 2 1:
#HELP    Line -20 -40 0 80 #000080 2 1:
#HELP    Line -30 -30 10 0 #000080 2 1:
#HELP    Line 20 -30 10 0 #000080 2 1:
#HELP    Line -30 30 10 0 #000080 2 1:
#HELP    Line 20 30 10 0 #000080 2 1:
#HELP"/>
#HELP	<worklist>
#HELP	</worklist>
#HELP</ovp>
#HELP


from pradis.ppl.ovp import *
import math

class LINESINT(ovp):
	def Execute(COMMON, XOUT, PAR, WRK, DOF):
	


	
		r = 1.0
		r1 = 0.0
		r2 = 0.0
	
		if COMMON.NSTEP == 1:
			WRK[1] = -1000000000
#			print 'w=', WRK[1]
			

	
		x1 = DOF[1]+PAR[1]
		y1 = DOF[2]+PAR[2]
		x2 = DOF[4]+PAR[3]
		y2 = DOF[5]+PAR[4]
		x3 = DOF[7]+PAR[5]
		y3 = DOF[8]+PAR[6]
		x4 = DOF[10]+PAR[7]
		y4 = DOF[11]+PAR[8]


		
		d = -(x2-x1)*(y4-y3)+(x4-x3)*(y2-y1)
		d1= -(x3-x1)*(y4-y3)+(x4-x3)*(y3-y1)
		d2 = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)

		

#		print 'd=',d
#		print 'd1=',d1
#		print 'd2=',d2
		
		
		if (abs(d)<1e-8):
			XOUT[1] =0.0
			res = return_result(COMMON, XOUT, WRK)
			return res
		
		
		t1 = d1/d
		t2 = d2/d
		
#		print 't1=',t1
#		print 't2=',t2

#check!	
		f1 = (x2-x1)*t1+(x4-x3)*t2- (x3-x1)
		f2 = (y2-y1)*t1+(y4-y3)*t2- (y3-y1)
		
		

#		if (abs(f1)>1e-8 | abs(f2)>1e-8):
#			print 'Wrong linear system calculation'

			
			
		r1 =  t1 * (1.0 - t1)
		r2 =  t2 * (1.0 - t2)

#		print 't1=',t1,' t2=',t2

		if r1>=0.0 and r2 >=0.0:
	
			r = (r1+r2)/2.0
#			print 'r=',r		
		else: 
#			print 'r1=',r1,' r2=',r2
			if r1 >0.0:
				r = r2
			else:
				r = r1

		

		
#		r = r1 + r2
#		r = r1

#		print 'r=',r, 'WRK=', WRK[1]
		if (r>WRK[1]):
			WRK[1] = r		
			
		
			
		XOUT[1] =WRK[1]
#		XOUT[1] =t1
	
		res = return_result(COMMON, XOUT, WRK)
		return res

