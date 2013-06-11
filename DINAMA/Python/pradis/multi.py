# This file was created automatically by SWIG 1.3.30.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _multi
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


class Model(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Model, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Model, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _multi.new_Model(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _multi.delete_Model
    __del__ = lambda self : None;
    def SetScheme(*args): return _multi.Model_SetScheme(*args)
    def GetScheme(*args): return _multi.Model_GetScheme(*args)
    def AddParameter(*args): return _multi.Model_AddParameter(*args)
    def SetParameterValue(*args): return _multi.Model_SetParameterValue(*args)
    def GetParameterValue(*args): return _multi.Model_GetParameterValue(*args)
    def AddExtParameter(*args): return _multi.Model_AddExtParameter(*args)
    def SetExtParameterValue(*args): return _multi.Model_SetExtParameterValue(*args)
    def GetExtParameterValue(*args): return _multi.Model_GetExtParameterValue(*args)
    def Reset(*args): return _multi.Model_Reset(*args)
    def AddFunction(*args): return _multi.Model_AddFunction(*args)
    def GetFunctionName(*args): return _multi.Model_GetFunctionName(*args)
    def GetFunctionValue(*args): return _multi.Model_GetFunctionValue(*args)
    def Run(*args): return _multi.Model_Run(*args)
    def SetLayer(*args): return _multi.Model_SetLayer(*args)
    def SetResultFile(*args): return _multi.Model_SetResultFile(*args)
    def SetResultsFormat(*args): return _multi.Model_SetResultsFormat(*args)
    def SetHistoryFile(*args): return _multi.Model_SetHistoryFile(*args)
    def GetHistoryFile(*args): return _multi.Model_GetHistoryFile(*args)
    def SetFilePostfix(*args): return _multi.Model_SetFilePostfix(*args)
    def SetOpenSign(*args): return _multi.Model_SetOpenSign(*args)
    def SetCloseSign(*args): return _multi.Model_SetCloseSign(*args)
    def SetDefaultCommand(*args): return _multi.Model_SetDefaultCommand(*args)
    def SetDescription(*args): return _multi.Model_SetDescription(*args)
    def replaceSymbol(*args): return _multi.Model_replaceSymbol(*args)
    def addPostfix(*args): return _multi.Model_addPostfix(*args)
    __swig_getmethods__["changeExtension"] = lambda x: _multi.Model_changeExtension
    if _newclass:changeExtension = staticmethod(_multi.Model_changeExtension)
    def writeHistory(*args): return _multi.Model_writeHistory(*args)
    def readResults(*args): return _multi.Model_readResults(*args)
    def initHistory(*args): return _multi.Model_initHistory(*args)
    __swig_setmethods__["SC"] = _multi.Model_SC_set
    __swig_getmethods__["SC"] = _multi.Model_SC_get
    if _newclass:SC = _swig_property(_multi.Model_SC_get, _multi.Model_SC_set)
    __swig_setmethods__["myScheme"] = _multi.Model_myScheme_set
    __swig_getmethods__["myScheme"] = _multi.Model_myScheme_get
    if _newclass:myScheme = _swig_property(_multi.Model_myScheme_get, _multi.Model_myScheme_set)
    __swig_setmethods__["myDescription"] = _multi.Model_myDescription_set
    __swig_getmethods__["myDescription"] = _multi.Model_myDescription_get
    if _newclass:myDescription = _swig_property(_multi.Model_myDescription_get, _multi.Model_myDescription_set)
    __swig_setmethods__["myResFile"] = _multi.Model_myResFile_set
    __swig_getmethods__["myResFile"] = _multi.Model_myResFile_get
    if _newclass:myResFile = _swig_property(_multi.Model_myResFile_get, _multi.Model_myResFile_set)
    __swig_setmethods__["myResFormat"] = _multi.Model_myResFormat_set
    __swig_getmethods__["myResFormat"] = _multi.Model_myResFormat_get
    if _newclass:myResFormat = _swig_property(_multi.Model_myResFormat_get, _multi.Model_myResFormat_set)
    __swig_setmethods__["myHistory"] = _multi.Model_myHistory_set
    __swig_getmethods__["myHistory"] = _multi.Model_myHistory_get
    if _newclass:myHistory = _swig_property(_multi.Model_myHistory_get, _multi.Model_myHistory_set)
    __swig_setmethods__["myPostfix"] = _multi.Model_myPostfix_set
    __swig_getmethods__["myPostfix"] = _multi.Model_myPostfix_get
    if _newclass:myPostfix = _swig_property(_multi.Model_myPostfix_get, _multi.Model_myPostfix_set)
    __swig_setmethods__["myOpenSign"] = _multi.Model_myOpenSign_set
    __swig_getmethods__["myOpenSign"] = _multi.Model_myOpenSign_get
    if _newclass:myOpenSign = _swig_property(_multi.Model_myOpenSign_get, _multi.Model_myOpenSign_set)
    __swig_setmethods__["myCloseSign"] = _multi.Model_myCloseSign_set
    __swig_getmethods__["myCloseSign"] = _multi.Model_myCloseSign_get
    if _newclass:myCloseSign = _swig_property(_multi.Model_myCloseSign_get, _multi.Model_myCloseSign_set)
    __swig_setmethods__["FunctionVector"] = _multi.Model_FunctionVector_set
    __swig_getmethods__["FunctionVector"] = _multi.Model_FunctionVector_get
    if _newclass:FunctionVector = _swig_property(_multi.Model_FunctionVector_get, _multi.Model_FunctionVector_set)
    __swig_setmethods__["ParameterVector"] = _multi.Model_ParameterVector_set
    __swig_getmethods__["ParameterVector"] = _multi.Model_ParameterVector_get
    if _newclass:ParameterVector = _swig_property(_multi.Model_ParameterVector_get, _multi.Model_ParameterVector_set)
    __swig_setmethods__["ParameterValue"] = _multi.Model_ParameterValue_set
    __swig_getmethods__["ParameterValue"] = _multi.Model_ParameterValue_get
    if _newclass:ParameterValue = _swig_property(_multi.Model_ParameterValue_get, _multi.Model_ParameterValue_set)
    __swig_setmethods__["ExtParameterVector"] = _multi.Model_ExtParameterVector_set
    __swig_getmethods__["ExtParameterVector"] = _multi.Model_ExtParameterVector_get
    if _newclass:ExtParameterVector = _swig_property(_multi.Model_ExtParameterVector_get, _multi.Model_ExtParameterVector_set)
    __swig_setmethods__["ExtParameterValue"] = _multi.Model_ExtParameterValue_set
    __swig_getmethods__["ExtParameterValue"] = _multi.Model_ExtParameterValue_get
    if _newclass:ExtParameterValue = _swig_property(_multi.Model_ExtParameterValue_get, _multi.Model_ExtParameterValue_set)
    __swig_setmethods__["myLayerNumber"] = _multi.Model_myLayerNumber_set
    __swig_getmethods__["myLayerNumber"] = _multi.Model_myLayerNumber_get
    if _newclass:myLayerNumber = _swig_property(_multi.Model_myLayerNumber_get, _multi.Model_myLayerNumber_set)
    __swig_setmethods__["defaultCommand"] = _multi.Model_defaultCommand_set
    __swig_getmethods__["defaultCommand"] = _multi.Model_defaultCommand_get
    if _newclass:defaultCommand = _swig_property(_multi.Model_defaultCommand_get, _multi.Model_defaultCommand_set)
Model_swigregister = _multi.Model_swigregister
Model_swigregister(Model)
Model_changeExtension = _multi.Model_changeExtension

class MultiAnalysis(Model):
    __swig_setmethods__ = {}
    for _s in [Model]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, MultiAnalysis, name, value)
    __swig_getmethods__ = {}
    for _s in [Model]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, MultiAnalysis, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _multi.new_MultiAnalysis(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _multi.delete_MultiAnalysis
    __del__ = lambda self : None;
    def AddAnalysis(*args): return _multi.MultiAnalysis_AddAnalysis(*args)
    def AddValue(*args): return _multi.MultiAnalysis_AddValue(*args)
    def GetFunctionValue(*args): return _multi.MultiAnalysis_GetFunctionValue(*args)
    def Run(*args): return _multi.MultiAnalysis_Run(*args)
MultiAnalysis_swigregister = _multi.MultiAnalysis_swigregister
MultiAnalysis_swigregister(MultiAnalysis)

class Loadcase(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Loadcase, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Loadcase, name)
    __repr__ = _swig_repr
    __swig_setmethods__["Name"] = _multi.Loadcase_Name_set
    __swig_getmethods__["Name"] = _multi.Loadcase_Name_get
    if _newclass:Name = _swig_property(_multi.Loadcase_Name_get, _multi.Loadcase_Name_set)
    __swig_setmethods__["Scheme"] = _multi.Loadcase_Scheme_set
    __swig_getmethods__["Scheme"] = _multi.Loadcase_Scheme_get
    if _newclass:Scheme = _swig_property(_multi.Loadcase_Scheme_get, _multi.Loadcase_Scheme_set)
    __swig_setmethods__["ResultFile"] = _multi.Loadcase_ResultFile_set
    __swig_getmethods__["ResultFile"] = _multi.Loadcase_ResultFile_get
    if _newclass:ResultFile = _swig_property(_multi.Loadcase_ResultFile_get, _multi.Loadcase_ResultFile_set)
    __swig_setmethods__["Solver"] = _multi.Loadcase_Solver_set
    __swig_getmethods__["Solver"] = _multi.Loadcase_Solver_get
    if _newclass:Solver = _swig_property(_multi.Loadcase_Solver_get, _multi.Loadcase_Solver_set)
    __swig_setmethods__["OpenSign"] = _multi.Loadcase_OpenSign_set
    __swig_getmethods__["OpenSign"] = _multi.Loadcase_OpenSign_get
    if _newclass:OpenSign = _swig_property(_multi.Loadcase_OpenSign_get, _multi.Loadcase_OpenSign_set)
    __swig_setmethods__["CloseSign"] = _multi.Loadcase_CloseSign_set
    __swig_getmethods__["CloseSign"] = _multi.Loadcase_CloseSign_get
    if _newclass:CloseSign = _swig_property(_multi.Loadcase_CloseSign_get, _multi.Loadcase_CloseSign_set)
    def AddCritery(*args): return _multi.Loadcase_AddCritery(*args)
    def GetCriteria(*args): return _multi.Loadcase_GetCriteria(*args)
    def __init__(self, *args): 
        this = _multi.new_Loadcase(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _multi.delete_Loadcase
    __del__ = lambda self : None;
Loadcase_swigregister = _multi.Loadcase_swigregister
Loadcase_swigregister(Loadcase)

class Solver(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Solver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Solver, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_getmethods__["GetSolver"] = lambda x: _multi.Solver_GetSolver
    if _newclass:GetSolver = staticmethod(_multi.Solver_GetSolver)
    __swig_getmethods__["AddSolver"] = lambda x: _multi.Solver_AddSolver
    if _newclass:AddSolver = staticmethod(_multi.Solver_AddSolver)
    def Run(*args): return _multi.Solver_Run(*args)
    def GetValue(*args): return _multi.Solver_GetValue(*args)
    def SetLayer(*args): return _multi.Solver_SetLayer(*args)
    def GetLayersCount(*args): return _multi.Solver_GetLayersCount(*args)
    __swig_destroy__ = _multi.delete_Solver
    __del__ = lambda self : None;
Solver_swigregister = _multi.Solver_swigregister
Solver_swigregister(Solver)
Solver_GetSolver = _multi.Solver_GetSolver
Solver_AddSolver = _multi.Solver_AddSolver

class ModelLC(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ModelLC, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ModelLC, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _multi.new_ModelLC(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _multi.delete_ModelLC
    __del__ = lambda self : None;
    def SetScheme(*args): return _multi.ModelLC_SetScheme(*args)
    def GetScheme(*args): return _multi.ModelLC_GetScheme(*args)
    def AddParameter(*args): return _multi.ModelLC_AddParameter(*args)
    def SetParameterValue(*args): return _multi.ModelLC_SetParameterValue(*args)
    def GetParameterValue(*args): return _multi.ModelLC_GetParameterValue(*args)
    def AddExtParameter(*args): return _multi.ModelLC_AddExtParameter(*args)
    def SetExtParameterValue(*args): return _multi.ModelLC_SetExtParameterValue(*args)
    def GetExtParameterValue(*args): return _multi.ModelLC_GetExtParameterValue(*args)
    def GetFunctionValue(*args): return _multi.ModelLC_GetFunctionValue(*args)
    def f(*args): return _multi.ModelLC_f(*args)
    def fmint(*args): return _multi.ModelLC_fmint(*args)
    def fmaxt(*args): return _multi.ModelLC_fmaxt(*args)
    def GetFunctionLayer(*args): return _multi.ModelLC_GetFunctionLayer(*args)
    def Reset(*args): return _multi.ModelLC_Reset(*args)
    def AddLoadcase(*args): return _multi.ModelLC_AddLoadcase(*args)
    def GetLoadcase(*args): return _multi.ModelLC_GetLoadcase(*args)
    def Run(*args): return _multi.ModelLC_Run(*args)
    def SetLayer(*args): return _multi.ModelLC_SetLayer(*args)
    def GetLayersCount(*args): return _multi.ModelLC_GetLayersCount(*args)
    def SetHistoryFile(*args): return _multi.ModelLC_SetHistoryFile(*args)
    def GetHistoryFile(*args): return _multi.ModelLC_GetHistoryFile(*args)
    def SetFilePostfix(*args): return _multi.ModelLC_SetFilePostfix(*args)
    def SetDescription(*args): return _multi.ModelLC_SetDescription(*args)
    def replaceSymbol(*args): return _multi.ModelLC_replaceSymbol(*args)
    def addPostfix(*args): return _multi.ModelLC_addPostfix(*args)
    def writeHistory(*args): return _multi.ModelLC_writeHistory(*args)
    def initHistory(*args): return _multi.ModelLC_initHistory(*args)
    __swig_setmethods__["myScheme"] = _multi.ModelLC_myScheme_set
    __swig_getmethods__["myScheme"] = _multi.ModelLC_myScheme_get
    if _newclass:myScheme = _swig_property(_multi.ModelLC_myScheme_get, _multi.ModelLC_myScheme_set)
    __swig_setmethods__["myDescription"] = _multi.ModelLC_myDescription_set
    __swig_getmethods__["myDescription"] = _multi.ModelLC_myDescription_get
    if _newclass:myDescription = _swig_property(_multi.ModelLC_myDescription_get, _multi.ModelLC_myDescription_set)
    __swig_setmethods__["myHistory"] = _multi.ModelLC_myHistory_set
    __swig_getmethods__["myHistory"] = _multi.ModelLC_myHistory_get
    if _newclass:myHistory = _swig_property(_multi.ModelLC_myHistory_get, _multi.ModelLC_myHistory_set)
    __swig_setmethods__["myPostfix"] = _multi.ModelLC_myPostfix_set
    __swig_getmethods__["myPostfix"] = _multi.ModelLC_myPostfix_get
    if _newclass:myPostfix = _swig_property(_multi.ModelLC_myPostfix_get, _multi.ModelLC_myPostfix_set)
    __swig_setmethods__["ParameterVector"] = _multi.ModelLC_ParameterVector_set
    __swig_getmethods__["ParameterVector"] = _multi.ModelLC_ParameterVector_get
    if _newclass:ParameterVector = _swig_property(_multi.ModelLC_ParameterVector_get, _multi.ModelLC_ParameterVector_set)
    __swig_setmethods__["ParameterValue"] = _multi.ModelLC_ParameterValue_set
    __swig_getmethods__["ParameterValue"] = _multi.ModelLC_ParameterValue_get
    if _newclass:ParameterValue = _swig_property(_multi.ModelLC_ParameterValue_get, _multi.ModelLC_ParameterValue_set)
    __swig_setmethods__["ExtParameterVector"] = _multi.ModelLC_ExtParameterVector_set
    __swig_getmethods__["ExtParameterVector"] = _multi.ModelLC_ExtParameterVector_get
    if _newclass:ExtParameterVector = _swig_property(_multi.ModelLC_ExtParameterVector_get, _multi.ModelLC_ExtParameterVector_set)
    __swig_setmethods__["ExtParameterValue"] = _multi.ModelLC_ExtParameterValue_set
    __swig_getmethods__["ExtParameterValue"] = _multi.ModelLC_ExtParameterValue_get
    if _newclass:ExtParameterValue = _swig_property(_multi.ModelLC_ExtParameterValue_get, _multi.ModelLC_ExtParameterValue_set)
    __swig_setmethods__["myLayerNumber"] = _multi.ModelLC_myLayerNumber_set
    __swig_getmethods__["myLayerNumber"] = _multi.ModelLC_myLayerNumber_get
    if _newclass:myLayerNumber = _swig_property(_multi.ModelLC_myLayerNumber_get, _multi.ModelLC_myLayerNumber_set)
ModelLC_swigregister = _multi.ModelLC_swigregister
ModelLC_swigregister(ModelLC)

class FunctionStudy(ModelLC):
    __swig_setmethods__ = {}
    for _s in [ModelLC]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, FunctionStudy, name, value)
    __swig_getmethods__ = {}
    for _s in [ModelLC]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, FunctionStudy, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _multi.new_FunctionStudy(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _multi.delete_FunctionStudy
    __del__ = lambda self : None;
    def AddAnalysis(*args): return _multi.FunctionStudy_AddAnalysis(*args)
    def AddValue(*args): return _multi.FunctionStudy_AddValue(*args)
    def GetFunctionValue(*args): return _multi.FunctionStudy_GetFunctionValue(*args)
    def Run(*args): return _multi.FunctionStudy_Run(*args)
FunctionStudy_swigregister = _multi.FunctionStudy_swigregister
FunctionStudy_swigregister(FunctionStudy)

class Variable(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Variable, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Variable, name)
    __repr__ = _swig_repr
    __swig_setmethods__["Name"] = _multi.Variable_Name_set
    __swig_getmethods__["Name"] = _multi.Variable_Name_get
    if _newclass:Name = _swig_property(_multi.Variable_Name_get, _multi.Variable_Name_set)
    __swig_setmethods__["Value"] = _multi.Variable_Value_set
    __swig_getmethods__["Value"] = _multi.Variable_Value_get
    if _newclass:Value = _swig_property(_multi.Variable_Value_get, _multi.Variable_Value_set)
    __swig_setmethods__["Min"] = _multi.Variable_Min_set
    __swig_getmethods__["Min"] = _multi.Variable_Min_get
    if _newclass:Min = _swig_property(_multi.Variable_Min_get, _multi.Variable_Min_set)
    __swig_setmethods__["Max"] = _multi.Variable_Max_set
    __swig_getmethods__["Max"] = _multi.Variable_Max_get
    if _newclass:Max = _swig_property(_multi.Variable_Max_get, _multi.Variable_Max_set)
    __swig_setmethods__["Count"] = _multi.Variable_Count_set
    __swig_getmethods__["Count"] = _multi.Variable_Count_get
    if _newclass:Count = _swig_property(_multi.Variable_Count_get, _multi.Variable_Count_set)
    __swig_setmethods__["Type"] = _multi.Variable_Type_set
    __swig_getmethods__["Type"] = _multi.Variable_Type_get
    if _newclass:Type = _swig_property(_multi.Variable_Type_get, _multi.Variable_Type_set)
    def __init__(self, *args): 
        this = _multi.new_Variable(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _multi.delete_Variable
    __del__ = lambda self : None;
Variable_swigregister = _multi.Variable_swigregister
Variable_swigregister(Variable)

class FunctionScanner(FunctionStudy):
    __swig_setmethods__ = {}
    for _s in [FunctionStudy]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, FunctionScanner, name, value)
    __swig_getmethods__ = {}
    for _s in [FunctionStudy]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, FunctionScanner, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _multi.new_FunctionScanner(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _multi.delete_FunctionScanner
    __del__ = lambda self : None;
    def AddVariable(*args): return _multi.FunctionScanner_AddVariable(*args)
    def Run(*args): return _multi.FunctionScanner_Run(*args)
FunctionScanner_swigregister = _multi.FunctionScanner_swigregister
FunctionScanner_swigregister(FunctionScanner)

GetEnv = _multi.GetEnv
ExecCommand = _multi.ExecCommand


