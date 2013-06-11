# -*- coding: cp1251 -*-
from scipy.fftpack import *
from string import *
from scipy import interpolate
import scipy
import math
import af
import misc
import os
def writeFile (dat,name,desc):																			# ������� ������ ����������� � ����
	Filehandle = open (desc+".hst", 'w')
	Filehandle.write(desc+"\n\n")
	for i in name:
		Filehandle.write (ljust(str(i), 41))
	Filehandle.write ("\n")
	Len_Dat=len(dat[0])
	count=0
	while count <Len_Dat:
		i=-1
		while i< (len(dat)-1):
			Filehandle.write (rjust(str(dat[i][count]), 41))
			i+=1
		count+=1
		Filehandle.write ("\n")
	Filehandle.close ()	

def Simulation_Scheme(Scheme_Name):																	# ������� ������� ������������� �����
	Position =Scheme_Name.rfind('.')
	Extension=Scheme_Name[Position:]
	Name=Scheme_Name[:Position]
	if Extension=='.sch':
		Dat=Name_Name+'.sch.psl.DAT'
	elif Extension=='.py':
		os.spawnve(os.P_WAIT, os.getenv("DINSYS")+"\Python24\python", [os.getenv("DINSYS")+"\Python24\python", Scheme_Name], os.environ) 
		Dat_Name=Name+'.psl.DAT'
	elif Extension=='.psl':
		os.spawnve(os.P_WAIT, os.getenv("DINSYS")+"\dinama\pradis32\slang", [os.getenv("DINSYS")+"\dinama\pradis32\slang", Scheme_Name], os.environ) 
		Dat_Name=Name+'.psl.DAT'
	return Dat_Name
def Getting_List_ID(List_Names,Solver_Context, Data_Context):										# ������� ��������� ������ ID ����
	List_Numbers=List_Names[:]
	for h in range(len(List_Names)):									
		for k in range(Solver_Context.GetPRVPSize()):
			Data_Context.SetPRVPNumber(k+1)
			if rstrip(Data_Context.GetOVPName())==List_Names[h]:
				List_Numbers[h]=k
				break
	return List_Numbers
def Formation_Array_Data(Solver_Context, Data_Context,List_Numbers_Variables):						#������� ��������� ������ �� DAT �����
	Data_Aray=scipy.zeros((len(List_Numbers_Variables)+1,Solver_Context.GetLayerSize()), float)		# ������������� ������� �������� �������� ����������  � �������
	i=0
	Number_Layers=Solver_Context.GetLayerSize()
	while i <Number_Layers:         																# ����  �� ��������� �����. ��������� ����� ��������� �����. ������������ �������� ������.
		Data_Context.SetLayer (i)																	# ��������� �������� ���������� ����
		Solver_Context.SetLayer(i)																	# ��������� �������� ���������� ����. ���� ����.
		Data_Aray[-1,i]=Solver_Context.GetTime()													# ��������� �������� �������
		for k in range(len(List_Numbers_Variables)):												# ���� ��������� �������� ���� ������������ ��� ���������� �� ������ ��������� ����)
			Data_Aray[k,i]=Data_Context.GetOutVariable(List_Numbers_Variables[k])
		i+=1
	return Data_Aray
def Calculation_MaxFrequency(Frequency):															#������� ���������� ������������ �������
	temp=1
	while Frequency > temp:												
		temp*=2
	MaxFrequency=temp
	return MaxFrequency
def Interpolate_Data(Data,Number_Points):															#������� ������������ ������
	Tnew=scipy.arange(Data[-1,0]+1e-25,Data[-1,-1],Data[-1,-1]/Number_Points)						#��������� ������� ������� �� ������ ���������
	Interpolated=scipy.zeros((len(Data),Number_Points), float)			
	for h in range(len(Interpolated)-1):																#�������� ������������ ������ � ��������� ������ �� ������ ����������� �������
		f = interpolate.interp1d(Data[-1], Data[h])
		Interpolated[h]=f(Tnew)
	Interpolated[-1]=Tnew
	return Interpolated
def Amplitude_Spectrum(Data):																		#������� ��������� ������� ��������
	Spectrum=scipy.zeros((len(Data),len(Data[0])/2), float)											#��������� ������� ��� �������
	for h in range(len(Data)):										
		Temp=rfft(Data[h])																			#�������������� �����
		Spectrum[h,0]=abs(Temp[0])/len(Data[0])														#������ ������ � ������� �� ����� ����� ��� ��������� �������� ���������
		k=1
		Len_Dat=len(Spectrum[0])
		while k<Len_Dat:
			Spectrum[h,k]=math.sqrt(Temp[2*k-1]**2+Temp[2*k]**2)*2/len(Data[0])
			k+=1
	return Spectrum
