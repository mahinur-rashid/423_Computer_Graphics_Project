'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_SGIS_point_parameters'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_SGIS_point_parameters',error_checker=_errors._error_checker)
GL_DISTANCE_ATTENUATION_SGIS=_C('GL_DISTANCE_ATTENUATION_SGIS',0x8129)
GL_POINT_FADE_THRESHOLD_SIZE_SGIS=_C('GL_POINT_FADE_THRESHOLD_SIZE_SGIS',0x8128)
GL_POINT_SIZE_MAX_SGIS=_C('GL_POINT_SIZE_MAX_SGIS',0x8127)
GL_POINT_SIZE_MIN_SGIS=_C('GL_POINT_SIZE_MIN_SGIS',0x8126)
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat)
def glPointParameterfSGIS(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glPointParameterfvSGIS(pname,params):pass
