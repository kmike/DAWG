#! /usr/bin/env python
import glob
from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    name="DAWG",
    version="0.7.8",
    description="Fast and memory efficient DAWG (DAFSA) for Python",
    long_description = open('README.rst').read() +'\n\n' + open('CHANGES.rst').read(),
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',
    url='https://github.com/pytries/DAWG/',

    ext_modules = cythonize(
        Extension(
            "dawg",
            glob.glob('src/dawg.pyx') + glob.glob('lib/b64/*.c'),
            include_dirs=['lib'],
            language = "c++",
        )
    ),

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Linguistic',
    ],
)
