import js
from vtkmodules.vtkCommonDataModel import vtkPolyData
from pyvista_vtkjs.logger import logger

class vtkArcSource:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkArcSource' is not implemented yet")

class vtkArrowSource:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkArrowSource' is not implemented yet")

class vtkCapsuleSource:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkCapsuleSource' is not implemented yet")

class vtkConeSource:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkConeSource' is not implemented yet")

class vtkCubeSource:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkCubeSource' is not implemented yet")

# TODO: Ideally we'd define/generate this off the back of the vtkFiltersSources.pyi file which defines these definitions
class vtkCylinderSource():
    def __init__(self):
        logger.debug("vtkCylinderSource: __init__")
        # Does this need to be torn down / destroyed? Check docs
        self.obj = js.vtk.Filters.Sources.CylinderSource.newInstance()
        # We could also use/store:
        # csi.toJSON().to_py()
        # We could 'walk' this structure looking for vtkClass
    def GetHeight(self):
        logger.debug(f"vtkCylinderSource: GetHeight")
        return self.obj.getHeight()
    def SetHeight(self, x):
        logger.debug(f"vtkCylinderSource: SetHeight: {x}")
        self.obj.setHeight(x)
    def GetRadius(self):
        logger.debug(f"vtkCylinderSource: GetRadius")
        return self.obj.getRadius()
    def SetRadius(self, x):
        logger.debug(f"vtkCylinderSource: SetRadius: {x}")
        self.obj.setRadius(x)
    def GetResolution(self):
        logger.debug(f"vtkCylinderSource: GetResolution")
        return self.obj.getResolution()
    def SetResolution(self, x):
        logger.debug(f"vtkCylinderSource: SetResolution: {x}")
        self.obj.setResolution(x)
    def GetCapping(self):
        logger.debug(f"vtkCylinderSource: GetCapping")
        return self.obj.getCapping()
    def SetCapping(self, x):
        logger.debug(f"vtkCylinderSource: SetCapping: {x}")
        self.obj.setCapping(x)
    def GetCapsuleCap(self):
        logger.debug(f"vtkCylinderSource: GetCapsuleCap")
        return self.obj.getCapsuleCap()
    def SetCapsuleCap(self, x):
        logger.debug(f"vtkCylinderSource: SetCapsuleCap: {x}")
        self.obj.setCapsuleCap(x)
    def Update(self):
        logger.debug(f"vtkCylinderSource: Update")
        self.obj.update()
    def GetOutput(self):
        logger.debug(f"vtkCylinderSource: GetOutput")
        # c.getState() looks super handy and what we need
        # or c.toJSON()
        # d = c.getOutputData()
        # d.getClassName() gives 'vtkPolyData'
        # c = vtk.Filters.Sources.vtkCylinderSource.newInstance({ height: 2, radius: 1, resolution: 80 })

        # d = polyData.newInstance()
        # print(d.getBounds())

        # returns a JS vtkPolyData
        output = self.obj.getOutputData() 
        # creates a Python vtkPolyData
        polydata = vtkPolyData(output)
        return polydata

class vtkDiskSource:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkDiskSource' is not implemented yet")

class vtkFrustumSource:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkFrustumSource' is not implemented yet")

class vtkLineSource:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkLineSource' is not implemented yet")

class vtkOutlineCornerFilter:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkOutlineCornerFilter' is not implemented yet")

class vtkOutlineCornerSource:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkOutlineCornerSource' is not implemented yet")

class vtkParametricFunctionSource:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkParametricFunctionSource' is not implemented yet")

class vtkPlaneSource:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkPlaneSource' is not implemented yet")

class vtkPlatonicSolidSource:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkPlatonicSolidSource' is not implemented yet")

class vtkPointSource:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkPointSource' is not implemented yet")

class vtkRegularPolygonSource:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkRegularPolygonSource' is not implemented yet")

class vtkSphereSource:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkSphereSource' is not implemented yet")

class vtkSuperquadricSource:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkSuperquadricSource' is not implemented yet")

class vtkTessellatedBoxSource:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkTessellatedBoxSource' is not implemented yet")

