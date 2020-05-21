'''This script is used to cythonize the scripts: it generates compiled .pyd files from the uncompiled, cythonized .pyx scripts'''
import setuptools  # important
from distutils.core import setup
from Cython.Build import cythonize
setup(ext_modules=cythonize("newexplorargsim2.pyx", build_dir="build"),
                                           script_args=['build'], 
                                           options={'build':{'build_lib':'.'}})
                                           
#Change the name of the .pyx file to cythonize different files.                                   