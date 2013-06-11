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
			Dat=Simulation_Scheme(Scheme)																	#запуск схемы на симуляцию, если задано имя файла схемы
		sc = af.SolverContext (Dat)																			#инициализация контекста решателя
		dc = af.OutVariableContext (sc)																		#инициализация контекста ПРВП
		Signals_Numbers=Getting_List_ID(Signals_List,sc,dc)													#получение списка ID ПРВП
		Input_Data=Formation_Array_Data(sc,dc,Signals_Numbers)												#получение данных по ID ПРВП и временных слоев из DAT файла
		MaxFrequency=Calculation_MaxFrequency(Frequency)													#вычисление максимальной частоты(приведение ее к большей степени двойки)
		Discretization=MaxFrequency*16*math.ceil(Input_Data[-1,-1])											#вычисление числа точек дискретизации 
		Interpolated_Data=Interpolate_Data(Input_Data,Discretization)										#вычисление интерполяции данных  по числу точек дискретизации
		Maximums=GetMax(Input_Data[0:-1])																	#нахождение максимальных значений всех сигналов на всем временном диапазоне
		Average_Square=RMS(Input_Data[0:-1])																#нахождение среднеквадратических отклонений и их логарифмических уровней всех сигналов на всем временном диапазоне

#---------------------------------------------Расчет интегральной оценки--------------

		Integral_Assessment=scipy.zeros((len(Signals_List),2), float)										#создание массива под интегральную оценку среднеквадратического ускорения и его логарифмического уровня
		for i in range(Lower_Octave,Upper_Octave+1):														#цикл по заданным октавам
			Frequency_Range=Get_Frequency_Range(i,i,Type_Intervals)											#получение диапазона частот для данной октавы(третьоктавы)
			Range_Signal=Signal_Range(Interpolated_Data,Frequency_Range,MaxFrequency)						#получение сигнала в заданном частотном диапазоне
			Temp_Average_Square=RMS(Range_Signal[:-1])														#высисление среднеквадратичного значения сигнала и его логарифмического уровня
			Coefficients=Reading_File(Table_Coefficients,i,Type_Intervals)									#чтение коэффициентов из файла для данной октавы
			for h in range(len(Signals_List)):																#цикл по списку сигналов
				Integral_Assessment[h,0]+=(Temp_Average_Square[h,0]*Coefficients[0])**2						#умножение среднеквадратического отклонения на коээфициент
				Integral_Assessment[h,1]+=10**(0.1*(Temp_Average_Square[h,1]+Coefficients [1]))				#добавление коэффициента к логарифмическому уровню
		for h in range(len(Signals_List)):																	#цикл по списку сигналов
			Integral_Assessment[h,0]=math.sqrt(Integral_Assessment[h,0])									#расчет среднеквадратического отклонения сигнала скоректированного по частоте
			Integral_Assessment[h,1]=10*math.log10(Integral_Assessment[h,1])								#расчет логарифмического уровня сигнала скоректированного по частоте

#----Создание выходного массива данных и запись в него расчитанных выше параметров-----
			
		Length=MaxFrequency*math.ceil(Input_Data[-1,-1])													#расчет количества точек каждого параметра исходя из максимальной частоты и времени динамического расчета
		Output_List=scipy.zeros((len(Signals_List)*7+5,Length), float)										#создание выходног массива данных
		for k in range(len(Signals_List)):																	#цикл по списку сигналов
			i=0
			while i<Length:																					#запись ведется по всей длине массива
				Output_List[k,i]=Maximums[k]																#запись максимального значения сигнала
				Output_List[k+len(Signals_List),i]=Average_Square[k,0]										#запись среднексадратического отклонения сигнала
				Output_List[k+len(Signals_List)*2,i]=Average_Square[k,1]									#запись логарифмического уровня
				Output_List[k+len(Signals_List)*3,i]=Integral_Assessment[k,0]								#запись скорректированного по частоте среднеквадратического отклонения
				Output_List[k+len(Signals_List)*4,i]=Integral_Assessment[k,1]								#запись скорректированного по частоте логарифмического уровня
				i+=1
		
		i=0
		while i<Length:																						#запись контролирующих прямых
				Output_List[-3,i]=0.56																		#запись прямой 0.56 м/с
				Output_List[-2,i]=115																		#запись прямой 115 дБ
				i+=1
		h=0
		while h<Length:																						#генерация оси частот	
			Output_List[-1,h]=h/Input_Data[-1,-1]															#xастота расчиnsdftncz исходя из времени динамического рассчета
			h+=1
