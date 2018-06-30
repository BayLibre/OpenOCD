#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='OpenOCD',
    packages=find_packages(),
    author='screwer',
    author_email='screwer@gmail.com',
    description='This library allows to control OpenOCD debug server via it\'s telnet connection port.',
    long_description=open('README.md').read(),
    url='https://github.com/BayLibre/OpenOCD', 
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: WTFPL",
        "Natural Language :: English",
        "Operating System :: GNU/Linux",
        "Programming Language :: Python :: 3.6",
    ],
)
