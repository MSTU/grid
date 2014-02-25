from solvers.pythonsolver import PythonSolver
from solvers.modelicasolver import ModelicaSolver

solver_name_to_class = dict()
solver_name_to_class[PythonSolver.name] = PythonSolver
solver_name_to_class[ModelicaSolver.name] = ModelicaSolver

solvers = dict()

def get_solver(name):
	if not name in solvers:
		solvers[name] = solver_name_to_class[name]()
	return solvers[name]

BROKER_URL = 'amqp://guest@localhost//'
CELERY_RESULT_BACKEND = 'amqp'

#CELERY_ROUTES = {'grid.Worker.RunTask': {'queue': 'default'}, 'Worker.TestTask': {'queue': 'default'}}