# This file was created automatically by SWIG 1.3.30.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _PradisLog
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


MAX_PAR = _PradisLog.MAX_PAR
MAX_STR_LEN = _PradisLog.MAX_STR_LEN
class PradisLog(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PradisLog, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PradisLog, name)
    __repr__ = _swig_repr
    __swig_getmethods__["error"] = lambda x: _PradisLog.PradisLog_error
    if _newclass:error = staticmethod(_PradisLog.PradisLog_error)
    __swig_getmethods__["_print"] = lambda x: _PradisLog.PradisLog__print
    if _newclass:_print = staticmethod(_PradisLog.PradisLog__print)
    __swig_getmethods__["printr"] = lambda x: _PradisLog.PradisLog_printr
    if _newclass:printr = staticmethod(_PradisLog.PradisLog_printr)
    __swig_getmethods__["perr"] = lambda x: _PradisLog.PradisLog_perr
    if _newclass:perr = staticmethod(_PradisLog.PradisLog_perr)
    __swig_getmethods__["WinToDos"] = lambda x: _PradisLog.PradisLog_WinToDos
    if _newclass:WinToDos = staticmethod(_PradisLog.PradisLog_WinToDos)
    __swig_getmethods__["CloseIOs"] = lambda x: _PradisLog.PradisLog_CloseIOs
    if _newclass:CloseIOs = staticmethod(_PradisLog.PradisLog_CloseIOs)
    def __init__(self, *args): 
        this = _PradisLog.new_PradisLog(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _PradisLog.delete_PradisLog
    __del__ = lambda self : None;
PradisLog_swigregister = _PradisLog.PradisLog_swigregister
PradisLog_swigregister(PradisLog)
PradisLog_error = _PradisLog.PradisLog_error
PradisLog__print = _PradisLog.PradisLog__print
PradisLog_printr = _PradisLog.PradisLog_printr
PradisLog_perr = _PradisLog.PradisLog_perr
PradisLog_WinToDos = _PradisLog.PradisLog_WinToDos
PradisLog_CloseIOs = _PradisLog.PradisLog_CloseIOs



