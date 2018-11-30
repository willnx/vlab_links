#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages


setup(name="vlab-link-api",
      author="Nicholas Willhite,",
      version='2018.11.30',
      packages=find_packages(),
      include_package_data=True,
      description="Simplest URL shortner imaginable",
      install_requires=['flask', 'uwsgi', 'vlab-api-common', 'ujson']
      )
