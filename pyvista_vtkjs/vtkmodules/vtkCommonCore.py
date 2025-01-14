import js

VTK_ARIAL = 0
VTK_COURIER = 1
VTK_TIMES = 2
VTK_FONT_FILE = 1 # TODO: What is this value
VTK_UNSIGNED_CHAR = 3

# TODO: This looks fun..
class buffer_shared:
    def __init__(self):
        pass

class mutable:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'mutable' is not implemented yet")

class reference:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'reference' is not implemented yet")

class vtkAbstractArray:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkAbstractArray' is not implemented yet")

class vtkBitArray:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkBitArray' is not implemented yet")

class vtkCharArray:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkCharArray' is not implemented yet")

class vtkCommand:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkCommand' is not implemented yet")

# TODO
class vtkDataArray:
    def __init__(self):
        pass
    def CreateDataArray(vtk_arr_type):
        return vtkDataArray()
    def SetNumberOfComponents(self, n):
        pass
    def SetNumberOfTuples(self, n):
        pass
    def SetVoidArray(self, a, b, c):
        pass

class vtkDoubleArray:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkDoubleArray' is not implemented yet")

class vtkFileOutputWindow:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkFileOutputWindow' is not implemented yet")

class vtkFloatArray:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkFloatArray' is not implemented yet")

class vtkIdList:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkIdList' is not implemented yet")

# TODO
class vtkIdTypeArray:
    def __init__(self):
        # Example attribute
        self.data_type_size = 4  # Mock value for data type size

    def GetDataTypeSize(self):
        # Return a mocked data type size
        return self.data_type_size

class vtkLogger:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkLogger' is not implemented yet")

class vtkLookupTable:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkLookupTable' is not implemented yet")

class vtkMath:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkMath' is not implemented yet")

class vtkOutputWindow:
    def __init__(self, *args, **kwargs):
        # This doesn't appear to be used in the pyvista codebase
        # It might be a good place to log to console if it does get used though
        # raise NotImplementedError(f"'vtkStringOutputWindow' is not implemented yet")
        self.instance = None
    def SetInstance(self, instance):
        # TODO: 'instance' might be from variable 'error_output' so perhaps we console.log it? Or print it?
        self.instance = instance

# TODO
class vtkPoints:
    def __init__(self):
        self.obj = js.vtk.Common.Core.vtkPoints.newInstance()
    def SetData(self, data):
        pass
    def GetData(self):
        # TODO
        # This is a nested list of ints, eg rows of a matrix I imagine
        return []

class vtkSignedCharArray:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkSignedCharArray' is not implemented yet")

class vtkStringArray:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkStringArray' is not implemented yet")

class vtkStringOutputWindow:
        # This doesn't appear to be used in the pyvista codebase
        # It might be a good place to log to console if it does get used though
        # raise NotImplementedError(f"'vtkStringOutputWindow' is not implemented yet")
    def __init__(self):
        self.observers = []
    
    def AddObserver(self, event, callback):
        # Mock behavior of AddObserver
        print(f"AddObserver called with event: {event} and callback: {callback}")
        self.observers.append((event, callback))

class vtkTypeInt32Array:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkTypeInt32Array' is not implemented yet")

class vtkTypeInt64Array:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkTypeInt64Array' is not implemented yet")

class vtkTypeUInt32Array:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkTypeUInt32Array' is not implemented yet")

class vtkUnsignedCharArray:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkUnsignedCharArray' is not implemented yet")

class vtkVersion:
    major = 9
    @staticmethod
    def GetVTKMajorVersion():
        return 9

    @staticmethod
    def GetVTKMinorVersion():
        return 4

    @staticmethod
    def GetVTKBuildVersion():
        return 1

# TODO
class vtkWeakReference:
    def __init__(self):
        self._reference = None

    def Set(self, obj):
        # Store the reference to the actual object
        self._reference = obj
    
    def Get(self):
        # Return the actual referenced object
        return self._reference
