import os
import sys
import importlib.abc
import importlib.machinery
import importlib.util

sys.path.append('/lib/python3.12/site-packages/pyvista_vtkjs')
import vtkmodules
sys.path = sys.path[:-1]

sys.path.append('/lib/python3.12/site-packages/pyvista_vtkjs/pyvista')
import pyvista
sys.path = sys.path[:-1]


from pyvista import *

# # TODO: There might be some masked classes we need to clean up now?
# from pyvista.numpy_interface import *

CylinderSource._new_attr_exceptions.extend(['obj', 'radius', 'height', 'resolution', 'capping'])
print(CylinderSource._new_attr_exceptions)


# from .cylinder_source import CylinderSource
from .plotter import Plotter

# This will only work in pyodide..
import js

vtk_src_path = '/lib/python3.12/site-packages/pyvista_vtkjs/vtk-core-bundle.js'
with open(vtk_src_path, 'r') as f:
    vtk_src = f.read()

vtk_proxy = js.eval(vtk_src)


