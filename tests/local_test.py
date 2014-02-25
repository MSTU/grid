import unittest

from multigrid.multigrid import MultiGrid
from solvers.modelicasolver import ModelicaLoadcase
from solvers.pythonsolver import PythonLoadcase

def f(x):
	return x * x

class LocalTest(unittest.TestCase):
	def setUp(self):
		self.mg = MultiGrid(False)

	def test_1(self):
		lc = PythonLoadcase(f)
		input_list = range(1, 10)
		result_list = self.mg.map(lc, input_list)[f.__name__]
		self.assertEqual(result_list, map(f, input_list))

	def test_2(self):
		lc_name = 'lc'
		lc = ModelicaLoadcase('mos/mydcmotor.mos', lc_name)
		input_list = []

		par = dict()
		par['resistor1.R'] = 5.0
		par['inductor1.L'] = 0.4
		par['load.J'] = 2.0
		input_list.append(par)

		par = dict()
		par['resistor1.R'] = 2.0
		par['inductor1.L'] = 1.0
		par['load.J'] = 0.5
		input_list.append(par)

		result = self.mg.map(lc, input_list)

	def test_3(self):
		lc_name = 'lc'
		lc = ModelicaLoadcase('mos/mydcmotor.mos', lc_name)

		input = dict()
		input['resistor1.R'] = [5.0, 2.0]
		input['inductor1.L'] = [0.4, 1.0]
		input['load.J'] = [2.0, 0.5]

		result = self.mg.map(lc, input)

def test_suite():
	return unittest.TestLoader().loadTestsFromTestCase(LocalTest)


if __name__ == '__main__':
	unittest.main()