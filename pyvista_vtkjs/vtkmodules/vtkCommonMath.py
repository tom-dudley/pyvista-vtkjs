class vtkMatrix3x3:
    def __init__(self):
        raise NotImplementedError(f"'vtkMatrix3x3' is not implemented yet")

# TODO
class vtkMatrix4x4:
    def __init__(self):
        # TODO: What should back this??
        # Maybe vtkMatrixBuilder??
        # This class might just get passed into vtkTransform.SetMatrix
        pass
    def SetElement(self, i, j, val):
        pass
    def GetElement(self, i, j):
        # TODO
        return 1



