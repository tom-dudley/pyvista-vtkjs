# from .install import install
# install()

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

# from .cylinder_source import CylinderSource
from .plotter import Plotter


