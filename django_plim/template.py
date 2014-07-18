#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from functools import partial

from django.conf import settings
from plim import preprocessor as plim_preprocessor
from mako.template import Template as MakoTemplate
from mako.lookup import TemplateLookup
from django.template.loaders import app_directories


lookup = TemplateLookup(directories=settings.TEMPLATE_DIRS)
Template = partial(MakoTemplate, lookup=lookup,
                   preprocessor=plim_preprocessor)


class Template(MakoTemplate):
    def render(self, context):
        context_dict = {}
        for d in context.dicts:
            context_dict.update(d)
        return super(Template, self).render(context_dict)


class Loader(app_directories.Loader):
    is_usable = True

    def load_template(self, template_name, template_dirs=None):
        source, origin = self.load_template_source(template_name, template_dirs)
        template = Template(source)
        return template, origin