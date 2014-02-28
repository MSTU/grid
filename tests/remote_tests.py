import unittest
import local_test
from multigrid.multigrid import MultiGrid


class RemoteTest(local_test.LocalTest):
	def setUp(self):
		self.mg = MultiGrid(False)

def test_suite():
	return unittest.TestLoader().loadTestsFromTestCase(local_test.LocalTest)


if __name__ == '__main__':
	unittest.main()