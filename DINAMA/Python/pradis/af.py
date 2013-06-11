# This file was created automatically by SWIG 1.3.30.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _af
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


class PySwigIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PySwigIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PySwigIterator, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _af.delete_PySwigIterator
    __del__ = lambda self : None;
    def value(*args): return _af.PySwigIterator_value(*args)
    def incr(*args): return _af.PySwigIterator_incr(*args)
    def decr(*args): return _af.PySwigIterator_decr(*args)
    def distance(*args): return _af.PySwigIterator_distance(*args)
    def equal(*args): return _af.PySwigIterator_equal(*args)
    def copy(*args): return _af.PySwigIterator_copy(*args)
    def next(*args): return _af.PySwigIterator_next(*args)
    def previous(*args): return _af.PySwigIterator_previous(*args)
    def advance(*args): return _af.PySwigIterator_advance(*args)
    def __eq__(*args): return _af.PySwigIterator___eq__(*args)
    def __ne__(*args): return _af.PySwigIterator___ne__(*args)
    def __iadd__(*args): return _af.PySwigIterator___iadd__(*args)
    def __isub__(*args): return _af.PySwigIterator___isub__(*args)
    def __add__(*args): return _af.PySwigIterator___add__(*args)
    def __sub__(*args): return _af.PySwigIterator___sub__(*args)
    def __iter__(self): return self
PySwigIterator_swigregister = _af.PySwigIterator_swigregister
PySwigIterator_swigregister(PySwigIterator)

