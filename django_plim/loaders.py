#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from functools import partial

from django.template.loader import BaseLoader

from django.conf import settings
from mako.lookup import TemplateLookup
from django import template as django_template
from plim import preprocessor as plim_preprocessor
from mako.template import Template as MakoTemplate


def patch_django_template():
    django_template.Template = partial(MakoTemplate,
                                       preprocessor=plim_preprocessor)


def patch_mako_render():
    original_render = MakoTemplate.render

    def new_render(self, context):
        return original_render(self, **context)

    MakoTemplate.render = new_render

patch_django_template()
patch_mako_render()


class Loader(BaseLoader):
    is_usable = True

    def load_template_source(self, template_name, template_dirs=None):
        lookup = TemplateLookup(directories=settings.TEMPLATE_DIRS,
                                preprocessor=plim_preprocessor)
        return lookup.get_template('index.html'), 'index.html'

    def get_template_sources(self, template_name, template_dirs=None):
        pass
