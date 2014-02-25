from solvers import pythonsolver
from solvers import modelicasolver

solver_name_to_class = dict()
solver_name_to_class[pythonsolver.name] = pythonsolver.PythonSolver
solver_name_to_class[modelicasolver.name] = modelicasolver.ModelicaSolver

solvers = dict()

def get_solver(name):
	if not name in solvers:
		solvers[name] = solver_name_to_class[name]()
	return solvers[name]

BROKER_URL = 'amqp://guest@localhost//'
CELERY_RESULT_BACKEND = 'amqp'

#CELERY_ROUTES = {'grid.Worker.RunTask': {'queue': 'default'}, 'Worker.TestTask': {'queue': 'default'}}