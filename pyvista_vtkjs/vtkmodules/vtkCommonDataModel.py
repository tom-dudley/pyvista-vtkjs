VTK_EMPTY_CELL = 0
VTK_VERTEX = 1
VTK_POLY_VERTEX = 2
VTK_LINE = 3
VTK_POLY_LINE = 4
VTK_TRIANGLE = 5
VTK_TRIANGLE_STRIP = 6
VTK_POLYGON = 7
VTK_PIXEL = 8
VTK_QUAD = 9
VTK_TETRA = 10
VTK_VOXEL = 11
VTK_HEXAHEDRON = 12
VTK_WEDGE = 13
VTK_PYRAMID = 14
VTK_PENTAGONAL_PRISM = 15
VTK_HEXAGONAL_PRISM = 16
VTK_QUADRATIC_EDGE = 21
VTK_QUADRATIC_TRIANGLE = 22
VTK_QUADRATIC_QUAD = 23
VTK_QUADRATIC_POLYGON = 36
VTK_QUADRATIC_TETRA = 24
VTK_QUADRATIC_HEXAHEDRON = 25
VTK_QUADRATIC_WEDGE = 26
VTK_QUADRATIC_PYRAMID = 27
VTK_BIQUADRATIC_QUAD = 28
VTK_TRIQUADRATIC_HEXAHEDRON = 29
VTK_QUADRATIC_LINEAR_QUAD = 30
VTK_QUADRATIC_LINEAR_WEDGE = 31
VTK_BIQUADRATIC_QUADRATIC_WEDGE = 32
VTK_BIQUADRATIC_QUADRATIC_HEXAHEDRON = 33
VTK_BIQUADRATIC_TRIANGLE = 34
VTK_CUBIC_LINE = 35
VTK_CONVEX_POINT_SET = 41
VTK_POLYHEDRON = 42
VTK_PARAMETRIC_CURVE = 51
VTK_PARAMETRIC_SURFACE = 52
VTK_PARAMETRIC_TRI_SURFACE = 53
VTK_PARAMETRIC_QUAD_SURFACE = 54
VTK_PARAMETRIC_TETRA_REGION = 55
VTK_PARAMETRIC_HEX_REGION = 56
VTK_HIGHER_ORDER_EDGE = 60
VTK_HIGHER_ORDER_TRIANGLE = 61
VTK_HIGHER_ORDER_QUAD = 62
VTK_HIGHER_ORDER_POLYGON = 63
VTK_HIGHER_ORDER_TETRAHEDRON = 64
VTK_HIGHER_ORDER_WEDGE = 65
VTK_HIGHER_ORDER_PYRAMID = 66
VTK_HIGHER_ORDER_HEXAHEDRON = 67
VTK_LAGRANGE_CURVE = 68
VTK_LAGRANGE_TRIANGLE = 69
VTK_LAGRANGE_QUADRILATERAL = 70
VTK_LAGRANGE_TETRAHEDRON = 71
VTK_LAGRANGE_HEXAHEDRON = 72
VTK_LAGRANGE_WEDGE = 73
VTK_LAGRANGE_PYRAMID = 74
VTK_BEZIER_CURVE = 75
VTK_BEZIER_TRIANGLE = 76
VTK_BEZIER_QUADRILATERAL = 77
VTK_BEZIER_TETRAHEDRON = 78
VTK_BEZIER_HEXAHEDRON = 79
VTK_BEZIER_WEDGE = 80
VTK_BEZIER_PYRAMID = 10000 # TODO
VTK_TRIQUADRATIC_PYRAMID = 10001 # TODO
VTK_NUMBER_OF_CELL_TYPES = 75 # TODO: This was extracted from the pyvista codebase but doesn't seem to match

class vtkAbstractCellLocator:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkAbstractCellLocator' is not implemented yet")

class vtkBiQuadraticQuad:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkBiQuadraticQuad' is not implemented yet")

class vtkBiQuadraticQuadraticHexahedron:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkBiQuadraticQuadraticHexahedron' is not implemented yet")

class vtkBiQuadraticQuadraticWedge:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkBiQuadraticQuadraticWedge' is not implemented yet")

class vtkBiQuadraticTriangle:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkBiQuadraticTriangle' is not implemented yet")

class vtkCell:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkCell' is not implemented yet")

class vtkCellArray:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkCellArray' is not implemented yet")

class vtkCellLocator:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkCellLocator' is not implemented yet")

class vtkCellTreeLocator:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkCellTreeLocator' is not implemented yet")

class vtkColor3ub:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkColor3ub' is not implemented yet")

class vtkCompositeDataSet:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkCompositeDataSet' is not implemented yet")

class vtkConvexPointSet:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkConvexPointSet' is not implemented yet")

class vtkCubicLine:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkCubicLine' is not implemented yet")

