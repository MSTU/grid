# -*- coding: cp1251 -*-
#import multi
import af
import glb
import misc
import os
import math

#import scipy

#from numpy import copy



# ��������  �� ������ DAT, hst,  xls, txt � ������

class Reader: # (multi.ModelLC):

	def __init__ (self, nl, pl, desc=misc.default):

#		self.ma = multi.ModelLC ()
		self.file = pl[0]		# ���� � ����� �� �������� ����� ������
		
		# ? �������� �� ����� ���������, ������� ������ �� �����? ��� ������ ���������?
	
		

		
		
		self.Run()
#		misc.SetSolver ("")
#		misc.SetPost(os.getenv("DINSYS")+"\dinama\post\Postprocessor")
		
#		misc.SetPostFile(self.ma.GetHistoryFile())
					
				
	def Run (self):
	
		# ������ ���� �:
		values = [0,0,1,1]
		curve = Curve ([], [values, 'style', 'red', '1', 'none'], desc = 'curve name')
		self.curves['curve name'] = curve # ������ ������
	
		pass
		
	def f (self, name, layer = -1):
	
		# ���������� �������� �������� name �� ���� layer (���� -1, �� �� ��������� ����)
	
		return 0.0