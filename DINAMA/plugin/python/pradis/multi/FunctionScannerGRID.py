from numpy import linspace
from multigrid import map as multimap

class FunctionScanner():

	def __init__ (self, nl, pl, desc='FSG'):
		self.variables = pl[0]      #variables list
		self.var_levels = pl[1]
		#level list or amount of possible variable values. This parameter is unique for each variable
		#minimal value of this parameter is 2, because each variable has its minimum and maximum value
		#for example, if you set this parameter for 1st variable in self.variables to 5 there will be next
		#possible values of 1st variable: self.variables[0].Min, self.variables[0].Max and 3 values with step, that is
		#calculated as follows: (self.variables[0].Max - self.variables[0].Min) / (self.var_levels[0] - 1)
		self.loadcases = pl[2]      #loadcases list
		#pvv - possible variable values
		self.pvv_arrays_list = []      #list of 1-dimensional numpy arrays. Each array contains pvv

		if(len(self.var_levels) == 1 and len(self.variables) == 1):
			self.variables[0].Count = self.var_levels[0]
		elif(len(self.var_levels) == 1 and len(self.variables) > 1):
			for i in self.variables:
				i.Count = self.var_levels[0]
		elif(len(self.var_levels) == len(self.variables)):
			n = 0
			for i in self.variables:
				i.Count = self.var_levels[n]
				n += 1
		elif(len(self.var_levels) > len(self.variables)): #ERROR in AmountOfpvv Field
			#Variables Field - field where you specify list of variables,
			#which is used as input parameter for model calculation
			#AmountOfpvv Field - field where you specify list of amounts of pvv for each variable or
			#just one value for all variables
			raise RuntimeError("You made a mistake in AmountOfpvv Field. " +
			"You must enter as many values, as you have in Variables Field. " +
			"You can also enter only one value. All variables will get it. ")
		else: #ERROR in Variables Field (len(self.variables) > len(self.var_levels))
			raise RuntimeError("You made a mistake in Variables Field " +
			"You must enter as many values, as you have in AmountOfpvv Field. " +
			"You can also enter only one value. All variables will get it.")

		self.pvv_arrays_list = self.create_list_of_pvv_arrays(self.variables)

	def create_list_of_pvv_arrays(self, vl):
		#pvv_array = empty(1)        #1-d array (it contains garbage yet)
		pvv_arrays_list = []
		for i in vl:
			pvv_array = linspace(i.Min, i.Max, i.Count)
			pvv_arrays_list.append(pvv_array)
		return pvv_arrays_list

	def all_combinations(self, list_of_lists):
		if(len(list_of_lists) > 1):
			result_list = list()
			combinations_without_first_list = self.all_combinations(list_of_lists[1:])
			for item in list_of_lists[0]:
				for combination in combinations_without_first_list:
					if type(combination) is list:
						result_list.append([item] + combination)
					else:
						result_list.append([item] + [combination])
			return result_list
		else:
			return list_of_lists[0]

	def map_list_to_dict(self, combination, keys):
		result = {}
		if(len(keys) > 1):
			for i in xrange(len(combination)):
				result[keys[i].Name] = combination[i]
		else:
			result[keys[0].Name] = combination

		return result

	def run(self):
		pvv_arrays_list = self.create_list_of_pvv_arrays(self.variables)
		if(len(pvv_arrays_list) > 1):
			all_combs = self.all_combinations(pvv_arrays_list)
		else:
			all_combs = pvv_arrays_list[0]
		in_dicts = [self.map_list_to_dict(combination, self.variables) for combination in all_combs]
		results = multimap(self.loadcases, in_dicts)
		for i in results:
			print i
			print '======================================================'
