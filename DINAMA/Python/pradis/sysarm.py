# This file was created automatically by SWIG 1.3.30.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _sysarm
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


class BaseElement(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BaseElement, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BaseElement, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _sysarm.delete_BaseElement
    __del__ = lambda self : None;
    __swig_setmethods__["Name"] = _sysarm.BaseElement_Name_set
    __swig_getmethods__["Name"] = _sysarm.BaseElement_Name_get
    if _newclass:Name = _swig_property(_sysarm.BaseElement_Name_get, _sysarm.BaseElement_Name_set)
    __swig_setmethods__["Alias"] = _sysarm.BaseElement_Alias_set
    __swig_getmethods__["Alias"] = _sysarm.BaseElement_Alias_get
    if _newclass:Alias = _swig_property(_sysarm.BaseElement_Alias_get, _sysarm.BaseElement_Alias_set)
    __swig_setmethods__["Module"] = _sysarm.BaseElement_Module_set
    __swig_getmethods__["Module"] = _sysarm.BaseElement_Module_get
    if _newclass:Module = _swig_property(_sysarm.BaseElement_Module_get, _sysarm.BaseElement_Module_set)
    __swig_setmethods__["RuDescription"] = _sysarm.BaseElement_RuDescription_set
    __swig_getmethods__["RuDescription"] = _sysarm.BaseElement_RuDescription_get
    if _newclass:RuDescription = _swig_property(_sysarm.BaseElement_RuDescription_get, _sysarm.BaseElement_RuDescription_set)
    __swig_setmethods__["EnDescription"] = _sysarm.BaseElement_EnDescription_set
    __swig_getmethods__["EnDescription"] = _sysarm.BaseElement_EnDescription_get
    if _newclass:EnDescription = _swig_property(_sysarm.BaseElement_EnDescription_get, _sysarm.BaseElement_EnDescription_set)
    __swig_setmethods__["Priority"] = _sysarm.BaseElement_Priority_set
    __swig_getmethods__["Priority"] = _sysarm.BaseElement_Priority_get
    if _newclass:Priority = _swig_property(_sysarm.BaseElement_Priority_get, _sysarm.BaseElement_Priority_set)
    def SetName(*args): return _sysarm.BaseElement_SetName(*args)
    def SetAlias(*args): return _sysarm.BaseElement_SetAlias(*args)
    def SetRuDescription(*args): return _sysarm.BaseElement_SetRuDescription(*args)
    def SetEnDescription(*args): return _sysarm.BaseElement_SetEnDescription(*args)
    def GetName(*args): return _sysarm.BaseElement_GetName(*args)
    def GetAlias(*args): return _sysarm.BaseElement_GetAlias(*args)
    def GetRuDescription(*args): return _sysarm.BaseElement_GetRuDescription(*args)
    def GetEnDescription(*args): return _sysarm.BaseElement_GetEnDescription(*args)
    def SetModule(*args): return _sysarm.BaseElement_SetModule(*args)
    def GetModule(*args): return _sysarm.BaseElement_GetModule(*args)
    def SetPriority(*args): return _sysarm.BaseElement_SetPriority(*args)
    def GetPriority(*args): return _sysarm.BaseElement_GetPriority(*args)
    def write(*args): return _sysarm.BaseElement_write(*args)
    def GetNodeType(*args): return _sysarm.BaseElement_GetNodeType(*args)
    def GetNodeName(*args): return _sysarm.BaseElement_GetNodeName(*args)
    def GetNodeRuDescription(*args): return _sysarm.BaseElement_GetNodeRuDescription(*args)
    def GetNodeEnDescription(*args): return _sysarm.BaseElement_GetNodeEnDescription(*args)
    def GetParameterType(*args): return _sysarm.BaseElement_GetParameterType(*args)
    def GetParameterName(*args): return _sysarm.BaseElement_GetParameterName(*args)
    def GetParameterDefaultValue(*args): return _sysarm.BaseElement_GetParameterDefaultValue(*args)
    def GetParameterEnDescription(*args): return _sysarm.BaseElement_GetParameterEnDescription(*args)
    def GetParameterRuDescription(*args): return _sysarm.BaseElement_GetParameterRuDescription(*args)
    def GetType(*args): return _sysarm.BaseElement_GetType(*args)
    __swig_setmethods__["NodeTypes"] = _sysarm.BaseElement_NodeTypes_set
    __swig_getmethods__["NodeTypes"] = _sysarm.BaseElement_NodeTypes_get
    if _newclass:NodeTypes = _swig_property(_sysarm.BaseElement_NodeTypes_get, _sysarm.BaseElement_NodeTypes_set)
    __swig_setmethods__["NodeNames"] = _sysarm.BaseElement_NodeNames_set
    __swig_getmethods__["NodeNames"] = _sysarm.BaseElement_NodeNames_get
    if _newclass:NodeNames = _swig_property(_sysarm.BaseElement_NodeNames_get, _sysarm.BaseElement_NodeNames_set)
    __swig_setmethods__["ParameterTypes"] = _sysarm.BaseElement_ParameterTypes_set
    __swig_getmethods__["ParameterTypes"] = _sysarm.BaseElement_ParameterTypes_get
    if _newclass:ParameterTypes = _swig_property(_sysarm.BaseElement_ParameterTypes_get, _sysarm.BaseElement_ParameterTypes_set)
    __swig_setmethods__["ParameterNames"] = _sysarm.BaseElement_ParameterNames_set
    __swig_getmethods__["ParameterNames"] = _sysarm.BaseElement_ParameterNames_get
    if _newclass:ParameterNames = _swig_property(_sysarm.BaseElement_ParameterNames_get, _sysarm.BaseElement_ParameterNames_set)
    __swig_setmethods__["ParameterDefaultValue"] = _sysarm.BaseElement_ParameterDefaultValue_set
    __swig_getmethods__["ParameterDefaultValue"] = _sysarm.BaseElement_ParameterDefaultValue_get
    if _newclass:ParameterDefaultValue = _swig_property(_sysarm.BaseElement_ParameterDefaultValue_get, _sysarm.BaseElement_ParameterDefaultValue_set)
    __swig_setmethods__["NodeRuDescription"] = _sysarm.BaseElement_NodeRuDescription_set
    __swig_getmethods__["NodeRuDescription"] = _sysarm.BaseElement_NodeRuDescription_get
    if _newclass:NodeRuDescription = _swig_property(_sysarm.BaseElement_NodeRuDescription_get, _sysarm.BaseElement_NodeRuDescription_set)
    __swig_setmethods__["NodeEnDescription"] = _sysarm.BaseElement_NodeEnDescription_set
    __swig_getmethods__["NodeEnDescription"] = _sysarm.BaseElement_NodeEnDescription_get
    if _newclass:NodeEnDescription = _swig_property(_sysarm.BaseElement_NodeEnDescription_get, _sysarm.BaseElement_NodeEnDescription_set)
    __swig_setmethods__["ParameterRuDescription"] = _sysarm.BaseElement_ParameterRuDescription_set
    __swig_getmethods__["ParameterRuDescription"] = _sysarm.BaseElement_ParameterRuDescription_get
    if _newclass:ParameterRuDescription = _swig_property(_sysarm.BaseElement_ParameterRuDescription_get, _sysarm.BaseElement_ParameterRuDescription_set)
    __swig_setmethods__["ParameterEnDescription"] = _sysarm.BaseElement_ParameterEnDescription_set
    __swig_getmethods__["ParameterEnDescription"] = _sysarm.BaseElement_ParameterEnDescription_get
    if _newclass:ParameterEnDescription = _swig_property(_sysarm.BaseElement_ParameterEnDescription_get, _sysarm.BaseElement_ParameterEnDescription_set)
    __swig_setmethods__["Image2"] = _sysarm.BaseElement_Image2_set
    __swig_getmethods__["Image2"] = _sysarm.BaseElement_Image2_get
    if _newclass:Image2 = _swig_property(_sysarm.BaseElement_Image2_get, _sysarm.BaseElement_Image2_set)
BaseElement_swigregister = _sysarm.BaseElement_swigregister
BaseElement_swigregister(BaseElement)

class CommonSaxHandler(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CommonSaxHandler, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CommonSaxHandler, name)
    __repr__ = _swig_repr
    __swig_getmethods__["setPriority"] = lambda x: _sysarm.CommonSaxHandler_setPriority
    if _newclass:setPriority = staticmethod(_sysarm.CommonSaxHandler_setPriority)
    __swig_getmethods__["image2dAnalyser"] = lambda x: _sysarm.CommonSaxHandler_image2dAnalyser
    if _newclass:image2dAnalyser = staticmethod(_sysarm.CommonSaxHandler_image2dAnalyser)
    __swig_setmethods__["code"] = _sysarm.CommonSaxHandler_code_set
    __swig_getmethods__["code"] = _sysarm.CommonSaxHandler_code_get
    if _newclass:code = _swig_property(_sysarm.CommonSaxHandler_code_get, _sysarm.CommonSaxHandler_code_set)
    def GetErrorText(*args): return _sysarm.CommonSaxHandler_GetErrorText(*args)
    def __init__(self, *args): 
        this = _sysarm.new_CommonSaxHandler(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sysarm.delete_CommonSaxHandler
    __del__ = lambda self : None;
CommonSaxHandler_swigregister = _sysarm.CommonSaxHandler_swigregister
CommonSaxHandler_swigregister(CommonSaxHandler)
CommonSaxHandler_setPriority = _sysarm.CommonSaxHandler_setPriority
CommonSaxHandler_image2dAnalyser = _sysarm.CommonSaxHandler_image2dAnalyser

class Field(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Field, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Field, name)
    __repr__ = _swig_repr
    __swig_setmethods__["Name"] = _sysarm.Field_Name_set
    __swig_getmethods__["Name"] = _sysarm.Field_Name_get
    if _newclass:Name = _swig_property(_sysarm.Field_Name_get, _sysarm.Field_Name_set)
    __swig_setmethods__["Type"] = _sysarm.Field_Type_set
    __swig_getmethods__["Type"] = _sysarm.Field_Type_get
    if _newclass:Type = _swig_property(_sysarm.Field_Type_get, _sysarm.Field_Type_set)
    __swig_setmethods__["RuDescription"] = _sysarm.Field_RuDescription_set
    __swig_getmethods__["RuDescription"] = _sysarm.Field_RuDescription_get
    if _newclass:RuDescription = _swig_property(_sysarm.Field_RuDescription_get, _sysarm.Field_RuDescription_set)
    __swig_setmethods__["EnDescription"] = _sysarm.Field_EnDescription_set
    __swig_getmethods__["EnDescription"] = _sysarm.Field_EnDescription_get
    if _newclass:EnDescription = _swig_property(_sysarm.Field_EnDescription_get, _sysarm.Field_EnDescription_set)
    def __init__(self, *args): 
        this = _sysarm.new_Field(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sysarm.delete_Field
    __del__ = lambda self : None;
Field_swigregister = _sysarm.Field_swigregister
Field_swigregister(Field)

class Image2d(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Image2d, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Image2d, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _sysarm.new_Image2d(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["icon"] = _sysarm.Image2d_icon_set
    __swig_getmethods__["icon"] = _sysarm.Image2d_icon_get
    if _newclass:icon = _swig_property(_sysarm.Image2d_icon_get, _sysarm.Image2d_icon_set)
    __swig_setmethods__["Symbol"] = _sysarm.Image2d_Symbol_set
    __swig_getmethods__["Symbol"] = _sysarm.Image2d_Symbol_get
    if _newclass:Symbol = _swig_property(_sysarm.Image2d_Symbol_get, _sysarm.Image2d_Symbol_set)
    __swig_destroy__ = _sysarm.delete_Image2d
    __del__ = lambda self : None;
Image2d_swigregister = _sysarm.Image2d_swigregister
Image2d_swigregister(Image2d)

class Image(BaseElement):
    __swig_setmethods__ = {}
    for _s in [BaseElement]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, Image, name, value)
    __swig_getmethods__ = {}
    for _s in [BaseElement]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, Image, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _sysarm.new_Image(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["ext"] = _sysarm.Image_ext_set
    __swig_getmethods__["ext"] = _sysarm.Image_ext_get
    if _newclass:ext = _swig_property(_sysarm.Image_ext_get, _sysarm.Image_ext_set)
    __swig_setmethods__["par"] = _sysarm.Image_par_set
    __swig_getmethods__["par"] = _sysarm.Image_par_get
    if _newclass:par = _swig_property(_sysarm.Image_par_get, _sysarm.Image_par_set)
    __swig_setmethods__["wrk"] = _sysarm.Image_wrk_set
    __swig_getmethods__["wrk"] = _sysarm.Image_wrk_get
    if _newclass:wrk = _swig_property(_sysarm.Image_wrk_get, _sysarm.Image_wrk_set)
    __swig_setmethods__["vps"] = _sysarm.Image_vps_set
    __swig_getmethods__["vps"] = _sysarm.Image_vps_get
    if _newclass:vps = _swig_property(_sysarm.Image_vps_get, _sysarm.Image_vps_set)
    __swig_setmethods__["vpr"] = _sysarm.Image_vpr_set
    __swig_getmethods__["vpr"] = _sysarm.Image_vpr_get
    if _newclass:vpr = _swig_property(_sysarm.Image_vpr_get, _sysarm.Image_vpr_set)
    __swig_setmethods__["unv"] = _sysarm.Image_unv_set
    __swig_getmethods__["unv"] = _sysarm.Image_unv_get
    if _newclass:unv = _swig_property(_sysarm.Image_unv_get, _sysarm.Image_unv_set)
    __swig_setmethods__["wrs"] = _sysarm.Image_wrs_set
    __swig_getmethods__["wrs"] = _sysarm.Image_wrs_get
    if _newclass:wrs = _swig_property(_sysarm.Image_wrs_get, _sysarm.Image_wrs_set)
    __swig_setmethods__["ParameterLinkTypes"] = _sysarm.Image_ParameterLinkTypes_set
    __swig_getmethods__["ParameterLinkTypes"] = _sysarm.Image_ParameterLinkTypes_get
    if _newclass:ParameterLinkTypes = _swig_property(_sysarm.Image_ParameterLinkTypes_get, _sysarm.Image_ParameterLinkTypes_set)
    __swig_setmethods__["ParameterNodeLinks"] = _sysarm.Image_ParameterNodeLinks_set
    __swig_getmethods__["ParameterNodeLinks"] = _sysarm.Image_ParameterNodeLinks_get
    if _newclass:ParameterNodeLinks = _swig_property(_sysarm.Image_ParameterNodeLinks_get, _sysarm.Image_ParameterNodeLinks_set)
    def SetExt(*args): return _sysarm.Image_SetExt(*args)
    def SetPar(*args): return _sysarm.Image_SetPar(*args)
    def GetExt(*args): return _sysarm.Image_GetExt(*args)
    def GetPar(*args): return _sysarm.Image_GetPar(*args)
    def write(*args): return _sysarm.Image_write(*args)
    def GetType(*args): return _sysarm.Image_GetType(*args)
    __swig_destroy__ = _sysarm.delete_Image
    __del__ = lambda self : None;
Image_swigregister = _sysarm.Image_swigregister
Image_swigregister(Image)

class ImageSaxHandler(CommonSaxHandler):
    __swig_setmethods__ = {}
    for _s in [CommonSaxHandler]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, ImageSaxHandler, name, value)
    __swig_getmethods__ = {}
    for _s in [CommonSaxHandler]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, ImageSaxHandler, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _sysarm.new_ImageSaxHandler(*args)
        try: self.this.append(this)
        except: self.this = this
    def startElement(*args): return _sysarm.ImageSaxHandler_startElement(*args)
    def endElement(*args): return _sysarm.ImageSaxHandler_endElement(*args)
    def characters(*args): return _sysarm.ImageSaxHandler_characters(*args)
    def fatalError(*args): return _sysarm.ImageSaxHandler_fatalError(*args)
    __swig_setmethods__["DescriptionRus"] = _sysarm.ImageSaxHandler_DescriptionRus_set
    __swig_getmethods__["DescriptionRus"] = _sysarm.ImageSaxHandler_DescriptionRus_get
    if _newclass:DescriptionRus = _swig_property(_sysarm.ImageSaxHandler_DescriptionRus_get, _sysarm.ImageSaxHandler_DescriptionRus_set)
    __swig_setmethods__["DescriptionEng"] = _sysarm.ImageSaxHandler_DescriptionEng_set
    __swig_getmethods__["DescriptionEng"] = _sysarm.ImageSaxHandler_DescriptionEng_get
    if _newclass:DescriptionEng = _swig_property(_sysarm.ImageSaxHandler_DescriptionEng_get, _sysarm.ImageSaxHandler_DescriptionEng_set)
    __swig_destroy__ = _sysarm.delete_ImageSaxHandler
    __del__ = lambda self : None;
ImageSaxHandler_swigregister = _sysarm.ImageSaxHandler_swigregister
ImageSaxHandler_swigregister(ImageSaxHandler)

class Model(BaseElement):
    __swig_setmethods__ = {}
    for _s in [BaseElement]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, Model, name, value)
    __swig_getmethods__ = {}
    for _s in [BaseElement]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, Model, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _sysarm.new_Model(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["ext"] = _sysarm.Model_ext_set
    __swig_getmethods__["ext"] = _sysarm.Model_ext_get
    if _newclass:ext = _swig_property(_sysarm.Model_ext_get, _sysarm.Model_ext_set)
    __swig_setmethods__["ent"] = _sysarm.Model_ent_set
    __swig_getmethods__["ent"] = _sysarm.Model_ent_get
    if _newclass:ent = _swig_property(_sysarm.Model_ent_get, _sysarm.Model_ent_set)
    __swig_setmethods__["par"] = _sysarm.Model_par_set
    __swig_getmethods__["par"] = _sysarm.Model_par_get
    if _newclass:par = _swig_property(_sysarm.Model_par_get, _sysarm.Model_par_set)
    __swig_setmethods__["vpr"] = _sysarm.Model_vpr_set
    __swig_getmethods__["vpr"] = _sysarm.Model_vpr_get
    if _newclass:vpr = _swig_property(_sysarm.Model_vpr_get, _sysarm.Model_vpr_set)
    __swig_setmethods__["str"] = _sysarm.Model_str_set
    __swig_getmethods__["str"] = _sysarm.Model_str_get
    if _newclass:str = _swig_property(_sysarm.Model_str_get, _sysarm.Model_str_set)
    __swig_setmethods__["stp"] = _sysarm.Model_stp_set
    __swig_getmethods__["stp"] = _sysarm.Model_stp_get
    if _newclass:stp = _swig_property(_sysarm.Model_stp_get, _sysarm.Model_stp_set)
    __swig_setmethods__["wrk"] = _sysarm.Model_wrk_set
    __swig_getmethods__["wrk"] = _sysarm.Model_wrk_get
    if _newclass:wrk = _swig_property(_sysarm.Model_wrk_get, _sysarm.Model_wrk_set)
    __swig_setmethods__["wrp"] = _sysarm.Model_wrp_set
    __swig_getmethods__["wrp"] = _sysarm.Model_wrp_get
    if _newclass:wrp = _swig_property(_sysarm.Model_wrp_get, _sysarm.Model_wrp_set)
    __swig_setmethods__["adr"] = _sysarm.Model_adr_set
    __swig_getmethods__["adr"] = _sysarm.Model_adr_get
    if _newclass:adr = _swig_property(_sysarm.Model_adr_get, _sysarm.Model_adr_set)
    __swig_setmethods__["ign"] = _sysarm.Model_ign_set
    __swig_getmethods__["ign"] = _sysarm.Model_ign_get
    if _newclass:ign = _swig_property(_sysarm.Model_ign_get, _sysarm.Model_ign_set)
    __swig_setmethods__["Image"] = _sysarm.Model_Image_set
    __swig_getmethods__["Image"] = _sysarm.Model_Image_get
    if _newclass:Image = _swig_property(_sysarm.Model_Image_get, _sysarm.Model_Image_set)
    __swig_setmethods__["ParameterLinkTypes"] = _sysarm.Model_ParameterLinkTypes_set
    __swig_getmethods__["ParameterLinkTypes"] = _sysarm.Model_ParameterLinkTypes_get
    if _newclass:ParameterLinkTypes = _swig_property(_sysarm.Model_ParameterLinkTypes_get, _sysarm.Model_ParameterLinkTypes_set)
    __swig_setmethods__["ParameterNodeLinks"] = _sysarm.Model_ParameterNodeLinks_set
    __swig_getmethods__["ParameterNodeLinks"] = _sysarm.Model_ParameterNodeLinks_get
    if _newclass:ParameterNodeLinks = _swig_property(_sysarm.Model_ParameterNodeLinks_get, _sysarm.Model_ParameterNodeLinks_set)
    __swig_setmethods__["WorkRuDescription"] = _sysarm.Model_WorkRuDescription_set
    __swig_getmethods__["WorkRuDescription"] = _sysarm.Model_WorkRuDescription_get
    if _newclass:WorkRuDescription = _swig_property(_sysarm.Model_WorkRuDescription_get, _sysarm.Model_WorkRuDescription_set)
    __swig_setmethods__["WorkEnDescription"] = _sysarm.Model_WorkEnDescription_set
    __swig_getmethods__["WorkEnDescription"] = _sysarm.Model_WorkEnDescription_get
    if _newclass:WorkEnDescription = _swig_property(_sysarm.Model_WorkEnDescription_get, _sysarm.Model_WorkEnDescription_set)
    __swig_setmethods__["StateRuDescription"] = _sysarm.Model_StateRuDescription_set
    __swig_getmethods__["StateRuDescription"] = _sysarm.Model_StateRuDescription_get
    if _newclass:StateRuDescription = _swig_property(_sysarm.Model_StateRuDescription_get, _sysarm.Model_StateRuDescription_set)
    __swig_setmethods__["StateEnDescription"] = _sysarm.Model_StateEnDescription_set
    __swig_getmethods__["StateEnDescription"] = _sysarm.Model_StateEnDescription_get
    if _newclass:StateEnDescription = _swig_property(_sysarm.Model_StateEnDescription_get, _sysarm.Model_StateEnDescription_set)
    __swig_setmethods__["WorkParameterTypes"] = _sysarm.Model_WorkParameterTypes_set
    __swig_getmethods__["WorkParameterTypes"] = _sysarm.Model_WorkParameterTypes_get
    if _newclass:WorkParameterTypes = _swig_property(_sysarm.Model_WorkParameterTypes_get, _sysarm.Model_WorkParameterTypes_set)
    __swig_setmethods__["WorkParameterNames"] = _sysarm.Model_WorkParameterNames_set
    __swig_getmethods__["WorkParameterNames"] = _sysarm.Model_WorkParameterNames_get
    if _newclass:WorkParameterNames = _swig_property(_sysarm.Model_WorkParameterNames_get, _sysarm.Model_WorkParameterNames_set)
    __swig_setmethods__["StateParameterTypes"] = _sysarm.Model_StateParameterTypes_set
    __swig_getmethods__["StateParameterTypes"] = _sysarm.Model_StateParameterTypes_get
    if _newclass:StateParameterTypes = _swig_property(_sysarm.Model_StateParameterTypes_get, _sysarm.Model_StateParameterTypes_set)
    __swig_setmethods__["StateParameterNames"] = _sysarm.Model_StateParameterNames_set
    __swig_getmethods__["StateParameterNames"] = _sysarm.Model_StateParameterNames_get
    if _newclass:StateParameterNames = _swig_property(_sysarm.Model_StateParameterNames_get, _sysarm.Model_StateParameterNames_set)
    def SetExt(*args): return _sysarm.Model_SetExt(*args)
    def SetPar(*args): return _sysarm.Model_SetPar(*args)
    def SetAdr(*args): return _sysarm.Model_SetAdr(*args)
    def GetExt(*args): return _sysarm.Model_GetExt(*args)
    def GetPar(*args): return _sysarm.Model_GetPar(*args)
    def GetAdr(*args): return _sysarm.Model_GetAdr(*args)
    def write(*args): return _sysarm.Model_write(*args)
    def GetType(*args): return _sysarm.Model_GetType(*args)
    __swig_destroy__ = _sysarm.delete_Model
    __del__ = lambda self : None;
Model_swigregister = _sysarm.Model_swigregister
Model_swigregister(Model)

class ModelSaxHandler(CommonSaxHandler):
    __swig_setmethods__ = {}
    for _s in [CommonSaxHandler]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, ModelSaxHandler, name, value)
    __swig_getmethods__ = {}
    for _s in [CommonSaxHandler]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, ModelSaxHandler, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _sysarm.new_ModelSaxHandler(*args)
        try: self.this.append(this)
        except: self.this = this
    def startElement(*args): return _sysarm.ModelSaxHandler_startElement(*args)
    def endElement(*args): return _sysarm.ModelSaxHandler_endElement(*args)
    def characters(*args): return _sysarm.ModelSaxHandler_characters(*args)
    def fatalError(*args): return _sysarm.ModelSaxHandler_fatalError(*args)
    __swig_setmethods__["DescriptionRus"] = _sysarm.ModelSaxHandler_DescriptionRus_set
    __swig_getmethods__["DescriptionRus"] = _sysarm.ModelSaxHandler_DescriptionRus_get
    if _newclass:DescriptionRus = _swig_property(_sysarm.ModelSaxHandler_DescriptionRus_get, _sysarm.ModelSaxHandler_DescriptionRus_set)
    __swig_setmethods__["DescriptionEng"] = _sysarm.ModelSaxHandler_DescriptionEng_set
    __swig_getmethods__["DescriptionEng"] = _sysarm.ModelSaxHandler_DescriptionEng_get
    if _newclass:DescriptionEng = _swig_property(_sysarm.ModelSaxHandler_DescriptionEng_get, _sysarm.ModelSaxHandler_DescriptionEng_set)
    __swig_destroy__ = _sysarm.delete_ModelSaxHandler
    __del__ = lambda self : None;
ModelSaxHandler_swigregister = _sysarm.ModelSaxHandler_swigregister
ModelSaxHandler_swigregister(ModelSaxHandler)

class Module(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Module, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Module, name)
    __repr__ = _swig_repr
    __swig_setmethods__["Name"] = _sysarm.Module_Name_set
    __swig_getmethods__["Name"] = _sysarm.Module_Name_get
    if _newclass:Name = _swig_property(_sysarm.Module_Name_get, _sysarm.Module_Name_set)
    __swig_setmethods__["RuDescription"] = _sysarm.Module_RuDescription_set
    __swig_getmethods__["RuDescription"] = _sysarm.Module_RuDescription_get
    if _newclass:RuDescription = _swig_property(_sysarm.Module_RuDescription_get, _sysarm.Module_RuDescription_set)
    __swig_setmethods__["EnDescription"] = _sysarm.Module_EnDescription_set
    __swig_getmethods__["EnDescription"] = _sysarm.Module_EnDescription_get
    if _newclass:EnDescription = _swig_property(_sysarm.Module_EnDescription_get, _sysarm.Module_EnDescription_set)
    def __init__(self, *args): 
        this = _sysarm.new_Module(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["Models"] = _sysarm.Module_Models_set
    __swig_getmethods__["Models"] = _sysarm.Module_Models_get
    if _newclass:Models = _swig_property(_sysarm.Module_Models_get, _sysarm.Module_Models_set)
    __swig_setmethods__["OVPs"] = _sysarm.Module_OVPs_set
    __swig_getmethods__["OVPs"] = _sysarm.Module_OVPs_get
    if _newclass:OVPs = _swig_property(_sysarm.Module_OVPs_get, _sysarm.Module_OVPs_set)
    __swig_setmethods__["Images"] = _sysarm.Module_Images_set
    __swig_getmethods__["Images"] = _sysarm.Module_Images_get
    if _newclass:Images = _swig_property(_sysarm.Module_Images_get, _sysarm.Module_Images_set)
    __swig_setmethods__["Nodes"] = _sysarm.Module_Nodes_set
    __swig_getmethods__["Nodes"] = _sysarm.Module_Nodes_get
    if _newclass:Nodes = _swig_property(_sysarm.Module_Nodes_get, _sysarm.Module_Nodes_set)
    __swig_setmethods__["Parameters"] = _sysarm.Module_Parameters_set
    __swig_getmethods__["Parameters"] = _sysarm.Module_Parameters_get
    if _newclass:Parameters = _swig_property(_sysarm.Module_Parameters_get, _sysarm.Module_Parameters_set)
    __swig_setmethods__["Objects"] = _sysarm.Module_Objects_set
    __swig_getmethods__["Objects"] = _sysarm.Module_Objects_get
    if _newclass:Objects = _swig_property(_sysarm.Module_Objects_get, _sysarm.Module_Objects_set)
    def SetName(*args): return _sysarm.Module_SetName(*args)
    def SetRuDescription(*args): return _sysarm.Module_SetRuDescription(*args)
    def SetEnDescription(*args): return _sysarm.Module_SetEnDescription(*args)
    def GetName(*args): return _sysarm.Module_GetName(*args)
    def GetRuDescription(*args): return _sysarm.Module_GetRuDescription(*args)
    def GetEnDescription(*args): return _sysarm.Module_GetEnDescription(*args)
    def GetElement(*args): return _sysarm.Module_GetElement(*args)
    def AddElement(*args): return _sysarm.Module_AddElement(*args)
    def write(*args): return _sysarm.Module_write(*args)
    __swig_destroy__ = _sysarm.delete_Module
    __del__ = lambda self : None;
Module_swigregister = _sysarm.Module_swigregister
Module_swigregister(Module)

class ModuleSaxHandler(CommonSaxHandler):
    __swig_setmethods__ = {}
    for _s in [CommonSaxHandler]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, ModuleSaxHandler, name, value)
    __swig_getmethods__ = {}
    for _s in [CommonSaxHandler]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, ModuleSaxHandler, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _sysarm.new_ModuleSaxHandler(*args)
        try: self.this.append(this)
        except: self.this = this
    def startElement(*args): return _sysarm.ModuleSaxHandler_startElement(*args)
    def endElement(*args): return _sysarm.ModuleSaxHandler_endElement(*args)
    def characters(*args): return _sysarm.ModuleSaxHandler_characters(*args)
    def fatalError(*args): return _sysarm.ModuleSaxHandler_fatalError(*args)
    __swig_setmethods__["DescriptionRus"] = _sysarm.ModuleSaxHandler_DescriptionRus_set
    __swig_getmethods__["DescriptionRus"] = _sysarm.ModuleSaxHandler_DescriptionRus_get
    if _newclass:DescriptionRus = _swig_property(_sysarm.ModuleSaxHandler_DescriptionRus_get, _sysarm.ModuleSaxHandler_DescriptionRus_set)
    __swig_setmethods__["DescriptionEng"] = _sysarm.ModuleSaxHandler_DescriptionEng_set
    __swig_getmethods__["DescriptionEng"] = _sysarm.ModuleSaxHandler_DescriptionEng_get
    if _newclass:DescriptionEng = _swig_property(_sysarm.ModuleSaxHandler_DescriptionEng_get, _sysarm.ModuleSaxHandler_DescriptionEng_set)
    __swig_destroy__ = _sysarm.delete_ModuleSaxHandler
    __del__ = lambda self : None;
ModuleSaxHandler_swigregister = _sysarm.ModuleSaxHandler_swigregister
ModuleSaxHandler_swigregister(ModuleSaxHandler)

class Node(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Node, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Node, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _sysarm.new_Node(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["FieldList"] = _sysarm.Node_FieldList_set
    __swig_getmethods__["FieldList"] = _sysarm.Node_FieldList_get
    if _newclass:FieldList = _swig_property(_sysarm.Node_FieldList_get, _sysarm.Node_FieldList_set)
    def SetName(*args): return _sysarm.Node_SetName(*args)
    def SetRuDescription(*args): return _sysarm.Node_SetRuDescription(*args)
    def SetEnDescription(*args): return _sysarm.Node_SetEnDescription(*args)
    def GetName(*args): return _sysarm.Node_GetName(*args)
    def GetRuDescription(*args): return _sysarm.Node_GetRuDescription(*args)
    def GetEnDescription(*args): return _sysarm.Node_GetEnDescription(*args)
    def SetModule(*args): return _sysarm.Node_SetModule(*args)
    def GetModule(*args): return _sysarm.Node_GetModule(*args)
    def write(*args): return _sysarm.Node_write(*args)
    __swig_destroy__ = _sysarm.delete_Node
    __del__ = lambda self : None;
Node_swigregister = _sysarm.Node_swigregister
Node_swigregister(Node)

class NodeSaxHandler(CommonSaxHandler):
    __swig_setmethods__ = {}
    for _s in [CommonSaxHandler]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, NodeSaxHandler, name, value)
    __swig_getmethods__ = {}
    for _s in [CommonSaxHandler]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, NodeSaxHandler, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _sysarm.new_NodeSaxHandler(*args)
        try: self.this.append(this)
        except: self.this = this
    def startElement(*args): return _sysarm.NodeSaxHandler_startElement(*args)
    def endElement(*args): return _sysarm.NodeSaxHandler_endElement(*args)
    def characters(*args): return _sysarm.NodeSaxHandler_characters(*args)
    def fatalError(*args): return _sysarm.NodeSaxHandler_fatalError(*args)
    __swig_setmethods__["DescriptionRus"] = _sysarm.NodeSaxHandler_DescriptionRus_set
    __swig_getmethods__["DescriptionRus"] = _sysarm.NodeSaxHandler_DescriptionRus_get
    if _newclass:DescriptionRus = _swig_property(_sysarm.NodeSaxHandler_DescriptionRus_get, _sysarm.NodeSaxHandler_DescriptionRus_set)
    __swig_setmethods__["DescriptionEng"] = _sysarm.NodeSaxHandler_DescriptionEng_set
    __swig_getmethods__["DescriptionEng"] = _sysarm.NodeSaxHandler_DescriptionEng_get
    if _newclass:DescriptionEng = _swig_property(_sysarm.NodeSaxHandler_DescriptionEng_get, _sysarm.NodeSaxHandler_DescriptionEng_set)
    __swig_destroy__ = _sysarm.delete_NodeSaxHandler
    __del__ = lambda self : None;
NodeSaxHandler_swigregister = _sysarm.NodeSaxHandler_swigregister
NodeSaxHandler_swigregister(NodeSaxHandler)

class ObjectSaxHandler(CommonSaxHandler):
    __swig_setmethods__ = {}
    for _s in [CommonSaxHandler]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, ObjectSaxHandler, name, value)
    __swig_getmethods__ = {}
    for _s in [CommonSaxHandler]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, ObjectSaxHandler, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _sysarm.new_ObjectSaxHandler(*args)
        try: self.this.append(this)
        except: self.this = this
    def startElement(*args): return _sysarm.ObjectSaxHandler_startElement(*args)
    def endElement(*args): return _sysarm.ObjectSaxHandler_endElement(*args)
    def characters(*args): return _sysarm.ObjectSaxHandler_characters(*args)
    def fatalError(*args): return _sysarm.ObjectSaxHandler_fatalError(*args)
    __swig_setmethods__["DescriptionRus"] = _sysarm.ObjectSaxHandler_DescriptionRus_set
    __swig_getmethods__["DescriptionRus"] = _sysarm.ObjectSaxHandler_DescriptionRus_get
    if _newclass:DescriptionRus = _swig_property(_sysarm.ObjectSaxHandler_DescriptionRus_get, _sysarm.ObjectSaxHandler_DescriptionRus_set)
    __swig_setmethods__["DescriptionEng"] = _sysarm.ObjectSaxHandler_DescriptionEng_set
    __swig_getmethods__["DescriptionEng"] = _sysarm.ObjectSaxHandler_DescriptionEng_get
    if _newclass:DescriptionEng = _swig_property(_sysarm.ObjectSaxHandler_DescriptionEng_get, _sysarm.ObjectSaxHandler_DescriptionEng_set)
    __swig_destroy__ = _sysarm.delete_ObjectSaxHandler
    __del__ = lambda self : None;
ObjectSaxHandler_swigregister = _sysarm.ObjectSaxHandler_swigregister
ObjectSaxHandler_swigregister(ObjectSaxHandler)

class OVP(BaseElement):
    __swig_setmethods__ = {}
    for _s in [BaseElement]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OVP, name, value)
    __swig_getmethods__ = {}
    for _s in [BaseElement]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OVP, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _sysarm.new_OVP(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["out"] = _sysarm.OVP_out_set
    __swig_getmethods__["out"] = _sysarm.OVP_out_get
    if _newclass:out = _swig_property(_sysarm.OVP_out_get, _sysarm.OVP_out_set)
    __swig_setmethods__["sys"] = _sysarm.OVP_sys_set
    __swig_getmethods__["sys"] = _sysarm.OVP_sys_get
    if _newclass:sys = _swig_property(_sysarm.OVP_sys_get, _sysarm.OVP_sys_set)
    __swig_setmethods__["par"] = _sysarm.OVP_par_set
    __swig_getmethods__["par"] = _sysarm.OVP_par_get
    if _newclass:par = _swig_property(_sysarm.OVP_par_get, _sysarm.OVP_par_set)
    __swig_setmethods__["vps"] = _sysarm.OVP_vps_set
    __swig_getmethods__["vps"] = _sysarm.OVP_vps_get
    if _newclass:vps = _swig_property(_sysarm.OVP_vps_get, _sysarm.OVP_vps_set)
    __swig_setmethods__["vpr"] = _sysarm.OVP_vpr_set
    __swig_getmethods__["vpr"] = _sysarm.OVP_vpr_get
    if _newclass:vpr = _swig_property(_sysarm.OVP_vpr_get, _sysarm.OVP_vpr_set)
    __swig_setmethods__["wrk"] = _sysarm.OVP_wrk_set
    __swig_getmethods__["wrk"] = _sysarm.OVP_wrk_get
    if _newclass:wrk = _swig_property(_sysarm.OVP_wrk_get, _sysarm.OVP_wrk_set)
    __swig_setmethods__["wrs"] = _sysarm.OVP_wrs_set
    __swig_getmethods__["wrs"] = _sysarm.OVP_wrs_get
    if _newclass:wrs = _swig_property(_sysarm.OVP_wrs_get, _sysarm.OVP_wrs_set)
    __swig_setmethods__["wrp"] = _sysarm.OVP_wrp_set
    __swig_getmethods__["wrp"] = _sysarm.OVP_wrp_get
    if _newclass:wrp = _swig_property(_sysarm.OVP_wrp_get, _sysarm.OVP_wrp_set)
    __swig_setmethods__["str"] = _sysarm.OVP_str_set
    __swig_getmethods__["str"] = _sysarm.OVP_str_get
    if _newclass:str = _swig_property(_sysarm.OVP_str_get, _sysarm.OVP_str_set)
    __swig_setmethods__["mod"] = _sysarm.OVP_mod_set
    __swig_getmethods__["mod"] = _sysarm.OVP_mod_get
    if _newclass:mod = _swig_property(_sysarm.OVP_mod_get, _sysarm.OVP_mod_set)
    __swig_setmethods__["WorkParameterTypes"] = _sysarm.OVP_WorkParameterTypes_set
    __swig_getmethods__["WorkParameterTypes"] = _sysarm.OVP_WorkParameterTypes_get
    if _newclass:WorkParameterTypes = _swig_property(_sysarm.OVP_WorkParameterTypes_get, _sysarm.OVP_WorkParameterTypes_set)
    __swig_setmethods__["WorkParameterNames"] = _sysarm.OVP_WorkParameterNames_set
    __swig_getmethods__["WorkParameterNames"] = _sysarm.OVP_WorkParameterNames_get
    if _newclass:WorkParameterNames = _swig_property(_sysarm.OVP_WorkParameterNames_get, _sysarm.OVP_WorkParameterNames_set)
    __swig_setmethods__["WorkRuDescription"] = _sysarm.OVP_WorkRuDescription_set
    __swig_getmethods__["WorkRuDescription"] = _sysarm.OVP_WorkRuDescription_get
    if _newclass:WorkRuDescription = _swig_property(_sysarm.OVP_WorkRuDescription_get, _sysarm.OVP_WorkRuDescription_set)
    __swig_setmethods__["WorkEnDescription"] = _sysarm.OVP_WorkEnDescription_set
    __swig_getmethods__["WorkEnDescription"] = _sysarm.OVP_WorkEnDescription_get
    if _newclass:WorkEnDescription = _swig_property(_sysarm.OVP_WorkEnDescription_get, _sysarm.OVP_WorkEnDescription_set)
    def SetOut(*args): return _sysarm.OVP_SetOut(*args)
    def SetPar(*args): return _sysarm.OVP_SetPar(*args)
    def SetSys(*args): return _sysarm.OVP_SetSys(*args)
    def GetOut(*args): return _sysarm.OVP_GetOut(*args)
    def GetPar(*args): return _sysarm.OVP_GetPar(*args)
    def GetSys(*args): return _sysarm.OVP_GetSys(*args)
    def GetType(*args): return _sysarm.OVP_GetType(*args)
    def write(*args): return _sysarm.OVP_write(*args)
    __swig_destroy__ = _sysarm.delete_OVP
    __del__ = lambda self : None;
OVP_swigregister = _sysarm.OVP_swigregister
OVP_swigregister(OVP)

class OVPSaxHandler(CommonSaxHandler):
    __swig_setmethods__ = {}
    for _s in [CommonSaxHandler]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, OVPSaxHandler, name, value)
    __swig_getmethods__ = {}
    for _s in [CommonSaxHandler]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, OVPSaxHandler, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _sysarm.new_OVPSaxHandler(*args)
        try: self.this.append(this)
        except: self.this = this
    def startElement(*args): return _sysarm.OVPSaxHandler_startElement(*args)
    def endElement(*args): return _sysarm.OVPSaxHandler_endElement(*args)
    def characters(*args): return _sysarm.OVPSaxHandler_characters(*args)
    def fatalError(*args): return _sysarm.OVPSaxHandler_fatalError(*args)
    __swig_setmethods__["DescriptionRus"] = _sysarm.OVPSaxHandler_DescriptionRus_set
    __swig_getmethods__["DescriptionRus"] = _sysarm.OVPSaxHandler_DescriptionRus_get
    if _newclass:DescriptionRus = _swig_property(_sysarm.OVPSaxHandler_DescriptionRus_get, _sysarm.OVPSaxHandler_DescriptionRus_set)
    __swig_setmethods__["DescriptionEng"] = _sysarm.OVPSaxHandler_DescriptionEng_set
    __swig_getmethods__["DescriptionEng"] = _sysarm.OVPSaxHandler_DescriptionEng_get
    if _newclass:DescriptionEng = _swig_property(_sysarm.OVPSaxHandler_DescriptionEng_get, _sysarm.OVPSaxHandler_DescriptionEng_set)
    __swig_destroy__ = _sysarm.delete_OVPSaxHandler
    __del__ = lambda self : None;
OVPSaxHandler_swigregister = _sysarm.OVPSaxHandler_swigregister
OVPSaxHandler_swigregister(OVPSaxHandler)

class Parameter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Parameter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Parameter, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _sysarm.new_Parameter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["FieldList"] = _sysarm.Parameter_FieldList_set
    __swig_getmethods__["FieldList"] = _sysarm.Parameter_FieldList_get
    if _newclass:FieldList = _swig_property(_sysarm.Parameter_FieldList_get, _sysarm.Parameter_FieldList_set)
    def SetName(*args): return _sysarm.Parameter_SetName(*args)
    def SetRuDescription(*args): return _sysarm.Parameter_SetRuDescription(*args)
    def SetEnDescription(*args): return _sysarm.Parameter_SetEnDescription(*args)
    def GetName(*args): return _sysarm.Parameter_GetName(*args)
    def GetRuDescription(*args): return _sysarm.Parameter_GetRuDescription(*args)
    def GetEnDescription(*args): return _sysarm.Parameter_GetEnDescription(*args)
    def SetModule(*args): return _sysarm.Parameter_SetModule(*args)
    def GetModule(*args): return _sysarm.Parameter_GetModule(*args)
    def write(*args): return _sysarm.Parameter_write(*args)
    __swig_destroy__ = _sysarm.delete_Parameter
    __del__ = lambda self : None;
Parameter_swigregister = _sysarm.Parameter_swigregister
Parameter_swigregister(Parameter)

class ParameterSaxHandler(CommonSaxHandler):
    __swig_setmethods__ = {}
    for _s in [CommonSaxHandler]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, ParameterSaxHandler, name, value)
    __swig_getmethods__ = {}
    for _s in [CommonSaxHandler]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, ParameterSaxHandler, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _sysarm.new_ParameterSaxHandler(*args)
        try: self.this.append(this)
        except: self.this = this
    def startElement(*args): return _sysarm.ParameterSaxHandler_startElement(*args)
    def endElement(*args): return _sysarm.ParameterSaxHandler_endElement(*args)
    def characters(*args): return _sysarm.ParameterSaxHandler_characters(*args)
    def fatalError(*args): return _sysarm.ParameterSaxHandler_fatalError(*args)
    __swig_setmethods__["DescriptionRus"] = _sysarm.ParameterSaxHandler_DescriptionRus_set
    __swig_getmethods__["DescriptionRus"] = _sysarm.ParameterSaxHandler_DescriptionRus_get
    if _newclass:DescriptionRus = _swig_property(_sysarm.ParameterSaxHandler_DescriptionRus_get, _sysarm.ParameterSaxHandler_DescriptionRus_set)
    __swig_setmethods__["DescriptionEng"] = _sysarm.ParameterSaxHandler_DescriptionEng_set
    __swig_getmethods__["DescriptionEng"] = _sysarm.ParameterSaxHandler_DescriptionEng_get
    if _newclass:DescriptionEng = _swig_property(_sysarm.ParameterSaxHandler_DescriptionEng_get, _sysarm.ParameterSaxHandler_DescriptionEng_set)
    __swig_destroy__ = _sysarm.delete_ParameterSaxHandler
    __del__ = lambda self : None;
ParameterSaxHandler_swigregister = _sysarm.ParameterSaxHandler_swigregister
ParameterSaxHandler_swigregister(ParameterSaxHandler)

class PythonObject(BaseElement):
    __swig_setmethods__ = {}
    for _s in [BaseElement]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, PythonObject, name, value)
    __swig_getmethods__ = {}
    for _s in [BaseElement]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, PythonObject, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _sysarm.new_PythonObject(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sysarm.delete_PythonObject
    __del__ = lambda self : None;
    __swig_setmethods__["FieldList"] = _sysarm.PythonObject_FieldList_set
    __swig_getmethods__["FieldList"] = _sysarm.PythonObject_FieldList_get
    if _newclass:FieldList = _swig_property(_sysarm.PythonObject_FieldList_get, _sysarm.PythonObject_FieldList_set)
    def GetType(*args): return _sysarm.PythonObject_GetType(*args)
    def write(*args): return _sysarm.PythonObject_write(*args)
PythonObject_swigregister = _sysarm.PythonObject_swigregister
PythonObject_swigregister(PythonObject)

SysarmType = _sysarm.SysarmType
ModuleType = _sysarm.ModuleType
ModelType = _sysarm.ModelType
OVPType = _sysarm.OVPType
ImageType = _sysarm.ImageType
NodeType = _sysarm.NodeType
ParameterType = _sysarm.ParameterType
ObjectType = _sysarm.ObjectType
class SaxHandler(CommonSaxHandler):
    __swig_setmethods__ = {}
    for _s in [CommonSaxHandler]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, SaxHandler, name, value)
    __swig_getmethods__ = {}
    for _s in [CommonSaxHandler]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, SaxHandler, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _sysarm.new_SaxHandler(*args)
        try: self.this.append(this)
        except: self.this = this
    def startElement(*args): return _sysarm.SaxHandler_startElement(*args)
    def endElement(*args): return _sysarm.SaxHandler_endElement(*args)
    def characters(*args): return _sysarm.SaxHandler_characters(*args)
    def fatalError(*args): return _sysarm.SaxHandler_fatalError(*args)
    __swig_setmethods__["DescriptionRus"] = _sysarm.SaxHandler_DescriptionRus_set
    __swig_getmethods__["DescriptionRus"] = _sysarm.SaxHandler_DescriptionRus_get
    if _newclass:DescriptionRus = _swig_property(_sysarm.SaxHandler_DescriptionRus_get, _sysarm.SaxHandler_DescriptionRus_set)
    __swig_setmethods__["DescriptionEng"] = _sysarm.SaxHandler_DescriptionEng_set
    __swig_getmethods__["DescriptionEng"] = _sysarm.SaxHandler_DescriptionEng_get
    if _newclass:DescriptionEng = _swig_property(_sysarm.SaxHandler_DescriptionEng_get, _sysarm.SaxHandler_DescriptionEng_set)
    __swig_setmethods__["SysarmDescriptionRus"] = _sysarm.SaxHandler_SysarmDescriptionRus_set
    __swig_getmethods__["SysarmDescriptionRus"] = _sysarm.SaxHandler_SysarmDescriptionRus_get
    if _newclass:SysarmDescriptionRus = _swig_property(_sysarm.SaxHandler_SysarmDescriptionRus_get, _sysarm.SaxHandler_SysarmDescriptionRus_set)
    __swig_setmethods__["SysarmDescriptionEng"] = _sysarm.SaxHandler_SysarmDescriptionEng_set
    __swig_getmethods__["SysarmDescriptionEng"] = _sysarm.SaxHandler_SysarmDescriptionEng_get
    if _newclass:SysarmDescriptionEng = _swig_property(_sysarm.SaxHandler_SysarmDescriptionEng_get, _sysarm.SaxHandler_SysarmDescriptionEng_set)
    __swig_setmethods__["ModuleName"] = _sysarm.SaxHandler_ModuleName_set
    __swig_getmethods__["ModuleName"] = _sysarm.SaxHandler_ModuleName_get
    if _newclass:ModuleName = _swig_property(_sysarm.SaxHandler_ModuleName_get, _sysarm.SaxHandler_ModuleName_set)
    __swig_destroy__ = _sysarm.delete_SaxHandler
    __del__ = lambda self : None;
