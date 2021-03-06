# -*- coding: cp1251 -*-

#***************************************************************************
#
#    copyright            : (C) 2013 by Valery Ovchinnikov (LADUGA Ltd.)
#                                       Anton Lapshin
#                                       Anton Kargin
#    email                : laduga@laduga.com
#***************************************************************************
#***************************************************************************
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU General Public License as published by  *
#*   the Free Software Foundation; either version 2 of the License, or     *
#*   (at your option) any later version.                                   *
#*                                                                         *
#***************************************************************************/
from deap import base, creator, tools
import numpy as np
import random
from multigrid.solvers.python import PythonLoadcase
from multigrid import map as multimap

tb = base.Toolbox()

class GA():
	def __init__(self, nl, pl, desc="GA"):
		"""
		Parameters:
		loadcases - list of loadcases
		vl - list of variables
		f - objective function
		cxpb - probability of crossover
		mutpb - probability of mutation
		pop_size - size of population (amount of individuals in population)
		ngen - amount of generations
		d - dimension of the objective function
		"""
		creator.create("Minimization", base.Fitness, weights=(-1.0,))
		creator.create("Individual", np.ndarray, fitness=creator.Minimization)
		self.loadcase = pl[0]
		self.vl = pl[1]
		self.f = pl[2]
		self.cxpb = pl[3]
		self.mutpb = pl[4]
		self.indpb = pl[5]
		self.pop_size = pl[6]
		self.ngen = pl[7]
		self.d = len(self.vl)
		tb.register("individual", self.init_ind, creator.Individual, self.vl)
		tb.register("population", tools.initRepeat, list, tb.individual, self.pop_size)
		self.pop = tb.population()
		tb.register("evaluate", self.evaluate, objective_func=self.f)
		tb.register("sel_best_half", tools.selBest, k=self.pop_size / 2)
		tb.register("select", tools.selTournament, tournsize=3)
		tb.register("mate", self.cxOnePointCopy)
		tb.register("mutate", self.mutation_operator, vl=self.vl, indpb=0.05)

	def init_ind(self, ind_class, vl):
		ind = ind_class(np.random.uniform(variable.Min, variable.Max) for variable in vl)
		return ind

	def evaluate(self, individuals, objective_func):
		# if list "individuals" is empty, then return empty list
		if not individuals:
			return []
		input_list = []
		for ind in individuals:
			ind_dict = {}
			for i in xrange(len(ind)):
				ind_dict[self.vl[i].Name] = ind[i]
			input_list.append(ind_dict)
		result_list = multimap(self.loadcase, input_list)[self.loadcase.name]
		p_lc = PythonLoadcase(objective_func, desc='p_lc')
		fitnesses = multimap(p_lc, result_list)[p_lc.name]

		return fitnesses

	def cxOnePointCopy(self, ind1, ind2):
		"""Execute a one point crossover with copy on the input individuals. The
		copy is required because the slicing in numpy returns a view of the data,
		which leads to a self overwritting in the swap operation.

		"""
		size = min(len(ind1), len(ind2))
		cxpoint = random.randint(1, size - 1)
		ind1[cxpoint:], ind2[cxpoint:] \
			= ind2[cxpoint:].copy(), ind1[cxpoint:].copy()

		return ind1, ind2

	def cxTwoPointCopy(self, ind1, ind2):
		"""Execute a two points crossover with copy on the input individuals. The
		copy is required because the slicing in numpy returns a view of the data,
		which leads to a self overwritting in the swap operation.

		"""
		size = len(ind1)
		cxpoint1 = random.randint(1, size)
		cxpoint2 = random.randint(1, size - 1)
		if cxpoint2 >= cxpoint1:
			cxpoint2 += 1
		else: # Swap the two cx points
			cxpoint1, cxpoint2 = cxpoint2, cxpoint1

		ind1[cxpoint1:cxpoint2], ind2[cxpoint1:cxpoint2] \
			= ind2[cxpoint1:cxpoint2].copy(), ind1[cxpoint1:cxpoint2].copy()

		return ind1, ind2

	def mutation_operator(self, individual, vl, indpb):
		"""This function applies a mutation.
		i-th component of individual represents a variable of objective function.
		If mutation occurs, then i-th component becomes a random number within bounds,
		that correspond to i-th variable of objective function.
		"""
		size = len(individual)

		for i in xrange(size):
			if random.random() < indpb:
				individual[i] = np.random.uniform(vl[i].Min, vl[i].Max)

		return individual,

	def run(self):
		random.seed(64)
		pop, cxpb, mutpb, ngen = self.pop, self.cxpb, self.mutpb, self.ngen
		best = np.inf
		best_ind = None
		# Evaluate the entire population
		fitnesses = tb.evaluate(pop)
		for ind, fit in zip(pop, fitnesses):
			ind.fitness.values = fit
		for g in range(ngen):
			# Select the next generation individuals
			offspring = tb.select(pop, len(pop))

			# Apply crossover and mutation on the offspring
			for child1, child2 in zip(offspring[::2], offspring[1::2]):
				if random.random() < cxpb:
					tb.mate(child1, child2)
					del child1.fitness.values
					del child2.fitness.values

			for mutant in offspring:
				if random.random() < mutpb:
					tb.mutate(mutant)
					del mutant.fitness.values

			# Evaluate the individuals with an invalid fitness
			invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
			fitnesses = tb.evaluate(invalid_ind)
			for ind, fit in zip(invalid_ind, fitnesses):
				ind.fitness.values = fit

			# The population is entirely replaced by the offspring
			pop[:] = offspring
			print('Generation %i created' % (g+1))
		best_ind = tools.selBest(pop, 1)[0]
		print 'best ind: ', best_ind
		print 'fitness value: ', best_ind.fitness.values
		return pop

	def run_2(self):
		"""This algorithm uses elitism. It selects best half of individuals from population and moves them to the
		offspring. The second half of the offspring is gotten from crossover and mutation of that first half of
		individuals.
		"""
		random.seed(64)
		pop, cxpb, mutpb, ngen = self.pop, self.cxpb, self.mutpb, self.ngen
		best = 0.0
		best_ind = None
		# Evaluate the entire population
		fitnesses = tb.evaluate(pop)
		for ind, fit in zip(self.pop, fitnesses):
			ind.fitness.values = fit
		for g in range(ngen):
			# Select the next generation individuals
			elite_offspring = tb.sel_best_half(pop)
			# Clone the selected individuals
			cx_mut_offspring = map(tb.clone, elite_offspring)

			# Apply crossover and mutation on the offspring
			for child1, child2 in zip(cx_mut_offspring[::2], cx_mut_offspring[1::2]):
				if random.random() < cxpb:
					tb.mate(child1, child2)
					del child1.fitness.values
					del child2.fitness.values

			for mutant in cx_mut_offspring:
				if random.random() < mutpb:
					tb.mutate(mutant)
					del mutant.fitness.values
			offspring = elite_offspring + cx_mut_offspring
			# Evaluate the individuals with an invalid fitness
			invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
			fitnesses = tb.evaluate(invalid_ind)
			for ind, fit in zip(invalid_ind, fitnesses):
				ind.fitness.values = fit

			# The population is entirely replaced by the offspring
			pop[:] = offspring
			print('Generation %i created' % (g+1))
		best_ind = tools.selBest(pop, 1)[0]
		print 'best ind: ', best_ind
		print 'fitness value: ', best_ind.fitness.values
		return pop