def GetMax(Data):
	Maximums=scipy.zeros(len(Data), float)
	for h in range(len(Data)):
		Len_Dat=len(Data[h])
		i=0
		while i<Len_Dat:
			if abs(Data[h,i])>Maximums[h]:
				Maximums[h]=abs(Data[h,i])
			i+=1
	return Maximums
def RMS(Data):
	Average_Square=scipy.zeros((len(Data),2), float)
	Average=scipy.zeros(len(Data), float)
	for h in range(len(Data)):
		Len_Dat=len(Data[h])
		i=0
		Sum=0
		while i<Len_Dat:
			Sum+=Data[h,i]
			i+=1
		Average[h]=Sum/Len_Dat
	for h in range(len(Data)):
		Len_Dat=len(Data[h])
		i=0
		Sum_Squares=0
		while i<Len_Dat:
			Sum_Squares+=(Data[h,i]-Average[h])**2
			i+=1
		Average_Square[h,0]=math.sqrt(Sum_Squares/Len_Dat)
		Average_Square[h,1]=float(20*math.log10(Average_Square[h,0]/1e-6))
	return Average_Square

def Get_Frequency_Range(Lower_Octave,Upper_Octave,Type):
	if Type=='Octave':
		return [0.7*2**(Lower_Octave-1),0.7*2**Upper_Octave]
	elif Type=='Onethird_octave':
		return [0.7*2**(float(Lower_Octave-1)/3),0.7*2**(float(Upper_Octave)/3)]
	else:
		print 'Invalid type'

def Signal_Range(Data,Range,MaxFrequency):	
	Fourier=scipy.zeros((len(Data),len(Data[0])), float)									#��������� ������� ��� �������������� ����� ������
	Range_Signal=scipy.zeros((len(Data),len(Data[0])), float)
	for h in range(len(Data)-1):															#�������������� �����
		Fourier[h]=rfft(Data[h])																			
	
	Fourier[-1,0]=0																			#��������� ��� ������
	h=1
	while h<MaxFrequency*8*math.ceil(Data[-1,-1]):													
		Fourier[-1,h*2-1]=h/Data[-1,-1]																
		Fourier[-1,h*2]=h/Data[-1,-1]
		h+=1
	Fourier[-1,h*2-1]=h/Data[-1,-1]

	Len_Fourier=len(Fourier[-1])															#����� ������ ��������� ��������� �� ��� �����
	count=0
	while count<Len_Fourier:																#����� ��������� ����� ������� ��������� ��������� �� ��� ������
		if Fourier[-1,count]>=Range[0]:
			Left_Border=count
			break
		count+=1	
	while count<Len_Fourier:																#����� ��������� ������ ������� ��������� ��������� �� ��� ������
		if Fourier[-1,count]>Range[1]:
			Right_Border=count
			break
		count+=1

	for h in range(len(Data)-1):															#������(���������) ������ �������������� ����� �� �������� � �������� ��������
		Fourier[h,:Left_Border]=scipy.zeros(Left_Border, float)
		Fourier[h,Right_Border:]=scipy.zeros(len(Fourier[h,Right_Border:]), float)
	for h in range(len(Data)-1):															#�������� �������������� �����
		Range_Signal[h]=irfft(Fourier[h])
	Range_Signal[-1]=Data[-1]
	return Range_Signal

def Reading_File(File_Name,Number_Octave,Type):
	Filehandle = open (File_Name, 'r')														#�������� ����� ��� ������
	Number_Rows=sum(1 for l in Filehandle)													#������� ����� ����� � �����
	Filehandle.seek(0,0)																	#������� ��������� � ������ �����
	i=0
	while i<Number_Rows:																	#������� � ������� ������� ����� - ������ ��� �����������
		if Filehandle.readline()==Type+'\n':
			Filehandle.readline()
			break
		i+=1
	i=1
	while i<=Number_Octave:																	#������������� ��� �������� ������(�����������)
		Temp=Filehandle.readline()
		i+=1
	Coefficients=map(float,Temp.split('\t\t\t'))[1:]										#��������� ��������� ������������� Ki � LKi � ���� ������ [Ki,LKi]
	Filehandle.close ()																		#�������� �����
	return Coefficients																		#������� ������ �������������
def Frequency_Spectrum(Data):																		#������� ��������� ������� ������
	Spectrum=scipy.zeros((len(Data),len(Data[0])/2), float)											#��������� ������� ��� �������
	for h in range(len(Data)):										
		Temp=rfft(Data[h])																			#�������������� �����
		Spectrum[h,0]=0															#������ ������ � ������� �� ����� ����� ��� ��������� �������� ���������
		k=1
		Len_Dat=len(Spectrum[0])
		while k<Len_Dat:
			Spectrum[h,k]=math.atan(Temp[2*k-1]/Temp[2*k])
			k+=1
	return Spectrum