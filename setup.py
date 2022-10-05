from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(
    name="pymathfun",
    ext_modules=cythonize([Extension(
    name="pymathfun",
    sources=["pymathfun.pyx"],
    libraries=["mathfun"],
    library_dirs=["."],
    runtime_library_dirs=["."]
)])
)