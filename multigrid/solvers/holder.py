"""
Hold instances of solvers
"""

import python
import modelica

solver_name_to_class = dict()
solver_name_to_class[python.name] = python.PythonSolver
solver_name_to_class[modelica.name] = modelica.ModelicaSolver

solvers = dict()

def get_solver(name):
	if not name in solvers:
		solvers[name] = solver_name_to_class[name]()
	return solvers[name]