SaxHandler_swigregister = _sysarm.SaxHandler_swigregister
SaxHandler_swigregister(SaxHandler)

class Sysarm(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Sysarm, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Sysarm, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _sysarm.new_Sysarm(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["Modules"] = _sysarm.Sysarm_Modules_set
    __swig_getmethods__["Modules"] = _sysarm.Sysarm_Modules_get
    if _newclass:Modules = _swig_property(_sysarm.Sysarm_Modules_get, _sysarm.Sysarm_Modules_set)
    def SetRuDescription(*args): return _sysarm.Sysarm_SetRuDescription(*args)
    def SetEnDescription(*args): return _sysarm.Sysarm_SetEnDescription(*args)
    def GetRuDescription(*args): return _sysarm.Sysarm_GetRuDescription(*args)
    def GetEnDescription(*args): return _sysarm.Sysarm_GetEnDescription(*args)
    def GetElement(*args): return _sysarm.Sysarm_GetElement(*args)
    def GetModule(*args): return _sysarm.Sysarm_GetModule(*args)
    __swig_destroy__ = _sysarm.delete_Sysarm
    __del__ = lambda self : None;
Sysarm_swigregister = _sysarm.Sysarm_swigregister
Sysarm_swigregister(Sysarm)

class SysarmReader(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SysarmReader, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SysarmReader, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _sysarm.new_SysarmReader(*args)
        try: self.this.append(this)
        except: self.this = this
    def Read(*args): return _sysarm.SysarmReader_Read(*args)
    def ReadModule(*args): return _sysarm.SysarmReader_ReadModule(*args)
    def ReadModel(*args): return _sysarm.SysarmReader_ReadModel(*args)
    def ReadOVP(*args): return _sysarm.SysarmReader_ReadOVP(*args)
    def ReadImage(*args): return _sysarm.SysarmReader_ReadImage(*args)
    def ReadNode(*args): return _sysarm.SysarmReader_ReadNode(*args)
    def ReadParameter(*args): return _sysarm.SysarmReader_ReadParameter(*args)
    def ReadObject(*args): return _sysarm.SysarmReader_ReadObject(*args)
    __swig_destroy__ = _sysarm.delete_SysarmReader
    __del__ = lambda self : None;
SysarmReader_swigregister = _sysarm.SysarmReader_swigregister
SysarmReader_swigregister(SysarmReader)

class XMLWriter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, XMLWriter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, XMLWriter, name)
    __repr__ = _swig_repr
    def Write(*args): return _sysarm.XMLWriter_Write(*args)
    def __init__(self, *args): 
        this = _sysarm.new_XMLWriter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sysarm.delete_XMLWriter
    __del__ = lambda self : None;
XMLWriter_swigregister = _sysarm.XMLWriter_swigregister
XMLWriter_swigregister(XMLWriter)

GetEnv = _sysarm.GetEnv
ExecCommand = _sysarm.ExecCommand


