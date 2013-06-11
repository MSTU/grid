# -*- coding: cp1251 -*-
from scipy.fftpack import *
from string import *
from scipy import interpolate
import scipy
import math
import af
import misc
import os
from tools import*
class VibrationNorms:

	def __init__ (self, nl, pl, desc=misc.default):
		 
#------------------------------------getting variables--------------------------------------		
		Scheme=pl[0]
		Dat=pl[1]
		Table_Coefficients=pl[2]
		Table_Norm=pl[3]
		Signals_List=pl[4]
		Frequency=pl[5]
		Type_Intervals=pl[6]
		Lower_Octave=pl[7]
		Upper_Octave=pl[8]
#------------------------------------main function-----------------------------------
		if Scheme!='':
			Dat=Simulation_Scheme(Scheme)																	#������ ����� �� ���������, ���� ������ ��� ����� �����
		sc = af.SolverContext (Dat)																			#������������� ��������� ��������
		dc = af.OutVariableContext (sc)																		#������������� ��������� ����
		Signals_Numbers=Getting_List_ID(Signals_List,sc,dc)													#��������� ������ ID ����
		Input_Data=Formation_Array_Data(sc,dc,Signals_Numbers)												#��������� ������ �� ID ���� � ��������� ����� �� DAT �����
		MaxFrequency=Calculation_MaxFrequency(Frequency)													#���������� ������������ �������(���������� �� � ������� ������� ������)
		Discretization=MaxFrequency*16*math.ceil(Input_Data[-1,-1])											#���������� ����� ����� ������������� 
		Interpolated_Data=Interpolate_Data(Input_Data,Discretization)										#���������� ������������ ������  �� ����� ����� �������������
		Maximums=GetMax(Input_Data[0:-1])																	#���������� ������������ �������� ���� �������� �� ���� ��������� ���������
		Average_Square=RMS(Input_Data[0:-1])																#���������� �������������������� ���������� � �� ��������������� ������� ���� �������� �� ���� ��������� ���������

#---------------------------------------------������ ������������ ������--------------

		Integral_Assessment=scipy.zeros((len(Signals_List),2), float)										#�������� ������� ��� ������������ ������ ��������������������� ��������� � ��� ���������������� ������
		for i in range(Lower_Octave,Upper_Octave+1):														#���� �� �������� �������
			Frequency_Range=Get_Frequency_Range(i,i,Type_Intervals)											#��������� ��������� ������ ��� ������ ������(�����������)
			Range_Signal=Signal_Range(Interpolated_Data,Frequency_Range,MaxFrequency)						#��������� ������� � �������� ��������� ���������
			Temp_Average_Square=RMS(Range_Signal[:-1])														#���������� ������������������� �������� ������� � ��� ���������������� ������
			Coefficients=Reading_File(Table_Coefficients,i,Type_Intervals)									#������ ������������� �� ����� ��� ������ ������
			for h in range(len(Signals_List)):																#���� �� ������ ��������
				Integral_Assessment[h,0]+=(Temp_Average_Square[h,0]*Coefficients[0])**2						#��������� ��������������������� ���������� �� �����������
				Integral_Assessment[h,1]+=10**(0.1*(Temp_Average_Square[h,1]+Coefficients [1]))				#���������� ������������ � ���������������� ������
		for h in range(len(Signals_List)):																	#���� �� ������ ��������
			Integral_Assessment[h,0]=math.sqrt(Integral_Assessment[h,0])									#������ ��������������������� ���������� ������� ����������������� �� �������
			Integral_Assessment[h,1]=10*math.log10(Integral_Assessment[h,1])								#������ ���������������� ������ ������� ����������������� �� �������

#----�������� ��������� ������� ������ � ������ � ���� ����������� ���� ����������-----
			
		Length=MaxFrequency*math.ceil(Input_Data[-1,-1])													#������ ���������� ����� ������� ��������� ������ �� ������������ ������� � ������� ������������� �������
		Output_List=scipy.zeros((len(Signals_List)*7+5,Length), float)										#�������� �������� ������� ������
		for k in range(len(Signals_List)):																	#���� �� ������ ��������
			i=0
			while i<Length:																					#������ ������� �� ���� ����� �������
				Output_List[k,i]=Maximums[k]																#������ ������������� �������� �������
				Output_List[k+len(Signals_List),i]=Average_Square[k,0]										#������ ��������������������� ���������� �������
				Output_List[k+len(Signals_List)*2,i]=Average_Square[k,1]									#������ ���������������� ������
				Output_List[k+len(Signals_List)*3,i]=Integral_Assessment[k,0]								#������ ������������������ �� ������� ��������������������� ����������
				Output_List[k+len(Signals_List)*4,i]=Integral_Assessment[k,1]								#������ ������������������ �� ������� ���������������� ������
				i+=1
		
		i=0
		while i<Length:																						#������ �������������� ������
				Output_List[-3,i]=0.56																		#������ ������ 0.56 �/�
				Output_List[-2,i]=115																		#������ ������ 115 ��
				i+=1
		h=0
		while h<Length:																						#��������� ��� ������	
			Output_List[-1,h]=h/Input_Data[-1,-1]															#x������ �����nsdftncz ������ �� ������� ������������� ��������
			h+=1
