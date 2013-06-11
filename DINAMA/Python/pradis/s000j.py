# This file was created automatically by SWIG 1.3.30.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _s000j
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


W_S0001 = _s000j.W_S0001
W_S0002 = _s000j.W_S0002
W_S0003 = _s000j.W_S0003
W_S0004 = _s000j.W_S0004
W_S0005 = _s000j.W_S0005
W_S0007 = _s000j.W_S0007
W_S0008 = _s000j.W_S0008
W_S0010 = _s000j.W_S0010
W_S0011 = _s000j.W_S0011
W_S0011A = _s000j.W_S0011A
W_S0012 = _s000j.W_S0012
W_S0014 = _s000j.W_S0014
W_S0015 = _s000j.W_S0015
W_S0016 = _s000j.W_S0016
W_S0017 = _s000j.W_S0017
W_S0017A = _s000j.W_S0017A
W_S0020 = _s000j.W_S0020
W_S0021 = _s000j.W_S0021
W_S0022 = _s000j.W_S0022
W_S0022A = _s000j.W_S0022A
W_S0022B = _s000j.W_S0022B
W_S0024 = _s000j.W_S0024
W_S0025 = _s000j.W_S0025
W_S0026 = _s000j.W_S0026
W_S0027 = _s000j.W_S0027
W_S0028 = _s000j.W_S0028
W_S0029 = _s000j.W_S0029
W_S0030 = _s000j.W_S0030
W_S0031 = _s000j.W_S0031
W_S0032 = _s000j.W_S0032
W_S0033 = _s000j.W_S0033
W_S0264 = _s000j.W_S0264
class S000J(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, S000J, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, S000J, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _s000j.new_S000J(*args)
        try: self.this.append(this)
        except: self.this = this
    def f4(*args): return _s000j.S000J_f4(*args)
    def new_darray(*args): return _s000j.S000J_new_darray(*args)
    def darray_get(*args): return _s000j.S000J_darray_get(*args)
    def darray_set(*args): return _s000j.S000J_darray_set(*args)
    def new_iarray(*args): return _s000j.S000J_new_iarray(*args)
    def iarray_get(*args): return _s000j.S000J_iarray_get(*args)
    def iarray_set(*args): return _s000j.S000J_iarray_set(*args)
    def delete_darray(*args): return _s000j.S000J_delete_darray(*args)
    def S0001(*args): return _s000j.S000J_S0001(*args)
    def S0002(*args): return _s000j.S000J_S0002(*args)
    def S0003(*args): return _s000j.S000J_S0003(*args)
    def S0004(*args): return _s000j.S000J_S0004(*args)
    def S0005(*args): return _s000j.S000J_S0005(*args)
    def S0007(*args): return _s000j.S000J_S0007(*args)
    def S0008(*args): return _s000j.S000J_S0008(*args)
    def S0010(*args): return _s000j.S000J_S0010(*args)
    def S0011(*args): return _s000j.S000J_S0011(*args)
    def S0011A(*args): return _s000j.S000J_S0011A(*args)
    def S0012(*args): return _s000j.S000J_S0012(*args)
    def S0014(*args): return _s000j.S000J_S0014(*args)
    def S0015(*args): return _s000j.S000J_S0015(*args)
    def S0016(*args): return _s000j.S000J_S0016(*args)
    def S0017(*args): return _s000j.S000J_S0017(*args)
    def S0017A(*args): return _s000j.S000J_S0017A(*args)
    def S0020(*args): return _s000j.S000J_S0020(*args)
    def S0021(*args): return _s000j.S000J_S0021(*args)
    def S0022(*args): return _s000j.S000J_S0022(*args)
    def S0022A(*args): return _s000j.S000J_S0022A(*args)
    def S0022B(*args): return _s000j.S000J_S0022B(*args)
    def S0024(*args): return _s000j.S000J_S0024(*args)
    def S0025(*args): return _s000j.S000J_S0025(*args)
    def S0026(*args): return _s000j.S000J_S0026(*args)
    def S0027(*args): return _s000j.S000J_S0027(*args)
    def S0028(*args): return _s000j.S000J_S0028(*args)
    def S0029(*args): return _s000j.S000J_S0029(*args)
    def S0030(*args): return _s000j.S000J_S0030(*args)
    def S0031(*args): return _s000j.S000J_S0031(*args)
    def S0032(*args): return _s000j.S000J_S0032(*args)
    def S0033(*args): return _s000j.S000J_S0033(*args)
    def S0264(*args): return _s000j.S000J_S0264(*args)
    __swig_destroy__ = _s000j.delete_S000J
    __del__ = lambda self : None;
S000J_swigregister = _s000j.S000J_swigregister
S000J_swigregister(S000J)
cvar = _s000j.cvar



