import af
from glb import *
import sys
import os
import traceback
import getopt

from structs import *
from types import *
from ParameterValues import *

default = 17777.0
psl_fragment = 2
psl_data =1

solverName = os.getenv("DINSYS")+"\dinama\pradis32\slang"
isSlang    = 1
postName = os.getenv("DINSYS")+"\dinama\post\Postprocessor"
solverFileName = ""
postFileName = ""


from OVP import *
from copy import deepcopy

def unpackDataFromList(pl):
	import Data 
	pnew = []
	for i in pl:
		if isinstance(i, Data.Data):
			prm = i.GetOriginalValue()
		else:
			prm = i	
		prm = deepcopy (prm)
		pnew.append(prm)
	return pnew

def unpackData(i):
	import Data 
	if isinstance(i, Data.Data):
		prm = i.GetOriginalValue()
	else:
		prm = i	
	return prm


def Base (list):
	for p in list:
		if p.__class__ == DOF:
			p.SetBase (1)
		else:
			list = p.GetDOFList()
			for i in range (list.GetSize()):
				d = af.DOF1 (list.GetAt (i+1))
				d.SetBase (1)
		
def External (list):
	for p in list:
		list = p.GetDOFList()

		for i in range (list.GetSize()):
			d = af.DOF1 (list.GetAt (i+1))
			d.SetExternal (1)

def ppl_scheme_desc (desc, name):	
	if (desc == ""):
		return glb.sch.GetDescription()+'.' + name
	return desc+"."+name

def PradisInit (desc):
	glb.sch.SetDescription (desc)
#	glb._scheme_desc = desc
	file_name = sys.argv[0] + ".psl"
	file_name = file_name.replace(".py.",".") 
	del_fn = file_name+".DAT"
	b = os.access (del_fn, os.F_OK)
	if (b == False):
		return
	a = os.access (del_fn, os.W_OK)
#	print 'a=',a
	if a==True:
		os.remove (del_fn)
#	af.StringParameters.SetName (file_name)
		
def SetSolver (sn):
	misc.isSlang = 0
	misc.solverName = sn

def SetSolverFile (sf):
	misc.solverFileName = sf

def SetPost (pr):
	misc.postName = pr
	
def SetPostFile (fn):
	misc.postFileName = fn

def SetSlang():
	SetSolver (os.getenv("DINSYS")+"\dinama\pradis32\slang")
	misc.isSlang = 1
	file_name = sys.argv[0] + ".psl"
	file_name = file_name.replace(".py.",".") 
	SetSolverFile (file_name)
	del_fn = file_name+".DAT"
	SetPostFile (del_fn)
		
def Run ():
#	gen = af.PSLGenerator ()
#	file_name = sys.argv[0] + ".psl"
#	file_name = file_name.replace(".py.",".") 
#	gen.SaveToFile (doc, file_name)
#	cwd = file_name
#test
#	print cwd
#	slang = os.getenv("DINSYS")+"\dinama\pradis32\slang"
	if misc.isSlang == 1:
		PSLCreate()
	if misc.solverName != "":
		os.spawnve(os.P_WAIT, misc.solverName, [misc.solverName, misc.solverFileName], os.environ) 

def PreView3D ():
	misc.SetSlang()
	if misc.isSlang == 1:
		PSLCreate(mode = 1)
	
	if misc.solverName != "":
		os.spawnve(os.P_WAIT, misc.solverName, [misc.solverName, misc.solverFileName], os.environ) 

def Post ():
	if misc.postName == "":
		return
	opts, arg = getopt.getopt(sys.argv[1:], "", ["post"])
#	print opts, arg
	for o, a in opts:
		if o =="--post":
			os.spawnve(os.P_WAIT, misc.postName, [misc.postName, misc.postFileName], os.environ) 

#def PSLCreate ():
#	PSLCreate_ (0)
	
def PSLCreate (mode = 0):
	gen = af.PSLGenerator ()
	file_name = sys.argv[0] + ".psl"
	file_name = file_name.replace(".py.",".") 
	gen.SaveToFile (doc, file_name, mode)

def writeError(text):
#	fd = file ()
	fd = open("SYSPRINT.TXT", "a")
#	a,b,c = sys.exc_info()
#	sys.excepthook (a,b,c)

	strt = "\nPPL:\n    PPL executing error:" + text + "\n"
	fd.write (strt)
	traceback.print_exc(None, fd)
	fd.close()
	
