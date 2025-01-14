import js
from vtkmodules.vtkCommonDataModel import vtkPolyData

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

class vtkCylinderSource():
    def __init__(self):
        # Does this need to be torn down / destroyed? Check docs
        self.obj = js.vtk.Filters.Sources.CylinderSource.newInstance()
        # We could also use/store:
        # csi.toJSON().to_py()
        # We could 'walk' this structure looking for vtkClass
    def SetHeight(self, x):
        self.obj.setHeight(x)
    def SetRadius(self, x):
        self.obj.setRadius(x)
    def SetResolution(self, x):
        self.obj.setResolution(x)
    def Update(self):
        self.obj.update()
    def GetOutput(self):
        # c.getState() looks super handy and what we need
        # or c.toJSON()
        # d = c.getOutputData()
        # d.getClassName() gives 'vtkPolyData'
        # c = vtk.Filters.Sources.vtkCylinderSource.newInstance({ height: 2, radius: 1, resolution: 80 })

        # TODO: This should be a: vtkPolyData 
        # somehow..

        # polyData = js.vtk.vtk.Common.DataModel.vtkPolyData
        # d = polyData.newInstance()
        # print(d.getBounds())

        # output will be 'vtkPolyData' here
        output = self.obj.getOutputData() 
        polydata = vtkPolyData()
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

