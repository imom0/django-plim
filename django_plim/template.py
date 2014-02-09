#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from functools import partial

from django.conf import settings
from django.template.loader import find_template_loader
from plim import preprocessor as plim_preprocessor
from mako.template import Template as MakoTemplate


def find_template_dirs():
    dirs = []
    for loader_name in settings.TEMPLATE_LOADERS:
        loader = find_template_loader(loader_name)
        if loader is not None:
            dirs.extend(loader.get_template_sources(''))
    return dirs

Template = partial(MakoTemplate, preprocessor=plim_preprocessor)
