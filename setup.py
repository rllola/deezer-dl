#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='deezer-dl',
      version='0.1',
      description='Deezer music downloader',
      author='Lola',
      author_email='me@laflemme.lol',
      packages=['src'],
      package_dir={'src': 'src'},
      entry_points = {
            'console_scripts': ['deezer-dl=src.main:main'],
      },
     )