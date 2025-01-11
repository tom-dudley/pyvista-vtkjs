from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call

setup(
    name='pyvista_vtkjs',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'webcolors',
    ],
    # cmdclass={
    #     'install': InstallPyVistaCommand,
    # },

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
