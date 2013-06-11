# -*- coding: cp1251 -*-
from scipy.fftpack import *
from string import *
from scipy import interpolate
import scipy
import math
import cmath
import af
import misc
import os
from tools import*
class Modal:

	def __init__ (self, nl, pl, desc=misc.default):
		 
#------------------------------------getting variables--------------------------------------		
		Scheme=pl[0]
		Dat=pl[1]
		Output_Signals_List=pl[2]
		minFrequency=pl[3]
		if (minFrequency==None):
			minFrequency = -1
		maxFrequency=pl[4]
		if (maxFrequency==None):
			maxFrequency = 1e38
		NFrequency=pl[5]
		if (NFrequency==None):
			NFrequency = 32767
		eps=pl[6]

		#------------------------------------main function-----------------------------------
		if Scheme!='':
			Dat=Simulation_Scheme(Scheme)
		sc = af.SolverContext (Dat)																			#инициализация контекста решателя
		dc = af.OutVariableContext (sc)																		#инициализация контекста ПРВП
			
		Output_Signals_Numbers=Getting_List_ID(Output_Signals_List,sc,dc)									#получение списка ID ПРВП
		Input_Data=Formation_Array_Data(sc,dc,Output_Signals_Numbers)										#получение данных по ID ПРВП и временных слоев из DAT файла
		MaxFrequency=Calculation_MaxFrequency(maxFrequency)													#вычисление максимальной частоты(приведение ее к большей степени двойки)
		Discretization=MaxFrequency*16*math.ceil(Input_Data[-1,-1])											#вычисление числа точек дискретизации 
		Interpolated_Data=Interpolate_Data(Input_Data,Discretization)										#вычисление интерполяции данных  по числу точек дискретизации
		dt = 1.0/Input_Data[-1,-1]		
		(Freqs, Energy, Modes)=Modals(dt, Interpolated_Data[0:-1], minFrequency, maxFrequency, NFrequency, eps)												#получение спектра аплитуд для интерполированных сигналов
#		print 'sssss'
#		Output_List=scipy.zeros((len(Spectrum)*2+1,MaxFrequency*math.ceil(Input_Data[-1,-1])), float)		#формирование выходного списка для записи в файл *.hst


		for h in range(len(Output_Signals_List)):															#создание списка имен выходных параметров
			Output_Signals_List[h]="Modal."+Output_Signals_List[h]
		Output_Signals_List=["Modal.Frequency"]+["Modal.ModeEnergy"]+Output_Signals_List
	
		writeFile (Freqs, Energy, Modes,Output_Signals_List,desc)													#вызов функции записи результатов в файл
		
		misc.SetSolver ("")																					#вывод данных обработки в постпроцессор
		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")										#вывод данных обработки в постпроцессор
		misc.SetPostFile(desc+".hst")																		#вывод данных обработки в постпроцессор
		
		
		
def Modals(dt, Data, fmin, fmax, nmax, eps):																		# функция получения спектра амплитуд
	fftData=scipy.zeros((len(Data),len(Data[0])/2), complex)											# выделение массива под спектры
 
	lenData = len(Data)
#	print 'fftData = ', fftData
	lenFreq=len(fftData[0])
	for h in xrange(lenData):										
		Temp=fft(Data[h])																			# преобразование Фурье
#		print 'Temp = ', Temp
		for i in xrange(lenFreq):										
			fftData[h,i] = Temp[i]
	lastE=0.0
	lastEE=1.0

	Energy = []
	Modes = []
	Freqs   = []
	N=0
	f=0.0
#	print 'len=', lenFreq, 'fmin=', fmin, 'fmax=',fmax, 'nmax=', nmax
# поиск моды с максимальной энергетикой
	Emax = -1.0
	for h in xrange(lenFreq):		
		if h==0:
			continue	
		flast = f
		f= h*dt
		if (f<fmin):
			continue
		if (f>fmax):
			break
		En = 0.0
		for i in xrange (lenData):
			z = (fftData[i])[h] 
			En=En+abs(z)**2
		if (En>Emax):
			Emax = En
	Eeps = Emax * eps
# нормирование мод
	for h in xrange(lenFreq):		
		if h==0:
			continue	
		flast = f
		f= h*dt
		
		if (f<fmin):
			continue
		if (f>fmax):
			break
		En = 0.0
		for i in xrange (lenData):
			z = (fftData[i])[h] 
			En=En+abs(z)**2
		
#		print 'f=',f,' En=',En
		if (lastEE<lastE):
			if (lastE>En):
# maximum				
				if (lastE >=Eeps) :
					Energy.append (lastE)
					Freqs.append (flast)
					amp = math.sqrt(En)
					mode = []
					for j in xrange (lenData):
						z = (fftData[j])[h-1] 
						mode.append (abs(z)/amp)
					Modes.append(mode)
					N =N + 1
					if (N>=nmax):
						break
		lastEE=lastE
		lastE=En
 
	return (Freqs, Energy, Modes)


def writeFile (Freqs, Energy, Modes,name,desc):																			# функция записи результатов в файл
	Filehandle = open (desc+".hst", 'w')
	Filehandle.write(desc+"\n\n")
	for i in name:
		Filehandle.write (ljust(str(i), 41))
	Filehandle.write ("\n")
	Len_Dat=len(Freqs)
	count=0
	while count <Len_Dat:
		Filehandle.write (rjust(str(Freqs[count]), 41))
		Filehandle.write (rjust(str(Energy[count]), 41))
		i=0
		mode = Modes[count]
		while i< (len(Modes[0])):
			Filehandle.write (rjust(str(mode[i]), 41))
			i+=1
		count+=1
		Filehandle.write ("\n")
	Filehandle.close ()	






	