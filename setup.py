#!/usr/bin/env python
#
# Setup prog for plugins-management
#
#


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import time

current_time = time.gmtime()
release_version = "{0}.{1:0>2}.{2:0>2}".format(current_time.tm_year, current_time.tm_mon, current_time.tm_mday)

# setup for distutils
setup(
    name="pluginmanager",
    version=release_version,
    description='plugin-manager package',
    long_description='''This package contains the plugins management''',
    license='GPL',
    author='Jose Caballero',
    author_email='jcaballero@bnl.gov',
    maintainer='Jose Caballero',
    maintainer_email='jcaballero@bnl.gov',
    url='https://github.com/bnl-sdcc/plugin-manager',
    py_modules=['pluginmanager', ],
    scripts=[],
    data_files=[]
)
