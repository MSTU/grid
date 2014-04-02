import os
import subprocess
import unittest
import local_tests
from multigrid.modelgrid import ModelGrid


class RemoteTest(local_tests.LocalTest):
	@classmethod
	def setUpClass(cls):
		cls.subprocesses = []
		cls.mg = ModelGrid(False)
		cwd = os.getcwd()
		os.chdir('../multigrid/')
		worker = subprocess.Popen(['celery', '-A', 'remoteworker', 'worker', '--concurrency', '1' ])
		cls.subprocesses.append(worker)
		os.chdir(cwd)

	@classmethod
	def tearDownClass(cls):
		for subprocess in cls.subprocesses:
			subprocess.kill()
		cls.subprocesses = []


def test_suite():
	return unittest.TestLoader().loadTestsFromTestCase(local_tests.LocalTest)


if __name__ == '__main__':
	unittest.main()