# -*- coding: UTF-8 -*-
"""
All the things can override via Environment variables are keep in this one file.
"""
from os import environ
from collections import namedtuple, OrderedDict


DEFINED = OrderedDict([
            ('LINK_LOG_LEVEL', environ.get('LINK_LOG_LEVEL', 'INFO')),
            ('LINK_MAX_COUNT', int(environ.get('LINK_MAX_COUNT', 1000))),
            ('VLAB_URL', environ.get('VLAB_URL', 'https://localhost'))
          ])

Constants = namedtuple('Constants', list(DEFINED.keys()))

# The '*' expands the list, just liked passing a function *args
const = Constants(*list(DEFINED.values()))