class TElement(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TElement, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TElement, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_TElement(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_TElement
    __del__ = lambda self : None;
    def SetRoot(*args): return _af.TElement_SetRoot(*args)
    def GetRoot(*args): return _af.TElement_GetRoot(*args)
    def DetachTree(*args): return _af.TElement_DetachTree(*args)
    def IsAttached(*args): return _af.TElement_IsAttached(*args)
    def Copy(*args): return _af.TElement_Copy(*args)
    def Init(*args): return _af.TElement_Init(*args)
    def UnSet(*args): return _af.TElement_UnSet(*args)
    def IsSet(*args): return _af.TElement_IsSet(*args)
    def SetName(*args): return _af.TElement_SetName(*args)
    def GetName(*args): return _af.TElement_GetName(*args)
    def SetVisible(*args): return _af.TElement_SetVisible(*args)
    def IsVisible(*args): return _af.TElement_IsVisible(*args)
    def GetType(*args): return _af.TElement_GetType(*args)
    def GetClass(*args): return _af.TElement_GetClass(*args)
    def AddElement(*args): return _af.TElement_AddElement(*args)
    def SetElement(*args): return _af.TElement_SetElement(*args)
    def RemoveElement(*args): return _af.TElement_RemoveElement(*args)
    def RemoveReference(*args): return _af.TElement_RemoveReference(*args)
    def ChangeReferenceForAll(*args): return _af.TElement_ChangeReferenceForAll(*args)
    def ReplaceReference(*args): return _af.TElement_ReplaceReference(*args)
    def RemoveElementByName(*args): return _af.TElement_RemoveElementByName(*args)
    def ClearElements(*args): return _af.TElement_ClearElements(*args)
    def GetVGUID(*args): return _af.TElement_GetVGUID(*args)
    def GetField(*args): return _af.TElement_GetField(*args)
TElement_swigregister = _af.TElement_swigregister
TElement_swigregister(TElement)

class Application(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Application, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Application, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_Application(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_Application
    __del__ = lambda self : None;
    def Open(*args): return _af.Application_Open(*args)
    def Save(*args): return _af.Application_Save(*args)
    def New(*args): return _af.Application_New(*args)
    def Close(*args): return _af.Application_Close(*args)
Application_swigregister = _af.Application_swigregister
Application_swigregister(Application)

class Document(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Document, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Document, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_Document(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_Document
    __del__ = lambda self : None;
    def GetRoot(*args): return _af.Document_GetRoot(*args)
    def Redo(*args): return _af.Document_Redo(*args)
    def Undo(*args): return _af.Document_Undo(*args)
    def OpenCommand(*args): return _af.Document_OpenCommand(*args)
    def CommitCommand(*args): return _af.Document_CommitCommand(*args)
    def AbortCommand(*args): return _af.Document_AbortCommand(*args)
    def GetAvailableRedos(*args): return _af.Document_GetAvailableRedos(*args)
    def GetAvailableUndos(*args): return _af.Document_GetAvailableUndos(*args)
    def SetDocument(*args): return _af.Document_SetDocument(*args)
    def GetDocument(*args): return _af.Document_GetDocument(*args)
    def GetCommitList(*args): return _af.Document_GetCommitList(*args)
Document_swigregister = _af.Document_swigregister
Document_swigregister(Document)

class DOF1(TElement):
    __swig_setmethods__ = {}
    for _s in [TElement]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, DOF1, name, value)
    __swig_getmethods__ = {}
    for _s in [TElement]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, DOF1, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_DOF1(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_DOF1
    __del__ = lambda self : None;
    def UnSet(*args): return _af.DOF1_UnSet(*args)
    def IsSet(*args): return _af.DOF1_IsSet(*args)
    def SetName(*args): return _af.DOF1_SetName(*args)
    def GetName(*args): return _af.DOF1_GetName(*args)
    def SetVisible(*args): return _af.DOF1_SetVisible(*args)
    def IsVisible(*args): return _af.DOF1_IsVisible(*args)
    def Init(*args): return _af.DOF1_Init(*args)
    def SetObjectName(*args): return _af.DOF1_SetObjectName(*args)
    def SetExternal(*args): return _af.DOF1_SetExternal(*args)
    def SetBase(*args): return _af.DOF1_SetBase(*args)
    def SetValue(*args): return _af.DOF1_SetValue(*args)
    def GetObjectName(*args): return _af.DOF1_GetObjectName(*args)
    def GetExternal(*args): return _af.DOF1_GetExternal(*args)
    def GetBase(*args): return _af.DOF1_GetBase(*args)
    def GetValue(*args): return _af.DOF1_GetValue(*args)
    def GetType(*args): return _af.DOF1_GetType(*args)
    def GetClass(*args): return _af.DOF1_GetClass(*args)
    __swig_setmethods__["Name"] = _af.DOF1_Name_set
    __swig_getmethods__["Name"] = _af.DOF1_Name_get
    if _newclass:Name = _swig_property(_af.DOF1_Name_get, _af.DOF1_Name_set)
    __swig_setmethods__["External"] = _af.DOF1_External_set
    __swig_getmethods__["External"] = _af.DOF1_External_get
    if _newclass:External = _swig_property(_af.DOF1_External_get, _af.DOF1_External_set)
    __swig_setmethods__["Base"] = _af.DOF1_Base_set
    __swig_getmethods__["Base"] = _af.DOF1_Base_get
    if _newclass:Base = _swig_property(_af.DOF1_Base_get, _af.DOF1_Base_set)
    __swig_setmethods__["Value"] = _af.DOF1_Value_set
    __swig_getmethods__["Value"] = _af.DOF1_Value_get
    if _newclass:Value = _swig_property(_af.DOF1_Value_get, _af.DOF1_Value_set)
DOF1_swigregister = _af.DOF1_swigregister
DOF1_swigregister(DOF1)

class Image(TElement):
    __swig_setmethods__ = {}
    for _s in [TElement]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, Image, name, value)
    __swig_getmethods__ = {}
    for _s in [TElement]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, Image, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_Image(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_Image
    __del__ = lambda self : None;
    def UnSet(*args): return _af.Image_UnSet(*args)
    def IsSet(*args): return _af.Image_IsSet(*args)
    def SetName(*args): return _af.Image_SetName(*args)
    def GetName(*args): return _af.Image_GetName(*args)
    def SetVisible(*args): return _af.Image_SetVisible(*args)
    def IsVisible(*args): return _af.Image_IsVisible(*args)
    def Init(*args): return _af.Image_Init(*args)
    def GetType(*args): return _af.Image_GetType(*args)
    def GetClass(*args): return _af.Image_GetClass(*args)
    def SetObjectName(*args): return _af.Image_SetObjectName(*args)
    def SetDescription(*args): return _af.Image_SetDescription(*args)
    def SetImageModel(*args): return _af.Image_SetImageModel(*args)
    def SetLayerParameters(*args): return _af.Image_SetLayerParameters(*args)
    def SetNodeList(*args): return _af.Image_SetNodeList(*args)
    def SetParameterList(*args): return _af.Image_SetParameterList(*args)
    def GetObjectName(*args): return _af.Image_GetObjectName(*args)
    def GetShortName(*args): return _af.Image_GetShortName(*args)
    def GetModuleName(*args): return _af.Image_GetModuleName(*args)
    def GetDescription(*args): return _af.Image_GetDescription(*args)
    def GetImageModel(*args): return _af.Image_GetImageModel(*args)
    def HasImageModel(*args): return _af.Image_HasImageModel(*args)
    def GetLayerParameters(*args): return _af.Image_GetLayerParameters(*args)
    def GetNodeList(*args): return _af.Image_GetNodeList(*args)
    def GetParameterList(*args): return _af.Image_GetParameterList(*args)
    __swig_setmethods__["Name"] = _af.Image_Name_set
    __swig_getmethods__["Name"] = _af.Image_Name_get
    if _newclass:Name = _swig_property(_af.Image_Name_get, _af.Image_Name_set)
    __swig_setmethods__["Description"] = _af.Image_Description_set
    __swig_getmethods__["Description"] = _af.Image_Description_get
    if _newclass:Description = _swig_property(_af.Image_Description_get, _af.Image_Description_set)
    __swig_setmethods__["ImageModel"] = _af.Image_ImageModel_set
    __swig_getmethods__["ImageModel"] = _af.Image_ImageModel_get
    if _newclass:ImageModel = _swig_property(_af.Image_ImageModel_get, _af.Image_ImageModel_set)
    __swig_setmethods__["LayerParameters"] = _af.Image_LayerParameters_set
    __swig_getmethods__["LayerParameters"] = _af.Image_LayerParameters_get
    if _newclass:LayerParameters = _swig_property(_af.Image_LayerParameters_get, _af.Image_LayerParameters_set)
    __swig_setmethods__["NodeList"] = _af.Image_NodeList_set
    __swig_getmethods__["NodeList"] = _af.Image_NodeList_get
    if _newclass:NodeList = _swig_property(_af.Image_NodeList_get, _af.Image_NodeList_set)
    __swig_setmethods__["ParameterList"] = _af.Image_ParameterList_set
    __swig_getmethods__["ParameterList"] = _af.Image_ParameterList_get
    if _newclass:ParameterList = _swig_property(_af.Image_ParameterList_get, _af.Image_ParameterList_set)
Image_swigregister = _af.Image_swigregister
Image_swigregister(Image)

class Layer(TElement):
    __swig_setmethods__ = {}
    for _s in [TElement]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, Layer, name, value)
    __swig_getmethods__ = {}
    for _s in [TElement]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, Layer, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_Layer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_Layer
    __del__ = lambda self : None;
    def UnSet(*args): return _af.Layer_UnSet(*args)
    def IsSet(*args): return _af.Layer_IsSet(*args)
    def SetName(*args): return _af.Layer_SetName(*args)
    def GetName(*args): return _af.Layer_GetName(*args)
    def SetVisible(*args): return _af.Layer_SetVisible(*args)
    def IsVisible(*args): return _af.Layer_IsVisible(*args)
    def Init(*args): return _af.Layer_Init(*args)
    def GetType(*args): return _af.Layer_GetType(*args)
    def GetClass(*args): return _af.Layer_GetClass(*args)
    def SetObjectName(*args): return _af.Layer_SetObjectName(*args)
    def SetColor(*args): return _af.Layer_SetColor(*args)
    def SetTransparency(*args): return _af.Layer_SetTransparency(*args)
    def SetMaterial(*args): return _af.Layer_SetMaterial(*args)
    def GetObjectName(*args): return _af.Layer_GetObjectName(*args)
    def GetColor(*args): return _af.Layer_GetColor(*args)
    def GetTransparency(*args): return _af.Layer_GetTransparency(*args)
    def GetMaterial(*args): return _af.Layer_GetMaterial(*args)
    __swig_setmethods__["Name"] = _af.Layer_Name_set
    __swig_getmethods__["Name"] = _af.Layer_Name_get
    if _newclass:Name = _swig_property(_af.Layer_Name_get, _af.Layer_Name_set)
    __swig_setmethods__["Color"] = _af.Layer_Color_set
    __swig_getmethods__["Color"] = _af.Layer_Color_get
    if _newclass:Color = _swig_property(_af.Layer_Color_get, _af.Layer_Color_set)
    __swig_setmethods__["Transparency"] = _af.Layer_Transparency_set
    __swig_getmethods__["Transparency"] = _af.Layer_Transparency_get
    if _newclass:Transparency = _swig_property(_af.Layer_Transparency_get, _af.Layer_Transparency_set)
    __swig_setmethods__["Material"] = _af.Layer_Material_set
    __swig_getmethods__["Material"] = _af.Layer_Material_get
    if _newclass:Material = _swig_property(_af.Layer_Material_get, _af.Layer_Material_set)
Layer_swigregister = _af.Layer_swigregister
Layer_swigregister(Layer)

class Model(TElement):
    __swig_setmethods__ = {}
    for _s in [TElement]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, Model, name, value)
    __swig_getmethods__ = {}
    for _s in [TElement]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, Model, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_Model(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_Model
    __del__ = lambda self : None;
    def UnSet(*args): return _af.Model_UnSet(*args)
    def IsSet(*args): return _af.Model_IsSet(*args)
    def SetName(*args): return _af.Model_SetName(*args)
    def GetName(*args): return _af.Model_GetName(*args)
    def SetVisible(*args): return _af.Model_SetVisible(*args)
    def IsVisible(*args): return _af.Model_IsVisible(*args)
    def Init(*args): return _af.Model_Init(*args)
    def GetType(*args): return _af.Model_GetType(*args)
    def GetClass(*args): return _af.Model_GetClass(*args)
    def SetObjectName(*args): return _af.Model_SetObjectName(*args)
    def SetDescription(*args): return _af.Model_SetDescription(*args)
    def SetNodeList(*args): return _af.Model_SetNodeList(*args)
    def SetParameterList(*args): return _af.Model_SetParameterList(*args)
    def GetObjectName(*args): return _af.Model_GetObjectName(*args)
    def GetShortName(*args): return _af.Model_GetShortName(*args)
    def GetModuleName(*args): return _af.Model_GetModuleName(*args)
    def GetDescription(*args): return _af.Model_GetDescription(*args)
    def GetNodeList(*args): return _af.Model_GetNodeList(*args)
    def GetParameterList(*args): return _af.Model_GetParameterList(*args)
    __swig_setmethods__["Name"] = _af.Model_Name_set
    __swig_getmethods__["Name"] = _af.Model_Name_get
    if _newclass:Name = _swig_property(_af.Model_Name_get, _af.Model_Name_set)
    __swig_setmethods__["Description"] = _af.Model_Description_set
    __swig_getmethods__["Description"] = _af.Model_Description_get
    if _newclass:Description = _swig_property(_af.Model_Description_get, _af.Model_Description_set)
    __swig_setmethods__["NodeList"] = _af.Model_NodeList_set
    __swig_getmethods__["NodeList"] = _af.Model_NodeList_get
    if _newclass:NodeList = _swig_property(_af.Model_NodeList_get, _af.Model_NodeList_set)
    __swig_setmethods__["ParameterList"] = _af.Model_ParameterList_set
    __swig_getmethods__["ParameterList"] = _af.Model_ParameterList_get
    if _newclass:ParameterList = _swig_property(_af.Model_ParameterList_get, _af.Model_ParameterList_set)
Model_swigregister = _af.Model_swigregister
Model_swigregister(Model)

class Node(TElement):
    __swig_setmethods__ = {}
    for _s in [TElement]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, Node, name, value)
    __swig_getmethods__ = {}
    for _s in [TElement]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, Node, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_Node(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_Node
    __del__ = lambda self : None;
    def UnSet(*args): return _af.Node_UnSet(*args)
    def IsSet(*args): return _af.Node_IsSet(*args)
    def SetName(*args): return _af.Node_SetName(*args)
    def GetName(*args): return _af.Node_GetName(*args)
    def SetVisible(*args): return _af.Node_SetVisible(*args)
    def IsVisible(*args): return _af.Node_IsVisible(*args)
    def Init(*args): return _af.Node_Init(*args)
    def GetType(*args): return _af.Node_GetType(*args)
    def GetClass(*args): return _af.Node_GetClass(*args)
    def SetObjectName(*args): return _af.Node_SetObjectName(*args)
    def SetDescription(*args): return _af.Node_SetDescription(*args)
    def SetExternal(*args): return _af.Node_SetExternal(*args)
    def SetBase(*args): return _af.Node_SetBase(*args)
    def SetDOFList(*args): return _af.Node_SetDOFList(*args)
    def GetObjectName(*args): return _af.Node_GetObjectName(*args)
    def GetShortName(*args): return _af.Node_GetShortName(*args)
    def GetModuleName(*args): return _af.Node_GetModuleName(*args)
    def GetDescription(*args): return _af.Node_GetDescription(*args)
    def GetExternal(*args): return _af.Node_GetExternal(*args)
    def GetBase(*args): return _af.Node_GetBase(*args)
    def GetDOFList(*args): return _af.Node_GetDOFList(*args)
    __swig_setmethods__["Name"] = _af.Node_Name_set
    __swig_getmethods__["Name"] = _af.Node_Name_get
    if _newclass:Name = _swig_property(_af.Node_Name_get, _af.Node_Name_set)
    __swig_setmethods__["Description"] = _af.Node_Description_set
    __swig_getmethods__["Description"] = _af.Node_Description_get
    if _newclass:Description = _swig_property(_af.Node_Description_get, _af.Node_Description_set)
    __swig_setmethods__["External"] = _af.Node_External_set
    __swig_getmethods__["External"] = _af.Node_External_get
    if _newclass:External = _swig_property(_af.Node_External_get, _af.Node_External_set)
    __swig_setmethods__["Base"] = _af.Node_Base_set
    __swig_getmethods__["Base"] = _af.Node_Base_get
    if _newclass:Base = _swig_property(_af.Node_Base_get, _af.Node_Base_set)
    __swig_setmethods__["DOFList"] = _af.Node_DOFList_set
    __swig_getmethods__["DOFList"] = _af.Node_DOFList_get
    if _newclass:DOFList = _swig_property(_af.Node_DOFList_get, _af.Node_DOFList_set)
Node_swigregister = _af.Node_swigregister
Node_swigregister(Node)

class OutValue(TElement):
    __swig_setmethods__ = {}
    for _s in [TElement]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OutValue, name, value)
    __swig_getmethods__ = {}
    for _s in [TElement]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OutValue, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_OutValue(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_OutValue
    __del__ = lambda self : None;
    def UnSet(*args): return _af.OutValue_UnSet(*args)
    def IsSet(*args): return _af.OutValue_IsSet(*args)
    def SetName(*args): return _af.OutValue_SetName(*args)
    def GetName(*args): return _af.OutValue_GetName(*args)
    def SetVisible(*args): return _af.OutValue_SetVisible(*args)
    def IsVisible(*args): return _af.OutValue_IsVisible(*args)
    def Init(*args): return _af.OutValue_Init(*args)
    def GetType(*args): return _af.OutValue_GetType(*args)
    def GetClass(*args): return _af.OutValue_GetClass(*args)
    def SetObjectName(*args): return _af.OutValue_SetObjectName(*args)
    def SetDescription(*args): return _af.OutValue_SetDescription(*args)
    def SetOutValueType(*args): return _af.OutValue_SetOutValueType(*args)
    def SetNodeOfValue(*args): return _af.OutValue_SetNodeOfValue(*args)
    def SetModelOfValue(*args): return _af.OutValue_SetModelOfValue(*args)
    def SetNumber(*args): return _af.OutValue_SetNumber(*args)
    def GetObjectName(*args): return _af.OutValue_GetObjectName(*args)
    def GetDescription(*args): return _af.OutValue_GetDescription(*args)
    def GetOutValueType(*args): return _af.OutValue_GetOutValueType(*args)
    def GetNodeOfValue(*args): return _af.OutValue_GetNodeOfValue(*args)
    def GetModelOfValue(*args): return _af.OutValue_GetModelOfValue(*args)
    def GetNumber(*args): return _af.OutValue_GetNumber(*args)
    __swig_setmethods__["Name"] = _af.OutValue_Name_set
    __swig_getmethods__["Name"] = _af.OutValue_Name_get
    if _newclass:Name = _swig_property(_af.OutValue_Name_get, _af.OutValue_Name_set)
    __swig_setmethods__["Description"] = _af.OutValue_Description_set
    __swig_getmethods__["Description"] = _af.OutValue_Description_get
    if _newclass:Description = _swig_property(_af.OutValue_Description_get, _af.OutValue_Description_set)
    __swig_setmethods__["Type"] = _af.OutValue_Type_set
    __swig_getmethods__["Type"] = _af.OutValue_Type_get
    if _newclass:Type = _swig_property(_af.OutValue_Type_get, _af.OutValue_Type_set)
    __swig_setmethods__["NodeOfValue"] = _af.OutValue_NodeOfValue_set
    __swig_getmethods__["NodeOfValue"] = _af.OutValue_NodeOfValue_get
    if _newclass:NodeOfValue = _swig_property(_af.OutValue_NodeOfValue_get, _af.OutValue_NodeOfValue_set)
    __swig_setmethods__["ModelOfValue"] = _af.OutValue_ModelOfValue_set
    __swig_getmethods__["ModelOfValue"] = _af.OutValue_ModelOfValue_get
    if _newclass:ModelOfValue = _swig_property(_af.OutValue_ModelOfValue_get, _af.OutValue_ModelOfValue_set)
    __swig_setmethods__["Number"] = _af.OutValue_Number_set
    __swig_getmethods__["Number"] = _af.OutValue_Number_get
    if _newclass:Number = _swig_property(_af.OutValue_Number_get, _af.OutValue_Number_set)
OutValue_swigregister = _af.OutValue_swigregister
OutValue_swigregister(OutValue)

class OutVariable(TElement):
    __swig_setmethods__ = {}
    for _s in [TElement]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OutVariable, name, value)
    __swig_getmethods__ = {}
    for _s in [TElement]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OutVariable, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_OutVariable(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_OutVariable
    __del__ = lambda self : None;
    def UnSet(*args): return _af.OutVariable_UnSet(*args)
    def IsSet(*args): return _af.OutVariable_IsSet(*args)
    def SetName(*args): return _af.OutVariable_SetName(*args)
    def GetName(*args): return _af.OutVariable_GetName(*args)
    def SetVisible(*args): return _af.OutVariable_SetVisible(*args)
    def IsVisible(*args): return _af.OutVariable_IsVisible(*args)
    def Init(*args): return _af.OutVariable_Init(*args)
    def GetType(*args): return _af.OutVariable_GetType(*args)
    def GetClass(*args): return _af.OutVariable_GetClass(*args)
    def SetObjectName(*args): return _af.OutVariable_SetObjectName(*args)
    def SetDescription(*args): return _af.OutVariable_SetDescription(*args)
    def SetOutValueList(*args): return _af.OutVariable_SetOutValueList(*args)
    def SetParameterList(*args): return _af.OutVariable_SetParameterList(*args)
    def GetObjectName(*args): return _af.OutVariable_GetObjectName(*args)
    def GetShortName(*args): return _af.OutVariable_GetShortName(*args)
    def GetModuleName(*args): return _af.OutVariable_GetModuleName(*args)
    def GetDescription(*args): return _af.OutVariable_GetDescription(*args)
    def GetOutValueList(*args): return _af.OutVariable_GetOutValueList(*args)
    def GetParameterList(*args): return _af.OutVariable_GetParameterList(*args)
    __swig_setmethods__["Name"] = _af.OutVariable_Name_set
    __swig_getmethods__["Name"] = _af.OutVariable_Name_get
    if _newclass:Name = _swig_property(_af.OutVariable_Name_get, _af.OutVariable_Name_set)
    __swig_setmethods__["Description"] = _af.OutVariable_Description_set
    __swig_getmethods__["Description"] = _af.OutVariable_Description_get
    if _newclass:Description = _swig_property(_af.OutVariable_Description_get, _af.OutVariable_Description_set)
    __swig_setmethods__["OutValueList"] = _af.OutVariable_OutValueList_set
    __swig_getmethods__["OutValueList"] = _af.OutVariable_OutValueList_get
    if _newclass:OutValueList = _swig_property(_af.OutVariable_OutValueList_get, _af.OutVariable_OutValueList_set)
    __swig_setmethods__["ParameterList"] = _af.OutVariable_ParameterList_set
    __swig_getmethods__["ParameterList"] = _af.OutVariable_ParameterList_get
    if _newclass:ParameterList = _swig_property(_af.OutVariable_ParameterList_get, _af.OutVariable_ParameterList_set)
OutVariable_swigregister = _af.OutVariable_swigregister
OutVariable_swigregister(OutVariable)

class Print(TElement):
    __swig_setmethods__ = {}
    for _s in [TElement]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, Print, name, value)
    __swig_getmethods__ = {}
    for _s in [TElement]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, Print, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_Print(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_Print
    __del__ = lambda self : None;
    def UnSet(*args): return _af.Print_UnSet(*args)
    def IsSet(*args): return _af.Print_IsSet(*args)
    def SetName(*args): return _af.Print_SetName(*args)
    def GetName(*args): return _af.Print_GetName(*args)
    def SetVisible(*args): return _af.Print_SetVisible(*args)
    def IsVisible(*args): return _af.Print_IsVisible(*args)
    def Init(*args): return _af.Print_Init(*args)
    def GetType(*args): return _af.Print_GetType(*args)
    def GetClass(*args): return _af.Print_GetClass(*args)
    def SetObjectName(*args): return _af.Print_SetObjectName(*args)
    def SetDescription(*args): return _af.Print_SetDescription(*args)
    def SetRangeList(*args): return _af.Print_SetRangeList(*args)
    def SetParameterList(*args): return _af.Print_SetParameterList(*args)
    def GetObjectName(*args): return _af.Print_GetObjectName(*args)
    def GetDescription(*args): return _af.Print_GetDescription(*args)
    def GetRangeList(*args): return _af.Print_GetRangeList(*args)
    def GetParameterList(*args): return _af.Print_GetParameterList(*args)
    __swig_setmethods__["Name"] = _af.Print_Name_set
    __swig_getmethods__["Name"] = _af.Print_Name_get
    if _newclass:Name = _swig_property(_af.Print_Name_get, _af.Print_Name_set)
    __swig_setmethods__["Description"] = _af.Print_Description_set
    __swig_getmethods__["Description"] = _af.Print_Description_get
    if _newclass:Description = _swig_property(_af.Print_Description_get, _af.Print_Description_set)
    __swig_setmethods__["RangeList"] = _af.Print_RangeList_set
    __swig_getmethods__["RangeList"] = _af.Print_RangeList_get
    if _newclass:RangeList = _swig_property(_af.Print_RangeList_get, _af.Print_RangeList_set)
    __swig_setmethods__["ParameterList"] = _af.Print_ParameterList_set
    __swig_getmethods__["ParameterList"] = _af.Print_ParameterList_get
    if _newclass:ParameterList = _swig_property(_af.Print_ParameterList_get, _af.Print_ParameterList_set)
Print_swigregister = _af.Print_swigregister
Print_swigregister(Print)

class PSLGenerator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PSLGenerator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PSLGenerator, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_PSLGenerator(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_PSLGenerator
    __del__ = lambda self : None;
    def GetGeneratedFile(*args): return _af.PSLGenerator_GetGeneratedFile(*args)
    def SaveToFile(*args): return _af.PSLGenerator_SaveToFile(*args)
PSLGenerator_swigregister = _af.PSLGenerator_swigregister
PSLGenerator_swigregister(PSLGenerator)

class Range(TElement):
    __swig_setmethods__ = {}
    for _s in [TElement]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, Range, name, value)
    __swig_getmethods__ = {}
    for _s in [TElement]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, Range, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_Range(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_Range
    __del__ = lambda self : None;
    def UnSet(*args): return _af.Range_UnSet(*args)
    def IsSet(*args): return _af.Range_IsSet(*args)
    def SetName(*args): return _af.Range_SetName(*args)
    def GetName(*args): return _af.Range_GetName(*args)
    def SetVisible(*args): return _af.Range_SetVisible(*args)
    def IsVisible(*args): return _af.Range_IsVisible(*args)
    def Init(*args): return _af.Range_Init(*args)
    def GetType(*args): return _af.Range_GetType(*args)
    def GetClass(*args): return _af.Range_GetClass(*args)
    def SetObjectName(*args): return _af.Range_SetObjectName(*args)
    def SetMin(*args): return _af.Range_SetMin(*args)
    def SetMax(*args): return _af.Range_SetMax(*args)
    def SetOutVariable(*args): return _af.Range_SetOutVariable(*args)
    def GetObjectName(*args): return _af.Range_GetObjectName(*args)
    def GetMin(*args): return _af.Range_GetMin(*args)
    def GetMax(*args): return _af.Range_GetMax(*args)
    def GetOutVariable(*args): return _af.Range_GetOutVariable(*args)
    __swig_setmethods__["Name"] = _af.Range_Name_set
    __swig_getmethods__["Name"] = _af.Range_Name_get
    if _newclass:Name = _swig_property(_af.Range_Name_get, _af.Range_Name_set)
    __swig_setmethods__["Min"] = _af.Range_Min_set
    __swig_getmethods__["Min"] = _af.Range_Min_get
    if _newclass:Min = _swig_property(_af.Range_Min_get, _af.Range_Min_set)
    __swig_setmethods__["Max"] = _af.Range_Max_set
    __swig_getmethods__["Max"] = _af.Range_Max_get
    if _newclass:Max = _swig_property(_af.Range_Max_get, _af.Range_Max_set)
    __swig_setmethods__["myOutVariable"] = _af.Range_myOutVariable_set
    __swig_getmethods__["myOutVariable"] = _af.Range_myOutVariable_get
    if _newclass:myOutVariable = _swig_property(_af.Range_myOutVariable_get, _af.Range_myOutVariable_set)
Range_swigregister = _af.Range_swigregister
Range_swigregister(Range)

class Scheme(TElement):
    __swig_setmethods__ = {}
    for _s in [TElement]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, Scheme, name, value)
    __swig_getmethods__ = {}
    for _s in [TElement]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, Scheme, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_Scheme(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_Scheme
    __del__ = lambda self : None;
    def UnSet(*args): return _af.Scheme_UnSet(*args)
    def IsSet(*args): return _af.Scheme_IsSet(*args)
    def SetName(*args): return _af.Scheme_SetName(*args)
    def GetName(*args): return _af.Scheme_GetName(*args)
    def SetVisible(*args): return _af.Scheme_SetVisible(*args)
    def IsVisible(*args): return _af.Scheme_IsVisible(*args)
    def Init(*args): return _af.Scheme_Init(*args)
    def GetType(*args): return _af.Scheme_GetType(*args)
    def GetClass(*args): return _af.Scheme_GetClass(*args)
    def SetObjectName(*args): return _af.Scheme_SetObjectName(*args)
    def SetDescription(*args): return _af.Scheme_SetDescription(*args)
    def SetDataList(*args): return _af.Scheme_SetDataList(*args)
    def SetModelList(*args): return _af.Scheme_SetModelList(*args)
    def SetOutVariableList(*args): return _af.Scheme_SetOutVariableList(*args)
    def SetImageList(*args): return _af.Scheme_SetImageList(*args)
    def SetRunList(*args): return _af.Scheme_SetRunList(*args)
    def SetPrintList(*args): return _af.Scheme_SetPrintList(*args)
    def SetNodeList(*args): return _af.Scheme_SetNodeList(*args)
    def SetParameterList(*args): return _af.Scheme_SetParameterList(*args)
    def SetIncludeList(*args): return _af.Scheme_SetIncludeList(*args)
    def SetFragmentList(*args): return _af.Scheme_SetFragmentList(*args)
    def AddFragment(*args): return _af.Scheme_AddFragment(*args)
    def GetObjectName(*args): return _af.Scheme_GetObjectName(*args)
    def GetDescription(*args): return _af.Scheme_GetDescription(*args)
    def GetDataList(*args): return _af.Scheme_GetDataList(*args)
    def GetModelList(*args): return _af.Scheme_GetModelList(*args)
    def GetOutVariableList(*args): return _af.Scheme_GetOutVariableList(*args)
    def GetImageList(*args): return _af.Scheme_GetImageList(*args)
    def GetRunList(*args): return _af.Scheme_GetRunList(*args)
    def GetPrintList(*args): return _af.Scheme_GetPrintList(*args)
    def GetNodeList(*args): return _af.Scheme_GetNodeList(*args)
    def GetFragmentList(*args): return _af.Scheme_GetFragmentList(*args)
    def GetParameterList(*args): return _af.Scheme_GetParameterList(*args)
    def GetIncludeList(*args): return _af.Scheme_GetIncludeList(*args)
    def SetEqvList(*args): return _af.Scheme_SetEqvList(*args)
    def GetEqvList(*args): return _af.Scheme_GetEqvList(*args)
    def AddEquivalence(*args): return _af.Scheme_AddEquivalence(*args)
    def FindDOF(*args): return _af.Scheme_FindDOF(*args)
    __swig_setmethods__["Name"] = _af.Scheme_Name_set
    __swig_getmethods__["Name"] = _af.Scheme_Name_get
    if _newclass:Name = _swig_property(_af.Scheme_Name_get, _af.Scheme_Name_set)
    __swig_setmethods__["Description"] = _af.Scheme_Description_set
    __swig_getmethods__["Description"] = _af.Scheme_Description_get
    if _newclass:Description = _swig_property(_af.Scheme_Description_get, _af.Scheme_Description_set)
    __swig_setmethods__["DataList"] = _af.Scheme_DataList_set
    __swig_getmethods__["DataList"] = _af.Scheme_DataList_get
    if _newclass:DataList = _swig_property(_af.Scheme_DataList_get, _af.Scheme_DataList_set)
    __swig_setmethods__["ModelList"] = _af.Scheme_ModelList_set
    __swig_getmethods__["ModelList"] = _af.Scheme_ModelList_get
    if _newclass:ModelList = _swig_property(_af.Scheme_ModelList_get, _af.Scheme_ModelList_set)
    __swig_setmethods__["OutVariableList"] = _af.Scheme_OutVariableList_set
    __swig_getmethods__["OutVariableList"] = _af.Scheme_OutVariableList_get
    if _newclass:OutVariableList = _swig_property(_af.Scheme_OutVariableList_get, _af.Scheme_OutVariableList_set)
    __swig_setmethods__["ImageList"] = _af.Scheme_ImageList_set
    __swig_getmethods__["ImageList"] = _af.Scheme_ImageList_get
    if _newclass:ImageList = _swig_property(_af.Scheme_ImageList_get, _af.Scheme_ImageList_set)
    __swig_setmethods__["RunList"] = _af.Scheme_RunList_set
    __swig_getmethods__["RunList"] = _af.Scheme_RunList_get
    if _newclass:RunList = _swig_property(_af.Scheme_RunList_get, _af.Scheme_RunList_set)
    __swig_setmethods__["PrintList"] = _af.Scheme_PrintList_set
    __swig_getmethods__["PrintList"] = _af.Scheme_PrintList_get
    if _newclass:PrintList = _swig_property(_af.Scheme_PrintList_get, _af.Scheme_PrintList_set)
    __swig_setmethods__["NodeList"] = _af.Scheme_NodeList_set
    __swig_getmethods__["NodeList"] = _af.Scheme_NodeList_get
    if _newclass:NodeList = _swig_property(_af.Scheme_NodeList_get, _af.Scheme_NodeList_set)
    __swig_setmethods__["FragmentList"] = _af.Scheme_FragmentList_set
    __swig_getmethods__["FragmentList"] = _af.Scheme_FragmentList_get
    if _newclass:FragmentList = _swig_property(_af.Scheme_FragmentList_get, _af.Scheme_FragmentList_set)
    __swig_setmethods__["ParameterList"] = _af.Scheme_ParameterList_set
    __swig_getmethods__["ParameterList"] = _af.Scheme_ParameterList_get
    if _newclass:ParameterList = _swig_property(_af.Scheme_ParameterList_get, _af.Scheme_ParameterList_set)
    __swig_setmethods__["IncludeList"] = _af.Scheme_IncludeList_set
    __swig_getmethods__["IncludeList"] = _af.Scheme_IncludeList_get
    if _newclass:IncludeList = _swig_property(_af.Scheme_IncludeList_get, _af.Scheme_IncludeList_set)
    __swig_setmethods__["EqvList"] = _af.Scheme_EqvList_set
    __swig_getmethods__["EqvList"] = _af.Scheme_EqvList_get
    if _newclass:EqvList = _swig_property(_af.Scheme_EqvList_get, _af.Scheme_EqvList_set)
Scheme_swigregister = _af.Scheme_swigregister
Scheme_swigregister(Scheme)

class Include(TElement):
    __swig_setmethods__ = {}
    for _s in [TElement]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, Include, name, value)
    __swig_getmethods__ = {}
    for _s in [TElement]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, Include, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_Include(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_Include
    __del__ = lambda self : None;
    def UnSet(*args): return _af.Include_UnSet(*args)
    def IsSet(*args): return _af.Include_IsSet(*args)
    def SetName(*args): return _af.Include_SetName(*args)
    def GetName(*args): return _af.Include_GetName(*args)
    def SetVisible(*args): return _af.Include_SetVisible(*args)
    def IsVisible(*args): return _af.Include_IsVisible(*args)
    def Init(*args): return _af.Include_Init(*args)
    def GetType(*args): return _af.Include_GetType(*args)
    def GetClass(*args): return _af.Include_GetClass(*args)
    def SetObjectName(*args): return _af.Include_SetObjectName(*args)
    def SetDescription(*args): return _af.Include_SetDescription(*args)
    def SetIncludeType(*args): return _af.Include_SetIncludeType(*args)
    def SetFile(*args): return _af.Include_SetFile(*args)
    def GetObjectName(*args): return _af.Include_GetObjectName(*args)
    def GetDescription(*args): return _af.Include_GetDescription(*args)
    def GetIncludeType(*args): return _af.Include_GetIncludeType(*args)
    def GetFile(*args): return _af.Include_GetFile(*args)
    __swig_setmethods__["Name"] = _af.Include_Name_set
    __swig_getmethods__["Name"] = _af.Include_Name_get
    if _newclass:Name = _swig_property(_af.Include_Name_get, _af.Include_Name_set)
    __swig_setmethods__["Description"] = _af.Include_Description_set
    __swig_getmethods__["Description"] = _af.Include_Description_get
    if _newclass:Description = _swig_property(_af.Include_Description_get, _af.Include_Description_set)
    __swig_setmethods__["Type"] = _af.Include_Type_set
    __swig_getmethods__["Type"] = _af.Include_Type_get
    if _newclass:Type = _swig_property(_af.Include_Type_get, _af.Include_Type_set)
    __swig_setmethods__["FileName"] = _af.Include_FileName_set
    __swig_getmethods__["FileName"] = _af.Include_FileName_get
    if _newclass:FileName = _swig_property(_af.Include_FileName_get, _af.Include_FileName_set)
Include_swigregister = _af.Include_swigregister
Include_swigregister(Include)

class Solver(TElement):
    __swig_setmethods__ = {}
    for _s in [TElement]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, Solver, name, value)
    __swig_getmethods__ = {}
    for _s in [TElement]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, Solver, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_Solver(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_Solver
    __del__ = lambda self : None;
    def UnSet(*args): return _af.Solver_UnSet(*args)
    def IsSet(*args): return _af.Solver_IsSet(*args)
    def SetName(*args): return _af.Solver_SetName(*args)
    def GetName(*args): return _af.Solver_GetName(*args)
    def SetVisible(*args): return _af.Solver_SetVisible(*args)
    def IsVisible(*args): return _af.Solver_IsVisible(*args)
    def Init(*args): return _af.Solver_Init(*args)
    def GetType(*args): return _af.Solver_GetType(*args)
    def GetClass(*args): return _af.Solver_GetClass(*args)
    def SetObjectName(*args): return _af.Solver_SetObjectName(*args)
    def SetDescription(*args): return _af.Solver_SetDescription(*args)
    def SetParameterList(*args): return _af.Solver_SetParameterList(*args)
    def SetRangeList(*args): return _af.Solver_SetRangeList(*args)
    def GetObjectName(*args): return _af.Solver_GetObjectName(*args)
    def GetDescription(*args): return _af.Solver_GetDescription(*args)
    def GetParameterList(*args): return _af.Solver_GetParameterList(*args)
    def GetRangeList(*args): return _af.Solver_GetRangeList(*args)
    __swig_setmethods__["Name"] = _af.Solver_Name_set
    __swig_getmethods__["Name"] = _af.Solver_Name_get
    if _newclass:Name = _swig_property(_af.Solver_Name_get, _af.Solver_Name_set)
    __swig_setmethods__["Description"] = _af.Solver_Description_set
    __swig_getmethods__["Description"] = _af.Solver_Description_get
    if _newclass:Description = _swig_property(_af.Solver_Description_get, _af.Solver_Description_set)
    __swig_setmethods__["RangeList"] = _af.Solver_RangeList_set
    __swig_getmethods__["RangeList"] = _af.Solver_RangeList_get
    if _newclass:RangeList = _swig_property(_af.Solver_RangeList_get, _af.Solver_RangeList_set)
    __swig_setmethods__["ParameterList"] = _af.Solver_ParameterList_set
    __swig_getmethods__["ParameterList"] = _af.Solver_ParameterList_get
    if _newclass:ParameterList = _swig_property(_af.Solver_ParameterList_get, _af.Solver_ParameterList_set)
Solver_swigregister = _af.Solver_swigregister
Solver_swigregister(Solver)

class TList(TElement):
    __swig_setmethods__ = {}
    for _s in [TElement]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TList, name, value)
    __swig_getmethods__ = {}
    for _s in [TElement]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TList, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_TList(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_TList
    __del__ = lambda self : None;
    def GetType(*args): return _af.TList_GetType(*args)
    def GetClass(*args): return _af.TList_GetClass(*args)
    def UnSet(*args): return _af.TList_UnSet(*args)
    def IsSet(*args): return _af.TList_IsSet(*args)
    def SetName(*args): return _af.TList_SetName(*args)
    def GetName(*args): return _af.TList_GetName(*args)
    def SetVisible(*args): return _af.TList_SetVisible(*args)
    def IsVisible(*args): return _af.TList_IsVisible(*args)
    def GetIterator(*args): return _af.TList_GetIterator(*args)
    def GetSize(*args): return _af.TList_GetSize(*args)
    def GetAt(*args): return _af.TList_GetAt(*args)
    def Add(*args): return _af.TList_Add(*args)
    def RemoveVar(*args): return _af.TList_RemoveVar(*args)
    def GetList(*args): return _af.TList_GetList(*args)
TList_swigregister = _af.TList_swigregister
TList_swigregister(TList)

class TReal(TElement):
    __swig_setmethods__ = {}
    for _s in [TElement]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TReal, name, value)
    __swig_getmethods__ = {}
    for _s in [TElement]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TReal, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_TReal(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_TReal
    __del__ = lambda self : None;
    def GetType(*args): return _af.TReal_GetType(*args)
    def GetClass(*args): return _af.TReal_GetClass(*args)
    def UnSet(*args): return _af.TReal_UnSet(*args)
    def IsSet(*args): return _af.TReal_IsSet(*args)
    def SetName(*args): return _af.TReal_SetName(*args)
    def GetName(*args): return _af.TReal_GetName(*args)
    def SetVisible(*args): return _af.TReal_SetVisible(*args)
    def IsVisible(*args): return _af.TReal_IsVisible(*args)
    def SetValue(*args): return _af.TReal_SetValue(*args)
    def GetValue(*args): return _af.TReal_GetValue(*args)
TReal_swigregister = _af.TReal_swigregister
TReal_swigregister(TReal)

class TData(TElement):
    __swig_setmethods__ = {}
    for _s in [TElement]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TData, name, value)
    __swig_getmethods__ = {}
    for _s in [TElement]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TData, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_TData(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_TData
    __del__ = lambda self : None;
    def UnSet(*args): return _af.TData_UnSet(*args)
    def UnSetValue(*args): return _af.TData_UnSetValue(*args)
    def IsSet(*args): return _af.TData_IsSet(*args)
    def SetName(*args): return _af.TData_SetName(*args)
    def GetName(*args): return _af.TData_GetName(*args)
    def SetObjectName(*args): return _af.TData_SetObjectName(*args)
    def SetDescription(*args): return _af.TData_SetDescription(*args)
    def GetObjectName(*args): return _af.TData_GetObjectName(*args)
    def GetDescription(*args): return _af.TData_GetDescription(*args)
    def SetVisible(*args): return _af.TData_SetVisible(*args)
    def IsVisible(*args): return _af.TData_IsVisible(*args)
    def GetType(*args): return _af.TData_GetType(*args)
    def GetClass(*args): return _af.TData_GetClass(*args)
    def SetValue(*args): return _af.TData_SetValue(*args)
    def GetValue(*args): return _af.TData_GetValue(*args)
    def ToString(*args): return _af.TData_ToString(*args)
    def FromString(*args): return _af.TData_FromString(*args)
    def GetParameterType(*args): return _af.TData_GetParameterType(*args)
TData_swigregister = _af.TData_swigregister
TData_swigregister(TData)

class TString(TElement):
    __swig_setmethods__ = {}
    for _s in [TElement]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TString, name, value)
    __swig_getmethods__ = {}
    for _s in [TElement]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TString, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_TString(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_TString
    __del__ = lambda self : None;
    def GetType(*args): return _af.TString_GetType(*args)
    def GetClass(*args): return _af.TString_GetClass(*args)
    def UnSet(*args): return _af.TString_UnSet(*args)
    def IsSet(*args): return _af.TString_IsSet(*args)
    def SetName(*args): return _af.TString_SetName(*args)
    def GetName(*args): return _af.TString_GetName(*args)
    def SetVisible(*args): return _af.TString_SetVisible(*args)
    def IsVisible(*args): return _af.TString_IsVisible(*args)
    def SetValue(*args): return _af.TString_SetValue(*args)
    def GetValue(*args): return _af.TString_GetValue(*args)
TString_swigregister = _af.TString_swigregister
TString_swigregister(TString)

class StringParameter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringParameter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringParameter, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _af.delete_StringParameter
    __del__ = lambda self : None;
    __swig_getmethods__["Add"] = lambda x: _af.StringParameter_Add
    if _newclass:Add = staticmethod(_af.StringParameter_Add)
    __swig_getmethods__["Get"] = lambda x: _af.StringParameter_Get
    if _newclass:Get = staticmethod(_af.StringParameter_Get)
    __swig_getmethods__["SetName"] = lambda x: _af.StringParameter_SetName
    if _newclass:SetName = staticmethod(_af.StringParameter_SetName)
    __swig_getmethods__["Close"] = lambda x: _af.StringParameter_Close
    if _newclass:Close = staticmethod(_af.StringParameter_Close)
    __swig_getmethods__["Save"] = lambda x: _af.StringParameter_Save
    if _newclass:Save = staticmethod(_af.StringParameter_Save)
StringParameter_swigregister = _af.StringParameter_swigregister
StringParameter_swigregister(StringParameter)
StringParameter_Add = _af.StringParameter_Add
StringParameter_Get = _af.StringParameter_Get
StringParameter_SetName = _af.StringParameter_SetName
StringParameter_Close = _af.StringParameter_Close
StringParameter_Save = _af.StringParameter_Save

class LVPS_TException:
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LVPS_TException, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LVPS_TException, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_LVPS_TException(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_LVPS_TException
    __del__ = lambda self : None;
    def GetError(*args): return _af.LVPS_TException_GetError(*args)
LVPS_TException_swigregister = _af.LVPS_TException_swigregister
LVPS_TException_swigregister(LVPS_TException)

class NoExistException(LVPS_TException):
    __swig_setmethods__ = {}
    for _s in [LVPS_TException]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, NoExistException, name, value)
    __swig_getmethods__ = {}
    for _s in [LVPS_TException]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, NoExistException, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_NoExistException(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_NoExistException
    __del__ = lambda self : None;
    def GetElement(*args): return _af.NoExistException_GetElement(*args)
NoExistException_swigregister = _af.NoExistException_swigregister
NoExistException_swigregister(NoExistException)

class NoLabelInicialisationException(LVPS_TException):
    __swig_setmethods__ = {}
    for _s in [LVPS_TException]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, NoLabelInicialisationException, name, value)
    __swig_getmethods__ = {}
    for _s in [LVPS_TException]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, NoLabelInicialisationException, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_NoLabelInicialisationException(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_NoLabelInicialisationException
    __del__ = lambda self : None;
NoLabelInicialisationException_swigregister = _af.NoLabelInicialisationException_swigregister
NoLabelInicialisationException_swigregister(NoLabelInicialisationException)

class COMMON(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, COMMON, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, COMMON, name)
    __repr__ = _swig_repr
    __swig_setmethods__["TIME"] = _af.COMMON_TIME_set
    __swig_getmethods__["TIME"] = _af.COMMON_TIME_get
    if _newclass:TIME = _swig_property(_af.COMMON_TIME_get, _af.COMMON_TIME_set)
    __swig_setmethods__["STEP"] = _af.COMMON_STEP_set
    __swig_getmethods__["STEP"] = _af.COMMON_STEP_get
    if _newclass:STEP = _swig_property(_af.COMMON_STEP_get, _af.COMMON_STEP_set)
    __swig_setmethods__["STEP01"] = _af.COMMON_STEP01_set
    __swig_getmethods__["STEP01"] = _af.COMMON_STEP01_get
    if _newclass:STEP01 = _swig_property(_af.COMMON_STEP01_get, _af.COMMON_STEP01_set)
    __swig_setmethods__["STEP02"] = _af.COMMON_STEP02_set
    __swig_getmethods__["STEP02"] = _af.COMMON_STEP02_get
    if _newclass:STEP02 = _swig_property(_af.COMMON_STEP02_get, _af.COMMON_STEP02_set)
    __swig_setmethods__["DT"] = _af.COMMON_DT_set
    __swig_getmethods__["DT"] = _af.COMMON_DT_get
    if _newclass:DT = _swig_property(_af.COMMON_DT_get, _af.COMMON_DT_set)
    __swig_setmethods__["DABSI"] = _af.COMMON_DABSI_set
    __swig_getmethods__["DABSI"] = _af.COMMON_DABSI_get
    if _newclass:DABSI = _swig_property(_af.COMMON_DABSI_get, _af.COMMON_DABSI_set)
    __swig_setmethods__["DRLTI"] = _af.COMMON_DRLTI_set
    __swig_getmethods__["DRLTI"] = _af.COMMON_DRLTI_get
    if _newclass:DRLTI = _swig_property(_af.COMMON_DRLTI_get, _af.COMMON_DRLTI_set)
    __swig_setmethods__["STEPMD"] = _af.COMMON_STEPMD_set
    __swig_getmethods__["STEPMD"] = _af.COMMON_STEPMD_get
    if _newclass:STEPMD = _swig_property(_af.COMMON_STEPMD_get, _af.COMMON_STEPMD_set)
    __swig_setmethods__["TIMEND"] = _af.COMMON_TIMEND_set
    __swig_getmethods__["TIMEND"] = _af.COMMON_TIMEND_get
    if _newclass:TIMEND = _swig_property(_af.COMMON_TIMEND_get, _af.COMMON_TIMEND_set)
    __swig_setmethods__["NAME"] = _af.COMMON_NAME_set
    __swig_getmethods__["NAME"] = _af.COMMON_NAME_get
    if _newclass:NAME = _swig_property(_af.COMMON_NAME_get, _af.COMMON_NAME_set)
    __swig_setmethods__["NSTEP"] = _af.COMMON_NSTEP_set
    __swig_getmethods__["NSTEP"] = _af.COMMON_NSTEP_get
    if _newclass:NSTEP = _swig_property(_af.COMMON_NSTEP_get, _af.COMMON_NSTEP_set)
    __swig_setmethods__["SYSPRN"] = _af.COMMON_SYSPRN_set
    __swig_getmethods__["SYSPRN"] = _af.COMMON_SYSPRN_get
    if _newclass:SYSPRN = _swig_property(_af.COMMON_SYSPRN_get, _af.COMMON_SYSPRN_set)
    __swig_setmethods__["NITER"] = _af.COMMON_NITER_set
    __swig_getmethods__["NITER"] = _af.COMMON_NITER_get
    if _newclass:NITER = _swig_property(_af.COMMON_NITER_get, _af.COMMON_NITER_set)
    __swig_setmethods__["ITR"] = _af.COMMON_ITR_set
    __swig_getmethods__["ITR"] = _af.COMMON_ITR_get
    if _newclass:ITR = _swig_property(_af.COMMON_ITR_get, _af.COMMON_ITR_set)
    __swig_setmethods__["CODE"] = _af.COMMON_CODE_set
    __swig_getmethods__["CODE"] = _af.COMMON_CODE_get
    if _newclass:CODE = _swig_property(_af.COMMON_CODE_get, _af.COMMON_CODE_set)
    __swig_setmethods__["NUMINT"] = _af.COMMON_NUMINT_set
    __swig_getmethods__["NUMINT"] = _af.COMMON_NUMINT_get
    if _newclass:NUMINT = _swig_property(_af.COMMON_NUMINT_get, _af.COMMON_NUMINT_set)
    __swig_setmethods__["NUMPRV"] = _af.COMMON_NUMPRV_set
    __swig_getmethods__["NUMPRV"] = _af.COMMON_NUMPRV_get
    if _newclass:NUMPRV = _swig_property(_af.COMMON_NUMPRV_get, _af.COMMON_NUMPRV_set)
    __swig_setmethods__["CODSTP"] = _af.COMMON_CODSTP_set
    __swig_getmethods__["CODSTP"] = _af.COMMON_CODSTP_get
    if _newclass:CODSTP = _swig_property(_af.COMMON_CODSTP_get, _af.COMMON_CODSTP_set)
    __swig_setmethods__["CODGRF"] = _af.COMMON_CODGRF_set
    __swig_getmethods__["CODGRF"] = _af.COMMON_CODGRF_get
    if _newclass:CODGRF = _swig_property(_af.COMMON_CODGRF_get, _af.COMMON_CODGRF_set)
    __swig_setmethods__["NEWINT"] = _af.COMMON_NEWINT_set
    __swig_getmethods__["NEWINT"] = _af.COMMON_NEWINT_get
    if _newclass:NEWINT = _swig_property(_af.COMMON_NEWINT_get, _af.COMMON_NEWINT_set)
    __swig_setmethods__["MINSTP"] = _af.COMMON_MINSTP_set
    __swig_getmethods__["MINSTP"] = _af.COMMON_MINSTP_get
    if _newclass:MINSTP = _swig_property(_af.COMMON_MINSTP_get, _af.COMMON_MINSTP_set)
    def __init__(self, *args): 
        this = _af.new_COMMON(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_COMMON
    __del__ = lambda self : None;
COMMON_swigregister = _af.COMMON_swigregister
COMMON_swigregister(COMMON)

class SolverContext(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SolverContext, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SolverContext, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_SolverContext(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_SolverContext
    __del__ = lambda self : None;
    def Read(*args): return _af.SolverContext_Read(*args)
    def GetVersion(*args): return _af.SolverContext_GetVersion(*args)
    def GetCreationDate(*args): return _af.SolverContext_GetCreationDate(*args)
    def GetDescription(*args): return _af.SolverContext_GetDescription(*args)
    def GetPermanentCodeTableLength(*args): return _af.SolverContext_GetPermanentCodeTableLength(*args)
    def GetVariableCodeTableLength(*args): return _af.SolverContext_GetVariableCodeTableLength(*args)
    def GetPermanentCodeTable(*args): return _af.SolverContext_GetPermanentCodeTable(*args)
    def GetVariableCodeTable(*args): return _af.SolverContext_GetVariableCodeTable(*args)
    def GetIntegrationParamLength(*args): return _af.SolverContext_GetIntegrationParamLength(*args)
    def GetIntegrationParam(*args): return _af.SolverContext_GetIntegrationParam(*args)
    def GetParLength(*args): return _af.SolverContext_GetParLength(*args)
    def GetPar(*args): return _af.SolverContext_GetPar(*args)
    def GetASMILength(*args): return _af.SolverContext_GetASMILength(*args)
    def GetASMI(*args): return _af.SolverContext_GetASMI(*args)
    def GetASMMLength(*args): return _af.SolverContext_GetASMMLength(*args)
    def GetASMM(*args): return _af.SolverContext_GetASMM(*args)
    def GetANUZLLength(*args): return _af.SolverContext_GetANUZLLength(*args)
    def GetANUZL(*args): return _af.SolverContext_GetANUZL(*args)
    def GetASMOLength(*args): return _af.SolverContext_GetASMOLength(*args)
    def GetASMO(*args): return _af.SolverContext_GetASMO(*args)
    def GetASYSOLength(*args): return _af.SolverContext_GetASYSOLength(*args)
    def GetASYSO(*args): return _af.SolverContext_GetASYSO(*args)
    def GetModelStructureLength(*args): return _af.SolverContext_GetModelStructureLength(*args)
    def GetModelStructure(*args): return _af.SolverContext_GetModelStructure(*args)
    def GetModelSize(*args): return _af.SolverContext_GetModelSize(*args)
    def GetModelNames(*args): return _af.SolverContext_GetModelNames(*args)
    def GetPRVPSize(*args): return _af.SolverContext_GetPRVPSize(*args)
    def GetOVPNames(*args): return _af.SolverContext_GetOVPNames(*args)
    def GetPGOSize(*args): return _af.SolverContext_GetPGOSize(*args)
    def GetPGONames(*args): return _af.SolverContext_GetPGONames(*args)
    def GetPGOStructure(*args): return _af.SolverContext_GetPGOStructure(*args)
    def GetLayerSize(*args): return _af.SolverContext_GetLayerSize(*args)
    def Refresh(*args): return _af.SolverContext_Refresh(*args)
    def SetLayer(*args): return _af.SolverContext_SetLayer(*args)
    def GetVariableInt(*args): return _af.SolverContext_GetVariableInt(*args)
    def GetVariableDouble(*args): return _af.SolverContext_GetVariableDouble(*args)
    def GetVariableLength(*args): return _af.SolverContext_GetVariableLength(*args)
    def GetCOMMON(*args): return _af.SolverContext_GetCOMMON(*args)
    def GetTime(*args): return _af.SolverContext_GetTime(*args)
    def GetCurrLayer(*args): return _af.SolverContext_GetCurrLayer(*args)
    def Reset(*args): return _af.SolverContext_Reset(*args)
    __swig_setmethods__["FileName"] = _af.SolverContext_FileName_set
    __swig_getmethods__["FileName"] = _af.SolverContext_FileName_get
    if _newclass:FileName = _swig_property(_af.SolverContext_FileName_get, _af.SolverContext_FileName_set)
SolverContext_swigregister = _af.SolverContext_swigregister
SolverContext_swigregister(SolverContext)

class OutVariableContext(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OutVariableContext, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OutVariableContext, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_OutVariableContext(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_OutVariableContext
    __del__ = lambda self : None;
    def SetLayer(*args): return _af.OutVariableContext_SetLayer(*args)
    def GetLength(*args): return _af.OutVariableContext_GetLength(*args)
    def GetOutVariable(*args): return _af.OutVariableContext_GetOutVariable(*args)
    def SetPRVPNumber(*args): return _af.OutVariableContext_SetPRVPNumber(*args)
    def GetParLength(*args): return _af.OutVariableContext_GetParLength(*args)
    def GetPar(*args): return _af.OutVariableContext_GetPar(*args)
    def GetOVPName(*args): return _af.OutVariableContext_GetOVPName(*args)
OutVariableContext_swigregister = _af.OutVariableContext_swigregister
OutVariableContext_swigregister(OutVariableContext)

class DOF(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DOF, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DOF, name)
    __repr__ = _swig_repr
    __swig_setmethods__["X"] = _af.DOF_X_set
    __swig_getmethods__["X"] = _af.DOF_X_get
    if _newclass:X = _swig_property(_af.DOF_X_get, _af.DOF_X_set)
    __swig_setmethods__["V"] = _af.DOF_V_set
    __swig_getmethods__["V"] = _af.DOF_V_get
    if _newclass:V = _swig_property(_af.DOF_V_get, _af.DOF_V_set)
    __swig_setmethods__["A"] = _af.DOF_A_set
    __swig_getmethods__["A"] = _af.DOF_A_get
    if _newclass:A = _swig_property(_af.DOF_A_get, _af.DOF_A_set)
    def __init__(self, *args): 
        this = _af.new_DOF(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_DOF
    __del__ = lambda self : None;
DOF_swigregister = _af.DOF_swigregister
DOF_swigregister(DOF)

class DOFContext(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DOFContext, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DOFContext, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _af.new_DOFContext(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _af.delete_DOFContext
    __del__ = lambda self : None;
    def Init(*args): return _af.DOFContext_Init(*args)
    def SetLayer(*args): return _af.DOFContext_SetLayer(*args)
    def GetLength(*args): return _af.DOFContext_GetLength(*args)
    def GetDOF(*args): return _af.DOFContext_GetDOF(*args)
DOFContext_swigregister = _af.DOFContext_swigregister
DOFContext_swigregister(DOFContext)

GetEnv = _af.GetEnv
ExecCommand = _af.ExecCommand


