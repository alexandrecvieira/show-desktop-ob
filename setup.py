#!/usr/bin/env python3

from distutils.core import setup
import glob
import os
from DistUtilsExtra.command import *

setup(name='show-desktop-ob',
      version='0.1.0',
      description='Show Desktop icon on alt-tab',
      author='Alexandre C Vieira',
      author_email='acamargo.vieira@gmail.com',
      url='https://github.com/acamargovieira/show-desktop-ob',
      scripts=[
          'show-desktop-ob',
      ],
      cmdclass={"build": build_extra.build_extra,
                "build_i18n": build_i18n.build_i18n},
      )
