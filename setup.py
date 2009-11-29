#!/usr/bin/env python

from distutils.core import setup

from dreque_frontend import __version__ as version

dependencies = ["redis"]

setup(
    name = 'dreque_frontend',
    version = version,
    description = 'Django-based web frontend for the dreque project',
    author = 'Henrik Lied',
    author_email = 'henriklied@gmail.com',
    url = 'http://github.com/henriklied/dreque_frontend',
    packages = ['dreque_frontend'],
    requires = dependencies,
    install_requires = dependencies,
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)