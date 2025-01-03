'''OpenGL extension NV.tessellation_program5

This module customises the behaviour of the 
OpenGL.raw.GL.NV.tessellation_program5 to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension, in conjunction with the ARB_tessellation_shader extension,
	introduces a new tessellation stage to the OpenGL primitive processing
	pipeline.  The ARB_tessellation_shader extension provides programmable
	shading functionality using the OpenGL Shading Language as its base; this
	extension provides assembly programmable shaders building on the family of
	assembly programmability extensions including ARB_vertex_program,
	ARB_fragment_program, NV_gpu_program4, and NV_geometry_program4.
	
	This extension adds a new basic primitive type, called a patch, which
	consists of an array of vertices plus some associated per-patch state.  It
	also adds two new assembly program types:  a tessellation control program
	that transforms a patch into a new patch and a tessellation evaluation
	program that computes the position and attributes of each vertex produced
	by the tesselator.
	
	When tessellation is active, it begins by running the optional
	tessellation control program, if enabled.  This program consumes a
	variable-size input patch and produces a new fixed-size output patch.  The
	output patch consists of an array of vertices, and a set of per-patch
	attributes.  The per-patch attributes include tessellation levels that
	control how finely the patch will be tessellated.  For each patch
	processed, multiple tessellation control program invocations are performed
	-- one per output patch vertex.  Each tessellation control program
	invocation writes all the attributes of its corresponding output patch
	vertex.  A tessellation control program may also read the per-vertex
	outputs of other tessellation control program invocations, as well as read
	and write shared per-patch outputs.  The tessellation control program
	invocations for a single patch effectively run as a group.  The GL
	automatically synchronizes threads to ensure that when executing a given
	instruction, all previous instructions have completed for all program
	invocations in the group.
	
	The tessellation primitive generator then decomposes a patch into a new
	set of primitives using the tessellation levels to determine how finely
	tessellated the output should be.  The primitive generator begins with
	either a triangle or a quad, and splits each outer edge of the primitive
	into a number of segments approximately equal to the corresponding element
	of the outer tessellation level array.  The interior of the primitive is
	tessellated according to elements of the inner tessellation level array.
	The primitive generator has three modes:  TRIANGLES and QUADS split a
	triangular or quad-shaped patch into a set of triangles that cover the
	original patch; ISOLINES_NV splits a quad-shaped patch into a set of line
	strips spanning the patch.  Each vertex generated by the tessellation
	primitive generator is assigned a (u,v) or (u,v,w) coordinate indicating
	its relative location in the subdivided triangle or quad.
	
	For each vertex produced by the tessellation primitive generator, the
	tessellation evaluation program is run to compute its position and other
	attributes of the vertex, using its (u,v) or (u,v,w) coordinate.  When
	computing the final vertex attributes, the tessellation evaluation program
	can also read the attributes of any of the vertices of the patch written
	by the tessellation control program.  Tessellation evaluation program
	invocations are completely independent, although all invocations for a
	single patch share the same collection of input vertices and per-patch
	attributes.
	
	The tessellator operates on vertices after they have been transformed by a
	vertex program or fixed-function vertex processing.  The primitives
	generated by the tessellator are passed further down the OpenGL pipeline,
	where they can be used as inputs to geometry programs, transform feedback,
	and the rasterizer.
	
	The tessellation control and evaluation programs are both optional.  If
	neither program type is present, the tessellation stage has no effect.  If
	no tessellation control program is present, the input patch provided by
	the application is passed directly to the tessellation primitive
	generator, and a set of fixed tessellation level parameters (specified via
	the PatchParameterfv function) is used to control primitive generation.
	If no tessellation evaluation program is present, the output patch
	produced by the tessellation control program is passed as a patch to
	subsequent pipeline stages, where it can be consumed by geometry programs,
	transform feedback, or the rasterizer.
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/tessellation_program5.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NV.tessellation_program5 import *
from OpenGL.raw.GL.NV.tessellation_program5 import _EXTENSION_NAME

def glInitTessellationProgram5NV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION