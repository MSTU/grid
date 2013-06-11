import misc

#import scipy

#from numpy import copy


# Кривая

class TextStyle: # (multi.ModelLC):

	def __init__ (self, nl, pl, desc=misc.default):

		self.family = pl[0]	#
		self.size = pl[1]

	def GetTextStyle(self):
		if self.family=='TimesNewRoman': 
			self.family='Times New Roman'
		div = '			<DIV  style="font-size:'+self.size+'; font-family:'+self.family+', sans-serif;">\n'
		return div
	