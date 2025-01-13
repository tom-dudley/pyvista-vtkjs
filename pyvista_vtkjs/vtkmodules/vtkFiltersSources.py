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

# TODO: This should persist to some background state in vtk.js rather than actually implementing functionality here. It should just proxy
class vtkCylinderSource():
    # _new_attr_exceptions = ['radius']
    # def __new__(cls, *args, **kwargs):
    #     print("Called new")
    #     instance = super().__new__(cls)
    #     print("Got instance")
    # #
    # #     print(instance.__dict__)
    # #
    # #     instance.radius = 0.5 
    # #
    #     print("Returning instance")
    #     return instance

    def __init__(self):
        print("Called init")
        self.radius = 10
        print("Set radius")

    #     self,
    #     center = (0.0, 0.0, 0.0),
    #     direction = (1.0, 0.0, 0.0),
    #     radius = 0.5,
    #     height = 1.0,
    #     capping = True,
    #     resolution = 100,
    # ) -> None:
    #     pass
    def SetHeight(self, x):
        self.height = x
    def SetRadius(self, x):
        self.radius = x
    def SetResolution(self, x):
        self.resolution = x
    def Update(self):
        pass
    def GetOutput(self):
        # c.getState() looks super handy and what we need
        # or c.toJSON()
        # d = c.getOutputData()
        # d.getClassName() gives 'vtkPolyData'
        # c = vtk.Filters.Sources.vtkCylinderSource.newInstance({ height: 2, radius: 1, resolution: 80 })

        # TODO: This should be a: vtkPolyData 
        # somehow..
        pass

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

