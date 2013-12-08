#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from functools import partial

from django.template.loader import BaseLoader
from django.template.loaders.app_directories import app_template_dirs
from django.conf import settings
from django import template as django_template

from mako.lookup import TemplateLookup
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


class FileSystemLoader(BaseLoader):
    is_usable = True

    def load_template_source(self, template_name, template_dirs=None):
        lookup = TemplateLookup(directories=settings.TEMPLATE_DIRS,
                                preprocessor=plim_preprocessor)
        return lookup.get_template(template_name), template_name

    def get_template_sources(self, template_name, template_dirs=None):
        yield


class AppDirectoriesLoader(BaseLoader):
    is_usable = True

    def load_template_source(self, template_name, template_dirs=None):
        lookup = TemplateLookup(directories=app_template_dirs,
                                preprocessor=plim_preprocessor)
        return lookup.get_template(template_name), template_name

    def get_template_sources(self, template_name, template_dirs=None):
        yield
