# -*- coding: utf-8 -*-
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, '.')
from MyNewPythonService import __version__


setup(
    name="MyNewPythonService",
    version=__version__,
    description="Flask based microservice.",
    maintainer="",
    packages=["MyNewPythonService", "MyNewPythonService.mynewmicroservice"],
    platforms=["any"]
)