class vtkDataObject:
    FIELD_ASSOCIATION_POINTS = 0
    FIELD_ASSOCIATION_CELLS = 1
    FIELD_ASSOCIATION_NONE = 2
    FIELD_ASSOCIATION_ROWS = 3
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkDataObject' is not implemented yet")

class vtkDataSet:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkDataSet' is not implemented yet")

class vtkDataSetAttributes:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkDataSetAttributes' is not implemented yet")

class vtkEmptyCell:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkEmptyCell' is not implemented yet")

class vtkExplicitStructuredGrid:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkExplicitStructuredGrid' is not implemented yet")

class vtkFieldData:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkFieldData' is not implemented yet")

class vtkGenericCell:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkGenericCell' is not implemented yet")

class vtkHexagonalPrism:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkHexagonalPrism' is not implemented yet")

class vtkHexahedron:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkHexahedron' is not implemented yet")

class vtkImageData:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkImageData' is not implemented yet")

class vtkImplicitFunction:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkImplicitFunction' is not implemented yet")

class vtkIterativeClosestPointTransform:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkIterativeClosestPointTransform' is not implemented yet")

class vtkLine:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkLine' is not implemented yet")

class vtkMultiBlockDataSet:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkMultiBlockDataSet' is not implemented yet")

class vtkNonMergingPointLocator:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkNonMergingPointLocator' is not implemented yet")

class vtkPartitionedDataSet:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkPartitionedDataSet' is not implemented yet")

class vtkPentagonalPrism:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkPentagonalPrism' is not implemented yet")

class vtkPerlinNoise:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkPerlinNoise' is not implemented yet")

class vtkPiecewiseFunction:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkPiecewiseFunction' is not implemented yet")

class vtkPixel:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkPixel' is not implemented yet")

class vtkPlane:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkPlane' is not implemented yet")

class vtkPlaneCollection:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkPlaneCollection' is not implemented yet")

class vtkPlanes:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkPlanes' is not implemented yet")

class vtkPointLocator:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkPointLocator' is not implemented yet")

class vtkPointSet:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkPointSet' is not implemented yet")

class vtkPolyData:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkPolyData' is not implemented yet")

class vtkPolyLine:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkPolyLine' is not implemented yet")

class vtkPolyPlane:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkPolyPlane' is not implemented yet")

class vtkPolyVertex:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkPolyVertex' is not implemented yet")

class vtkPolygon:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkPolygon' is not implemented yet")

class vtkPolyhedron:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkPolyhedron' is not implemented yet")

class vtkPyramid:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkPyramid' is not implemented yet")

class vtkQuad:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkQuad' is not implemented yet")

class vtkQuadraticEdge:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkQuadraticEdge' is not implemented yet")

class vtkQuadraticHexahedron:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkQuadraticHexahedron' is not implemented yet")

class vtkQuadraticLinearQuad:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkQuadraticLinearQuad' is not implemented yet")

class vtkQuadraticLinearWedge:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkQuadraticLinearWedge' is not implemented yet")

class vtkQuadraticPolygon:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkQuadraticPolygon' is not implemented yet")

class vtkQuadraticPyramid:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkQuadraticPyramid' is not implemented yet")

class vtkQuadraticQuad:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkQuadraticQuad' is not implemented yet")

class vtkQuadraticTetra:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkQuadraticTetra' is not implemented yet")

class vtkQuadraticTriangle:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkQuadraticTriangle' is not implemented yet")

class vtkQuadraticWedge:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkQuadraticWedge' is not implemented yet")

class vtkRectf:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkRectf' is not implemented yet")

class vtkRectilinearGrid:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkRectilinearGrid' is not implemented yet")

class vtkSelection:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkSelection' is not implemented yet")

class vtkSelectionNode:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkSelectionNode' is not implemented yet")

class vtkStaticCellLocator:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkStaticCellLocator' is not implemented yet")

class vtkStaticPointLocator:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkStaticPointLocator' is not implemented yet")

class vtkStructuredGrid:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkStructuredGrid' is not implemented yet")

class vtkStructuredPoints:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkStructuredPoints' is not implemented yet")

class vtkTable:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkTable' is not implemented yet")

class vtkTetra:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkTetra' is not implemented yet")

class vtkTriQuadraticHexahedron:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkTriQuadraticHexahedron' is not implemented yet")

class vtkTriQuadraticPyramid:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkTriQuadraticPyramid' is not implemented yet")

class vtkTriangle:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkTriangle' is not implemented yet")

class vtkTriangleStrip:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkTriangleStrip' is not implemented yet")

class vtkUnstructuredGrid:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkUnstructuredGrid' is not implemented yet")

class vtkVertex:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkVertex' is not implemented yet")

class vtkVoxel:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkVoxel' is not implemented yet")

class vtkWedge:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'vtkWedge' is not implemented yet")