#--------------------Расчет раздельно-частотной оценки и запись ее в выходной массив------
		for k in range(Lower_Octave,Upper_Octave+1):														#цикл по заданным октавам
			Frequency_Range=Get_Frequency_Range(k,k,Type_Intervals)											#получение диапазона частот для данной октавы(третьоктавы)
			Range_Signal=Signal_Range(Interpolated_Data,Frequency_Range,MaxFrequency)						#получение сигнала в заданном частотном диапазоне
			Temp_Average_Square=RMS(Range_Signal[:-1])														#высисление среднеквадратичного значения сигнала и его логарифмического уровня
			for h in range(len(Signals_List)):																#цикл по списку сигналов
				i=0
				while i<Length:																				#расчет и запись в выходной массив характеристик для отдельной октавы
					if (Output_List[-1,i]>=Frequency_Range[0])&(Output_List[-1,i]<=Frequency_Range[1]):		#записываем данные в массив в пределах частотного диапазона выбранной октавы
						Output_List[h+len(Signals_List)*5,i]=Temp_Average_Square[h,0]						#вычисление и запись среднеквадратического отклонения	
						Output_List[h+len(Signals_List)*6,i]=Temp_Average_Square[h,1]						#вычисление и запись логарифмического уровня
					elif Output_List[-1,i]>Frequency_Range[1]:												#выход из цикла расчета и записи по условию превышения верхней границы частотного диапазона выбранной октавы
						break
					i+=1	
#---------Запись в выходной массив контрольных данных из таблицы норм по октавам---------
		i=0
		for k in range(Lower_Octave,Upper_Octave+1):														#цикл по заданным октавам
			Frequency_Range=Get_Frequency_Range(k,k,Type_Intervals)											#получение диапазона частот для данной октавы(третьоктавы)
			Norm=Reading_File(Table_Norm,k,Type_Intervals)													#чтение санитарных норм из файла для данной октавы
			while i<Length:																					#запись ведется по всей длине массива
				if (Output_List[-1,i]>=Frequency_Range[0])&(Output_List[-1,i]<=Frequency_Range[1]):			#записываем данные в массив в пределах частотного диапазона выбранной октавы
					Output_List[-5,i]=Norm[0]																#запись нормы среднеквадратического отклонения
					Output_List[-4,i]=Norm[1]																#запись нормы логарифмического уровня
				elif Output_List[-1,i]>Frequency_Range[1]:													#выход из цикла расчета и записи по условию превышения верхней границы частотного диапазона выбранной октавы
					break
				i+=1
#---------Создание списка имен выходных сигналов, запись данных в файл и запуск постпроцессора-
		Named_List=["Av_Square.","Logarithmic_Level.","Integral_Assessment.","Integral_Log_Level.","Separ_Freq_Av_Square.","Separ_Freq_Log_Level."] 
		
		Len_Signals_List=len(Signals_List)																	#нахождение длины списка сигналов
		for k in Named_List:																				#цикл по приставкам к имени сигнала
			h=0
			while h <Len_Signals_List:																		#цикл по списку сигналов
				Signals_List+=[k+Signals_List[h]]															#добавление ко всем именам сигналов приставки
				h+=1	
		h=0
		while h <Len_Signals_List:																			#добавление приставки
			Signals_List[h]="Max."+Signals_List[h]
			h+=1		
		Signals_List=Signals_List+["Norm_Av_Square_m/s"]
		Signals_List=Signals_List+["Norm_Log_Level_dB"]
		Signals_List=Signals_List+["0.56m/s"]
		Signals_List=Signals_List+["115dB"]
		Signals_List=["Frequency"]+Signals_List
		


		
		writeFile (Output_List,Signals_List,desc)															#вызов функции записи результатов в файл
		misc.SetSolver ("")																					#вывод данных обработки в постпроцессор
		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")										#вывод данных обработки в постпроцессор
		misc.SetPostFile(desc+".hst")																		#вывод данных обработки в постпроцессор