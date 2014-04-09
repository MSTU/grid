import os
import subprocess
import unittest
import local_test
from multigrid.multigrid import MultiGrid


class RemoteTest(local_test.LocalTest):
	@classmethod
	def setUpClass(cls):
		cls.subprocesses = []
		cls.mg = MultiGrid(False)
		cwd = os.getcwd()
		os.chdir('..')
		worker = subprocess.Popen(['celery', '-A', 'remoteworker', 'worker', '--concurrency', '1' ])
		cls.subprocesses.append(worker)
		os.chdir(cwd)

	@classmethod
	def tearDownClass(cls):
		for subprocess in cls.subprocesses:
			subprocess.kill()
		cls.subprocesses = []


def test_suite():
	return unittest.TestLoader().loadTestsFromTestCase(local_test.LocalTest)


if __name__ == '__main__':
	unittest.main()