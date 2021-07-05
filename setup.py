#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='deezer-dl',
      version='0.2',
      description='Deezer music downloader',
      author='Lola',
      author_email='me@laflemme.lol',
      packages=['deezerdl', 'deezer'],
      package_dir={'deezerdl': 'deezerdl', 'deezer': 'deezerdl/deezer'},
      entry_points = {
            'console_scripts': ['deezer-dl=deezerdl.main:main'],
      },
     )