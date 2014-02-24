#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from functools import partial

from django.conf import settings
from plim import preprocessor as plim_preprocessor
from mako.template import Template as MakoTemplate
from mako.lookup import TemplateLookup


lookup = TemplateLookup(directories=settings.TEMPLATE_DIRS)
Template = partial(MakoTemplate, lookup=lookup,
                   preprocessor=plim_preprocessor)
