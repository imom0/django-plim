#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from functools import partial

from plim import preprocessor as plim_preprocessor
from mako.template import Template as MakoTemplate

Template = partial(MakoTemplate, preprocessor=plim_preprocessor)
