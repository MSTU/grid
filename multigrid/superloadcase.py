import constants
from serialization import cloudpickle


class SuperLoadcase:
	def __init__(self, nl, pl, desc = constants.DEFAULT_LOADCASE):
		scheme_name = pl[0]
		result_name = pl[1]
		self.functions_list = [cloudpickle.dumps(func) for func in pl[2]]
		self.criteria_list = pl[3]
		solver = pl[4]

		self.name = desc
		self.Scheme = scheme_name
		self.ResultFile = result_name
		self.Solver = solver

		self.SolverParameters = []
		self.OpenSign = pl[5]
		self.CloseSign = pl[6]
		self.inData = None
		self.status = 0
		self.log = ""