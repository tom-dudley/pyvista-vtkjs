import time
import asyncio
import micropip
from pyodide.webloop import PyodideTask

import js

p ='https://python.tomdudley.io/pyvista_vtkjs-0.0.1-py3-none-any.whl'

def done():
    print("Done!")
    js.console.log("Done!")

# micropip.install(p).then(done)

# let pyodide = await loadPyodide({packages:['https://python.tomdudley.io/pyvista_vtkjs-0.0.1-py3-none-any.whl', 'micropip']});
# await pyodide.runPython(`
# import pyvista_vtkjs
# import pyvista
# print("Version: " + str(pyvista.__version__))`);

def pip_install(package, deps=True):
    loop = asyncio.get_event_loop()
    i = micropip.install(package, deps=deps, verbose=True)
    result = loop.run_until_complete(i)
    print(type(i))
    print(type(result))
    t = PyodideTask(i)
    print(type(t))
    t.then(done)

# def install_pyvista_no_deps():
#     pip_install("pyvista", deps=False)
#     pip_install("numpy")

def install():
    # TODO: Dynamically lookup the version to mock
    micropip.add_mock_package("vtk", "9.3.1")
    micropip.add_mock_package("vtkmodules", "9.3.1")
    # install_pyvista_no_deps()  # Install PyVista without vtk
    pip_install("pyvista")
    # TODO: Wait until pyvista is importable
    time.sleep(45)

if __name__ == "__main__":
    install()
