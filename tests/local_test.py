import unittest

from multigrid.multigrid import MultiGrid
from solvers.pythonsolver import PythonLoadcase

def f(x):
	return x * x

class LocalTest(unittest.TestCase):
	def setUp(self):
		self.mg = MultiGrid(True)

	def test_1(self):
		lc = PythonLoadcase(f)
		input_list = range(1, 10)
		result_list = self.mg.map(lc, input_list)[f.__name__]
		self.assertEqual(result_list, map(f, input_list))


def test_suite():
	return unittest.TestLoader().loadTestsFromTestCase(LocalTest)


if __name__ == '__main__':
	unittest.main()