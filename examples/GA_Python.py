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
from numpy import sin
from numpy.random import random_sample
from pradis.multi.Variable import Variable

tb = base.Toolbox()

def evaluate(args):
	# minimum at -18.5
	x = args[0]
	y = args[1]
	return (1-(x**2+y**3))*np.exp(-(x**2+y**2)/2),
	#return x * sin(4*x) + 1.1 * y * sin(2*y),

class GA():
	def __init__(self, nl, pl, desc="GA"):
		"""
		Parameters:
		vl - list of variables
		d - dimension of the objective function
		f - objective function
		cxpb - probability of crossover
		mutpb - probability of mutation
		pop_size - size of population (amount of individuals in population)
		ngen - amount of generations
		"""
		creator.create("Minimization", base.Fitness, weights=(-1.0,))
		creator.create("Individual", np.ndarray, fitness=creator.Minimization)
		self.vl = pl[0]
		self.d = len(self.vl)
		self.f = pl[1]
		self.cxpb = pl[2]
		self.mutpb = pl[3]
		self.pop_size = pl[4]
		self.ngen = pl[5]
		tb.register("individual", self.init_ind, creator.Individual, self.vl)
		tb.register("population", tools.initRepeat, list, tb.individual, self.pop_size)
		self.pop = tb.population()
		tb.register("evaluate", evaluate)
		#tb.register("select", tools.selBest, k=self.pop_size / 2)
		tb.register("sel_best", tools.selBest, k=self.pop_size / 2)
		tb.register("select", tools.selTournament, tournsize=3)
		tb.register("mate", self.cxOnePointCopy)
		tb.register("mutate", self.mutation_operator, vl=self.vl, indpb=0.1)

	def init_ind(self, ind_class, vl):
		ind = ind_class(np.random.uniform(variable.Min, variable.Max) for variable in vl)
		return ind

	def cxOnePointCopy(self, ind1, ind2):
		"""Execute a one point crossover with copy on the input individuals. The
		copy is required because the slicing in numpy returns a view of the data,
		which leads to a self overwritting in the swap operation.

		"""
		size = min(len(ind1), len(ind2))
		cxpoint = np.random.random_integers(1, size - 1)
		ind1[cxpoint:], ind2[cxpoint:] \
			= ind2[cxpoint:].copy(), ind1[cxpoint:].copy()

		return ind1, ind2

	def cxTwoPointCopy(self, ind1, ind2):
		"""Execute a two points crossover with copy on the input individuals. The
		copy is required because the slicing in numpy returns a view of the data,
		which leads to a self overwritting in the swap operation.

		"""
		size = len(ind1)
		cxpoint1 = np.random.random_integers(1, size)
		cxpoint2 = np.random.random_integers(1, size - 1)
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
			if random_sample() < indpb:
				individual[i] = np.random.uniform(vl[i].Min, vl[i].Max)

		return individual,

	def run(self):
		# Evaluate the entire population
		pop, cxpb, mutpb, ngen = self.pop, self.cxpb, self.mutpb, self.ngen
		fitnesses = map(tb.evaluate, pop)
		for ind, fit in zip(self.pop, fitnesses):
			ind.fitness.values = fit

		best = 0.0

		for g in range(ngen):
			# Select the next generation individuals
			offspring = tb.select(pop, len(pop))
			# Clone the selected individuals
			offspring = map(tb.clone, offspring)

			# Apply crossover and mutation on the offspring
			for child1, child2 in zip(offspring[::2], offspring[1::2]):
				if random_sample() < cxpb:
					tb.mate(child1, child2)
					del child1.fitness.values
					del child2.fitness.values

			for mutant in offspring:
				if random_sample() < mutpb:
					tb.mutate(mutant)
					del mutant.fitness.values

			# Evaluate the individuals with an invalid fitness
			invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
			fitnesses = map(tb.evaluate, invalid_ind)
			for ind, fit in zip(invalid_ind, fitnesses):
				ind.fitness.values = fit

			# The population is entirely replaced by the offspring
			pop[:] = offspring
			sample = evaluate(tools.selBest(pop, 1)[0])
			if sample[0] < best:
				best = sample[0]
		print best
		return pop

	def run_2(self):
		"""This algorithm uses elitism. It selects best half of individuals from population and moves them to the
		offspring. The second half of the offspring is gotten from crossover and mutation of that first half of
		individuals.
		"""
		# Evaluate the entire population
		pop, cxpb, mutpb, ngen = self.pop, self.cxpb, self.mutpb, self.ngen
		fitnesses = map(tb.evaluate, pop)
		for ind, fit in zip(self.pop, fitnesses):
			ind.fitness.values = fit
		best = 0.0
		for g in range(ngen):
			# Select the next generation individuals
			elite_offspring = tb.sel_best(pop)
			# Clone the selected individuals
			cx_mut_offspring = map(tb.clone, elite_offspring)

			# Apply crossover and mutation on the offspring
			for child1, child2 in zip(cx_mut_offspring[::2], cx_mut_offspring[1::2]):
				if random_sample() < cxpb:
					tb.mate(child1, child2)
					del child1.fitness.values
					del child2.fitness.values

			for mutant in cx_mut_offspring:
				if random_sample() < mutpb:
					tb.mutate(mutant)
					del mutant.fitness.values
			offspring = elite_offspring + cx_mut_offspring
			# Evaluate the individuals with an invalid fitness
			invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
			fitnesses = map(tb.evaluate, invalid_ind)
			for ind, fit in zip(invalid_ind, fitnesses):
				ind.fitness.values = fit

			# The population is entirely replaced by the offspring
			pop[:] = offspring
			sample = evaluate(tools.selBest(pop, 1)[0])
			if sample[0] < best:
				best = sample[0]
		print best
		return pop

v1 = Variable("", ['v1', -0.1, -3.0, 3.0])
v2 = Variable("", ['v2', -1.6, -3.0, 3.0])
vl = [v1, v2]
ga = GA('', [vl, evaluate, 0.50, 0.20, 100, 30])
ga.run()
