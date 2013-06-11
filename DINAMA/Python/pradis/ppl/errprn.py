import af
import glb

def GetStr (f, num):
	f.seek (200 * (num - 1) + 18)
	return f.read (181)

def ErrPrnMdl (errnum, nm, *args):
	dir = af.GetEnv ("DINSYS")
	f = open (dir + "/DINAMA/sysarm/error.dat", "r")
	s = GetStr (f, 2000)
	print s.rstrip()
	s = GetStr (f, 2001)
	print s.rstrip() % glb.sch.GetObjectName()
	s = GetStr (f, 2002)
	l = af.TList (glb.sch.GetModelList())
	i = l.GetSize() + 1
	print s.rstrip() % i
	s = GetStr (f, 2003)
	print s.rstrip() % nm
	s = GetStr (f, errnum)
	print s.rstrip() % args
	f.close()

def ErrPrnPRVP (errnum, nm, *args):
	dir = af.GetEnv ("DINSYS")
	f = open (dir + "/DINAMA/sysarm/error.dat", "r")
	s = GetStr (f, 2011)
	print s.rstrip()
	s = GetStr (f, 2001)
	print s.rstrip() % glb.sch.GetObjectName()
	s = GetStr (f, 2012)
	l = af.TList (glb.sch.GetOutVariableList())
	i = l.GetSize() + 1
	print s.rstrip() % i
	s = GetStr (f, 2013)
	print s.rstrip() % nm
	s = GetStr (f, errnum)
	print s.rstrip() % args
	f.close()

def ErrPrnPGO (errnum, nm, *args):
	dir = af.GetEnv ("DINSYS")
	f = open (dir + "/DINAMA/sysarm/error.dat", "r")
	s = GetStr (f, 2019)
	print s.rstrip()
	s = GetStr (f, 2001)
	print s.rstrip() % glb.sch.GetObjectName()
	s = GetStr (f, 2020)
	l = af.TList (glb.sch.GetImageList())
	i = l.GetSize() + 1
	print s.rstrip() % i
	s = GetStr (f, 2021)
	print s.rstrip() % nm
	s = GetStr (f, errnum)
	print s.rstrip() % args
	f.close()
