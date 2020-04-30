import setuptools  # important
from distutils.core import setup
from Cython.Build import cythonize
setup(ext_modules=cythonize("newexplorargsim2.pyx", build_dir="build"),

#setup(ext_modules=cythonize("newcagent.pyx", build_dir="build"),
                                           script_args=['build'], 
                                           options={'build':{'build_lib':'.'}})