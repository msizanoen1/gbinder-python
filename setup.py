import pkgconfig
from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

gbinder = Extension('gbinder', sources=['gbinder.pyx'])
pkgconfig.configure_extension(gbinder, 'libgbinder')

extensions = cythonize(gbinder, compiler_directives={'language_level': "3"})

setup(
    name="gbinder-python",
    description="""Cython extension module for C++ gbinder functions""",
    version="1.0.0",
    author="Erfan Abdi",
    author_email="erfangplus@gmail.com",
    url="https://github.com/erfanoabdi/gbinder-python",
    license="GPL3",
    ext_modules=extensions
)