#--------------------������ ���������-��������� ������ � ������ �� � �������� ������------
		for k in range(Lower_Octave,Upper_Octave+1):														#���� �� �������� �������
			Frequency_Range=Get_Frequency_Range(k,k,Type_Intervals)											#��������� ��������� ������ ��� ������ ������(�����������)
			Range_Signal=Signal_Range(Interpolated_Data,Frequency_Range,MaxFrequency)						#��������� ������� � �������� ��������� ���������
			Temp_Average_Square=RMS(Range_Signal[:-1])														#���������� ������������������� �������� ������� � ��� ���������������� ������
			for h in range(len(Signals_List)):																#���� �� ������ ��������
				i=0
				while i<Length:																				#������ � ������ � �������� ������ ������������� ��� ��������� ������
					if (Output_List[-1,i]>=Frequency_Range[0])&(Output_List[-1,i]<=Frequency_Range[1]):		#���������� ������ � ������ � �������� ���������� ��������� ��������� ������
						Output_List[h+len(Signals_List)*5,i]=Temp_Average_Square[h,0]						#���������� � ������ ��������������������� ����������	
						Output_List[h+len(Signals_List)*6,i]=Temp_Average_Square[h,1]						#���������� � ������ ���������������� ������
					elif Output_List[-1,i]>Frequency_Range[1]:												#����� �� ����� ������� � ������ �� ������� ���������� ������� ������� ���������� ��������� ��������� ������
						break
					i+=1	
#---------������ � �������� ������ ����������� ������ �� ������� ���� �� �������---------
		i=0
		for k in range(Lower_Octave,Upper_Octave+1):														#���� �� �������� �������
			Frequency_Range=Get_Frequency_Range(k,k,Type_Intervals)											#��������� ��������� ������ ��� ������ ������(�����������)
			Norm=Reading_File(Table_Norm,k,Type_Intervals)													#������ ���������� ���� �� ����� ��� ������ ������
			while i<Length:																					#������ ������� �� ���� ����� �������
				if (Output_List[-1,i]>=Frequency_Range[0])&(Output_List[-1,i]<=Frequency_Range[1]):			#���������� ������ � ������ � �������� ���������� ��������� ��������� ������
					Output_List[-5,i]=Norm[0]																#������ ����� ��������������������� ����������
					Output_List[-4,i]=Norm[1]																#������ ����� ���������������� ������
				elif Output_List[-1,i]>Frequency_Range[1]:													#����� �� ����� ������� � ������ �� ������� ���������� ������� ������� ���������� ��������� ��������� ������
					break
				i+=1
#---------�������� ������ ���� �������� ��������, ������ ������ � ���� � ������ ��������������-
		Named_List=["Av_Square.","Logarithmic_Level.","Integral_Assessment.","Integral_Log_Level.","Separ_Freq_Av_Square.","Separ_Freq_Log_Level."] 
		
		Len_Signals_List=len(Signals_List)																	#���������� ����� ������ ��������
		for k in Named_List:																				#���� �� ���������� � ����� �������
			h=0
			while h <Len_Signals_List:																		#���� �� ������ ��������
				Signals_List+=[k+Signals_List[h]]															#���������� �� ���� ������ �������� ���������
				h+=1	
		h=0
		while h <Len_Signals_List:																			#���������� ���������
			Signals_List[h]="Max."+Signals_List[h]
			h+=1		
		Signals_List=Signals_List+["Norm_Av_Square_m/s"]
		Signals_List=Signals_List+["Norm_Log_Level_dB"]
		Signals_List=Signals_List+["0.56m/s"]
		Signals_List=Signals_List+["115dB"]
		Signals_List=["Frequency"]+Signals_List
		


		
		writeFile (Output_List,Signals_List,desc)															#����� ������� ������ ����������� � ����
		misc.SetSolver ("")																					#����� ������ ��������� � �������������
		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")										#����� ������ ��������� � �������������
		misc.SetPostFile(desc+".hst")																		#����� ������ ��������� � �������������