import vtkPoints from '@kitware/vtk.js/Common/Core/Points';
import vtkPolyData from '@kitware/vtk.js/Common/DataModel/PolyData';
import CylinderSource from '@kitware/vtk.js/Filters/Sources/CylinderSource';

// Ensure the vtk object is properly initialized and namespace is preserved
export const Common = {
    Core: {
        vtkPoints: vtkPoints
    },
    DataModel: {
        vtkPolyData: vtkPolyData
    }
}

export const Filters = {
    Sources: {
        CylinderSource: CylinderSource
    }
}
export const vtk = {
    Common: Common,
    Filters: Filters
};

// Attach to the global context (Pyodide or browser environment)
if (typeof window !== "undefined") {
    window.vtk = vtk; // For browser environments
} else {
    globalThis.vtk = vtk; // For environments like Pyodide
}
