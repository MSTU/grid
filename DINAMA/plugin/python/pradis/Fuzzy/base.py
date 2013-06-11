
import fuzzy.norm.Max 
import fuzzy.operator.Not 
import pradis.Fuzzy.Erosion 
import fuzzy.norm.Min 
#from fuzzy.norm.BoundedDifference import BoundedDifference
#from fuzzy.norm.DrasticSum import DrasticSum
import fuzzy.norm.EinsteinSum 
import fuzzy.norm.DombiUnion 

import fuzzy.norm.AlgebraicProduct 
import fuzzy.norm.AlgebraicSum 
import fuzzy.operator.Const
#from fuzzy.set.Polygon import Polygon


def getList (inputs):
	a_list = []
#	print inputs
	for i in inputs:
		if isinstance(i, pradis.Fuzzy.Adjective.Adjective): 
			a_list.append (fuzzy.operator.Input.Input(i.adjective))
		elif isinstance (i, float) or isinstance (i, int):
			a_list.append ( fuzzy.operator.Const.Const (i))
		else:
			a_list.append (i)
#	print 'a_list=',a_list
	return a_list

def getOp (inputs):
#	print inputs
	if isinstance(inputs, pradis.Fuzzy.Adjective.Adjective): 
		return fuzzy.operator.Input.Input(inputs.adjective)
	if isinstance(inputs, fuzzy.Adjective.Adjective): 
		return fuzzy.operator.Input.Input(inputs)
	return inputs

def Max (*inputs): 
	return fuzzy.operator.Compound.Compound(fuzzy.norm.Max.Max(), *getList(inputs)) 

def Min (*inputs): 
	return fuzzy.operator.Compound.Compound(fuzzy.norm.Min.Min(), *getList(inputs)) 
	
def Not (inputs): 
	return fuzzy.operator.Not.Not(getOp(inputs) )
	
def AlgebraicProduct (a,b): 
	return fuzzy.operator.Compound.Compound(fuzzy.norm.AlgebraicProduct.AlgebraicProduct(), getOp(a),getOp(b) )
	
def AlgebraicSum (a,b): 
	return fuzzy.operator.Compound.Compound(fuzzy.norm.AlgebraicSum.AlgebraicSum(), getOp(a),getOp(b)) 
	
def EinsteinSum (a,b): 
	return fuzzy.operator.Compound.Compound(fuzzy.norm.EinsteinSum.EinsteinSum(), getOp(a),getOp(b)) 
	
def DombiUnion (a,b): 
	return fuzzy.operator.Compound.Compound(fuzzy.norm.DombiUnion.DombiUnion(), getOp(a),getOp(b)) 
	
	
def Very (inputs): 
#	return fuzzy.operator.Compound.Compound(fuzzy.norm.AlgebraicProduct.AlgebraicProduct(), getOp(inputs),getOp(inputs) )
	return fuzzy.operator.Compound.Compound(pradis.Fuzzy.Erosion.ErosionNorm(6.0), getOp(inputs), getOp(inputs)) 

def NotVery (inputs): 
	return fuzzy.operator.Compound.Compound(pradis.Fuzzy.Erosion.ErosionNorm(1.0/6.0), getOp(inputs), getOp(inputs)) 
	
def Over (inputs): 
	return fuzzy.operator.Compound.Compound(pradis.Fuzzy.Erosion.ErosionNorm(3.0), getOp(inputs), getOp(inputs)) 
	
def Less (inputs): 
	return fuzzy.operator.Compound.Compound(pradis.Fuzzy.Erosion.ErosionNorm(1.0/3.0), getOp(inputs), getOp(inputs)) 
	
	