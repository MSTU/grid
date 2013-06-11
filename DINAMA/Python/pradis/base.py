# This file was created automatically by SWIG 1.3.30.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _base
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


class Facet(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Facet, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Facet, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _base.new_Facet(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _base.delete_Facet
    __del__ = lambda self : None;
    def SetObjectName(*args): return _base.Facet_SetObjectName(*args)
    def SetTaskName(*args): return _base.Facet_SetTaskName(*args)
    def SetScheme(*args): return _base.Facet_SetScheme(*args)
    def SetAngle(*args): return _base.Facet_SetAngle(*args)
    def SetDeflection(*args): return _base.Facet_SetDeflection(*args)
    def SetRelative(*args): return _base.Facet_SetRelative(*args)
    def SetFacet(*args): return _base.Facet_SetFacet(*args)
    def GetMeshFile(*args): return _base.Facet_GetMeshFile(*args)
    def GetList(*args): return _base.Facet_GetList(*args)
Facet_swigregister = _base.Facet_swigregister
Facet_swigregister(Facet)

class GeomImportExport(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, GeomImportExport, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, GeomImportExport, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _base.new_GeomImportExport(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _base.delete_GeomImportExport
    __del__ = lambda self : None;
    def Read(*args): return _base.GeomImportExport_Read(*args)
    def Save(*args): return _base.GeomImportExport_Save(*args)
    def ReadBREP(*args): return _base.GeomImportExport_ReadBREP(*args)
    def SaveBREP(*args): return _base.GeomImportExport_SaveBREP(*args)
    def ReadIGES(*args): return _base.GeomImportExport_ReadIGES(*args)
    def SaveIGES(*args): return _base.GeomImportExport_SaveIGES(*args)
    def ReadSTEP(*args): return _base.GeomImportExport_ReadSTEP(*args)
    def SaveSTEP(*args): return _base.GeomImportExport_SaveSTEP(*args)
    def SaveSTL(*args): return _base.GeomImportExport_SaveSTL(*args)
    def SaveVRML(*args): return _base.GeomImportExport_SaveVRML(*args)
GeomImportExport_swigregister = _base.GeomImportExport_swigregister
GeomImportExport_swigregister(GeomImportExport)

GetEnv = _base.GetEnv
ExecCommand = _base.ExecCommand


