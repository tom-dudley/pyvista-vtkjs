# pyvista-vtkjs
Pyvista with monekypatched vtkjs backend.

`pip install pyvista-vtkjs`

[Demo](https://tom-dudley.github.io/pyvista-vtkjs/lab/index.html?path=demo.ipynb)

# About
[PyVista](https://pyvista.org/) is a popular visualisation package for Python which leverages [VTK](https://vtk.org/). Since VTK is a C++ library, with no native WASM build, `PyVista` requires a server in order to run.

This package is an attempt to monkeypatch the VTK dependency in PyVista with [vkt.js](https://kitware.github.io/vtk-js/index.html) which is a reimplementation of VTK, suitable for Web.

# Install
`pip install pyvista-vtkjs`
or
`await micropip('pyvista-vtkjs')`

Note that this is intended for JupyterLite/Pyodide; installation and usage on standard Python is not expected to work (but it might!)


# Why?
The main motivation of this is to enable PyVista to run completely in the browser via [JupyterLite](https://jupyterlite.readthedocs.io/en/stable/) notebook, levearging [Pyodide](https://pyodide.org/en/stable/index.html). This enables PyVista notebooks to run completely client-side and be hosted on static sites such as GitHub Pages.

# How?
This package aims to take calls from PyVista intended for VTK, and forward them to vtk.js, effectively acting as a translation layer. In an ideal world KitWare would provide python bindings for vtk.js with exactly the same interface as VTK (or more likely a subset). If that were the case this package would be redundant.

# Current progress
This package currently implements approximately 0% of VTK, just enough to prove conceptually something could work.

## Partial implementations
- `CylinderSource`
- `Plotter`

# Current plan
- Try and recreate one of the [PyVista Examples](https://docs.pyvista.org/examples/), hosting it statically with full interactivity.

# Development
## Build
`python -m build --wheel`

You can point the install commands directly at the built `.whl` in JupyterLite/Pyodide. CORS might be a pain here.

