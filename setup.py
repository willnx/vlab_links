#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages


setup(name="vlab-links-api",
      author="Nicholas Willhite,",
      version='0.0.1',
      packages=find_packages(),
      include_package_data=True,
      description="Simplest URL shortner imaginable",
      install_requires=['flask', 'uwsgi', 'vlab-api-common', 'ujson']
      )
