import unittest
from multigrid.solvers import modelica


class ModelicaTest(unittest.TestCase):
	def setUp(self):
		pass

	def test_1(self):
		par = dict()
		par['startTime'] = 0.0
		par['stopTime'] = 10.0
		par['numberOfIntervals'] = 5

		result = modelica.create_mos_by_mo('dcmotor.mo', par)
		print result



def test_suite():
	return unittest.TestLoader().loadTestsFromTestCase(ModelicaTest)


if __name__ == '__main__':
	unittest.main()