import unittest

from multigrid.multigrid import MultiGrid, _dict_to_list, _list_to_dict


def f(x):
	return x * x

class MultiGridTest(unittest.TestCase):
	def setUp(self):
		pass

	def test_1(self):
		a = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
		b = _list_to_dict(a)
		self.assertEqual(b, {'a': [1, 3], 'b': [2, 4]})

	def test_2(self):
		a = {'a': [1, 3], 'b': [2, 4]}
		b = _dict_to_list(a)
		self.assertEqual(b, [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}])


def test_suite():
	return unittest.TestLoader().loadTestsFromTestCase(MultiGridTest)


if __name__ == '__main__':
	unittest.main()