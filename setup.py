# -*- coding: utf-8 -*-
"""
    chard setup script

    blah blah blah

    :copyright: uniphil 2013
    :license: dwtfyw. and i like coffee.
"""

from setuptools import setup


with open('readme.md') as readme:
    setup(
        name='chard',
        version='0',
        author='Phil Schleihauf',
        author_email='uniphil@gmail.com',
        url='https://github.com/uniphil/chard',
        license='blah blah blah',
        description='MongoDB Introspection-ish. ...',
        long_description=readme.read(),
        install_requires=['pymongo'],
        py_modules=['chard'],
    )
