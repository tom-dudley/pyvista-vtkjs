import js
from vtkmodules.vtkCommonDataModel import vtkDataObject, vtkPolyData
from pyvista_vtkjs.logger import logger

class vtkAxes:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkAxes' is not implemented yet")

class vtkBooleanOperationPolyDataFilter:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkBooleanOperationPolyDataFilter' is not implemented yet")

class vtkBoxClipDataSet:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkBoxClipDataSet' is not implemented yet")

class vtkCellTreeLocator:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkCellTreeLocator' is not implemented yet")

class vtkClipClosedSurface:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkClipClosedSurface' is not implemented yet")

class vtkContourTriangulator:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkContourTriangulator' is not implemented yet")

class vtkCursor3D:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkCursor3D' is not implemented yet")

class vtkCurvatures:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkCurvatures' is not implemented yet")

class vtkDataSetTriangleFilter:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkDataSetTriangleFilter' is not implemented yet")

class vtkGradientFilter:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkGradientFilter' is not implemented yet")

class vtkIntersectionPolyDataFilter:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkIntersectionPolyDataFilter' is not implemented yet")

class vtkOBBTree:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkOBBTree' is not implemented yet")

class vtkRectilinearGridToPointSet:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkRectilinearGridToPointSet' is not implemented yet")

class vtkRectilinearGridToTetrahedra:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkRectilinearGridToTetrahedra' is not implemented yet")

class vtkRemovePolyData:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkRemovePolyData' is not implemented yet")

class vtkShrinkFilter:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkShrinkFilter' is not implemented yet")

class vtkTableBasedClipDataSet:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkTableBasedClipDataSet' is not implemented yet")

class vtkTableToPolyData:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkTableToPolyData' is not implemented yet")

class vtkTessellatorFilter:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkTessellatorFilter' is not implemented yet")

# TODO
class vtkTransformFilter:
    def __init__(self):
        logger.debug(f"vtkTransformFilter: __init__")
        self.obj = js.vtk.Common.Transform.vtkTransform.newInstance()
        pass
    def SetInputDataObject(self, i):
        # This is type: pyvista.core.pointset.PolyData for CylinderSource
        logger.debug(f"vtkTransformFilter: SetInputDataObject: {type(i)}")
        self.input = i
    def SetTransform(self, t):
        logger.debug(f"vtkTransformFilter: SetTransform: {t}")
        pass
    def SetTransformAllInputVectors(self, transform_all_input_vectors):
        logger.debug(f"vtkTransformFilter: SetTransformAllInputVectors: {transform_all_input_vectors}")
        pass
    def Update(self):
        logger.debug(f"vtkTransformFilter: Update")
        pass
    # TODO
    # These two are inherited from vtkAlgorithm, returning something which inherits from vtkDataObject
    def GetInputDataObject(self, iport, iconnection):
        logger.debug(f"vtkTransformFilter: GetInputDataObject: {iport}, {iconnection}")
        return self.input
    def GetOutputDataObject(self, oport):
        logger.debug(f"vtkTransformFilter: GetOutputDataObject: {oport}")
        return self.input 

class vtkWarpScalar:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkWarpScalar' is not implemented yet")

class vtkWarpVector:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkWarpVector' is not implemented yet")