def Remove (el):
	sch_main.RemoveElement (el)

def Expand (l):
	p = []
#	print 'l=', l,'   ', l.__class__
	if l.__class__ != list:
		if isinstance(l, ParameterValues):
		
	#		print l
			
			pv = l.Values()
			ip = Expand (pv)
			for n in ip:
				p.append (n)
			return p

		p.append (l)
		return p

	for i in l:
		if i.__class__ == list:
			ip = Expand (i)
			for n in ip:
				p.append (n)
		else:
			if isinstance(i, ParameterValues):
			
#				print i
			
				pv = i.Values()
				ip = Expand (pv)
				for n in ip:
					p.append (n)
			else:
				p.append (i)
	return p

def Append (par, l):
	for i in range(len(l)):
		par.append(l[i])

def AddModel (name, nl, pl, desc=default):
	mdlist = sch.GetModelList()
	mdl = af.Model (mdlist.Add())
	mdl.SetObjectName (name)
	if desc != default:
		mdl.SetDescription(desc)
	misc.AddParameters (mdl, pl)
	ndlist = af.TList (mdl.SetNodeList())
	for i in nl:
		ndlist.Add(i)
	return mdl

def AddOVP (name, nl, pl, desc=default):
#	ovplist = sch.GetOutVariableList()
	ovp = OVP (name, nl, pl)
	if desc != default:
		ovp.SetDescription(desc)		
# ovp.SetObjectName (prvp)
# prmlist = af.TList (ovp.SetParameterList())
# for i in pl:
# 	prm = af.TReal (prmlist.Add())
# 	prm.SetValue (i)
# OVList = af.TList (ovp.SetOutValueList())
# hlp = OutValue ()
# for i in nl:
# 	ov = af.OutValue (OVList.Add())
# 	if hlp.__class__ != i.__class__ :
# 		ov.SetOutValueType (1)
# 		ov.SetNodeOfValue (i)
# 	else:
# 		ov.SetOutValueType (i.type)
# 		if i.type == 2 or i.type == 3:
# 			ov.SetNodeOfValue (i.node)
# 		else:
# 			ov.SetNumber (i.number)
# 			ov.SetModelOfValue (i.model)
	return ovp


def Clean ():
	sch_main.ClearElements()
	sch_main.SetFragmentList()
	sch_main.SetNodeList()
	sch_main.SetPrintList()
	sch_main.SetRunList()
	sch_main.SetImageList()
	sch_main.SetOutVariableList()
	sch_main.SetModelList()
	sch_main.SetDataList()
	sch_main.SetIncludeList()
	sch_main.SetObjectName("MAIN")

def AddImage (pgo, model, pgoparams, lp, desc=default):
	ilist = sch.GetImageList()
	img = af.Image (ilist.Add())
	img.SetObjectName (pgo)
	if desc != default:
		img.SetDescription(desc)	
	if model != None:
		img.SetImageModel (model)
		

#	print 'pgoparams=',pgoparams
	misc.AddParameters (img, pgoparams)
#	pgoparams = Expand (pgoparams)
#	pl = af.TList (img.SetParameterList())
#	for i in pgoparams:
#		r = af.TReal (pl.Add())
#		r.SetValue (i)
	layer = af.Layer (img.SetLayerParameters())
	if len (lp) == 0:
		lp = ['YELLOW','gold',1.0]
	layer.SetColor (lp[0])
	layer.SetMaterial (lp[1])
	layer.SetTransparency (lp[2])
	return img

def AddParameters (obj, pl):
	prmlist = af.TList (obj.SetParameterList())
	par = misc.Expand (pl)
#	print "par=",par
	for i in par:
		if type(i) is StringType:
			prm = af.TString (prmlist.Add())
			prm.SetValue (i)
			
			
			
			
		if type(i) is FloatType:
			prm = af.TReal (prmlist.Add())
			prm.SetValue (float(i))
		if type(i) is IntType or type(i) is LongType:
			prm = af.TReal (prmlist.Add())
#			print i
			prm.SetValue (float(i))
		if isinstance(i, af.TString):
			prm = af.TString (prmlist.Add())
			prm.SetValue (i.GetValue())
			prm.SetName(i.GetName())
#			print "prm=",i.GetValue()
		if isinstance(i, ParameterValues):
			p = Expand (i)
			AddParameters (obj, p)
			print p
