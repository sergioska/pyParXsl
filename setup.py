#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
  name="pyParXsl",
  version="*",
  description="Toolkit for python parser applications xslt transformation language based",
  author="Sergio Sicari",
  author_email="sergiosicari@gmail.com",
  url="http://github.com/sergioska/pyParXsl/tree/master",
  download_url="http://github.com/sergioska/PyParXsl/tree/master",
  zip_safe = False, # we include templates and tests
  )
