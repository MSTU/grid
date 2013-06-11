# -*- coding: cp1251 -*-
from scipy.fftpack import *
from string import *
from scipy import interpolate
import scipy
import math
import af
import misc
import os
def writeFile (dat,name,desc):																			# функция записи результатов в файл
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

def Simulation_Scheme(Scheme_Name):																	# функция запуска моделирования схемы
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
def Getting_List_ID(List_Names,Solver_Context, Data_Context):										# функция получения списка ID ПРВП
	List_Numbers=List_Names[:]
	for h in range(len(List_Names)):									
		for k in range(Solver_Context.GetPRVPSize()):
			Data_Context.SetPRVPNumber(k+1)
			if rstrip(Data_Context.GetOVPName())==List_Names[h]:
				List_Numbers[h]=k
				break
	return List_Numbers
def Formation_Array_Data(Solver_Context, Data_Context,List_Numbers_Variables):						#функция получения данных из DAT файла
	Data_Aray=scipy.zeros((len(List_Numbers_Variables)+1,Solver_Context.GetLayerSize()), float)		# инициализация массива значений выходных переменных  и времени
	i=0
	Number_Layers=Solver_Context.GetLayerSize()
	while i <Number_Layers:         																# цикл  по временным слоям. Получение числа временных слоев. Формирование массивов данных.
		Data_Context.SetLayer (i)																	# установка текущего временного слоя
		Solver_Context.SetLayer(i)																	# установка текущего временного слоя. Тоже надо.
		Data_Aray[-1,i]=Solver_Context.GetTime()													# получение текущего времени
		for k in range(len(List_Numbers_Variables)):												# цикл получения значений всех интересующих нас переменных на данном временном слое)
			Data_Aray[k,i]=Data_Context.GetOutVariable(List_Numbers_Variables[k])
		i+=1
	return Data_Aray
def Calculation_MaxFrequency(Frequency):															#функция вычисления максимальной частоты
	temp=1
	while Frequency > temp:												
		temp*=2
	MaxFrequency=temp
	return MaxFrequency
def Interpolate_Data(Data,Number_Points):															#функция интерполяции данных
	Tnew=scipy.arange(Data[-1,0]+1e-25,Data[-1,-1],Data[-1,-1]/Number_Points)						#разбиение отрезка времени на равные интервалы
	Interpolated=scipy.zeros((len(Data),Number_Points), float)			
	for h in range(len(Interpolated)-1):																#линейная интерполяция данных и получение данных на равных промежутках времени
		f = interpolate.interp1d(Data[-1], Data[h])
		Interpolated[h]=f(Tnew)
	Interpolated[-1]=Tnew
	return Interpolated
def Amplitude_Spectrum(Data):																		#функция получения спектра амплитуд
	Spectrum=scipy.zeros((len(Data),len(Data[0])/2), float)											#выделение массива под спектры
	for h in range(len(Data)):										
		Temp=rfft(Data[h])																			#преобразование Фурье
		Spectrum[h,0]=abs(Temp[0])/len(Data[0])														#взятие модуля и деление на число точек для получения истинной амплитуды
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
	Fourier=scipy.zeros((len(Data),len(Data[0])), float)									#выделение массива под преобразованеи Фурье данных
	Range_Signal=scipy.zeros((len(Data),len(Data[0])), float)
	for h in range(len(Data)-1):															#преобразование Фурье
		Fourier[h]=rfft(Data[h])																			
	
	Fourier[-1,0]=0																			#генерация оси частот
	h=1
	while h<MaxFrequency*8*math.ceil(Data[-1,-1]):													
		Fourier[-1,h*2-1]=h/Data[-1,-1]																
		Fourier[-1,h*2]=h/Data[-1,-1]
		h+=1
	Fourier[-1,h*2-1]=h/Data[-1,-1]

	Len_Fourier=len(Fourier[-1])															#поиск границ заданного интервала по оси часто
	count=0
	while count<Len_Fourier:																#поиск положения левой границы заданного диапазона на оси частот
		if Fourier[-1,count]>=Range[0]:
			Left_Border=count
			break
		count+=1	
	while count<Len_Fourier:																#поиск положения правой границы заданного диапазона на оси частот
		if Fourier[-1,count]>Range[1]:
			Right_Border=count
			break
		count+=1

	for h in range(len(Data)-1):															#отброс(зануление) частей преобразования фурье не входящих в заданный диапазон
		Fourier[h,:Left_Border]=scipy.zeros(Left_Border, float)
		Fourier[h,Right_Border:]=scipy.zeros(len(Fourier[h,Right_Border:]), float)
	for h in range(len(Data)-1):															#обратное преобразование Фурье
		Range_Signal[h]=irfft(Fourier[h])
	Range_Signal[-1]=Data[-1]
	return Range_Signal

def Reading_File(File_Name,Number_Octave,Type):
	Filehandle = open (File_Name, 'r')														#открытие файла для чтения
	Number_Rows=sum(1 for l in Filehandle)													#подсчет числа строк в файле
	Filehandle.seek(0,0)																	#возврат указателя в начало файла
	i=0
	while i<Number_Rows:																	#переход к нужному разделу файла - октавы или третьоктавы
		if Filehandle.readline()==Type+'\n':
			Filehandle.readline()
			break
		i+=1
	i=1
	while i<=Number_Octave:																	#коэффициентов для заданной октавы(третьоктавы)
		Temp=Filehandle.readline()
		i+=1
	Coefficients=map(float,Temp.split('\t\t\t'))[1:]										#получение получение коэффициентов Ki и LKi в виде списка [Ki,LKi]
	Filehandle.close ()																		#закрытие файла
	return Coefficients																		#возврат списка коэффициентов
def Frequency_Spectrum(Data):																		#функция получения спектра частот
	Spectrum=scipy.zeros((len(Data),len(Data[0])/2), float)											#выделение массива под спектры
	for h in range(len(Data)):										
		Temp=rfft(Data[h])																			#преобразование Фурье
		Spectrum[h,0]=0															#взятие модуля и деление на число точек для получения истинной амплитуды
		k=1
		Len_Dat=len(Spectrum[0])
		while k<Len_Dat:
			Spectrum[h,k]=math.atan(Temp[2*k-1]/Temp[2*k])
			k+=1
	return Spectrum