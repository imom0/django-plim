#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from functools import partial

from plim import preprocessor as plim_preprocessor
from mako.template import Template as MakoTemplate
from django.template.loaders import app_directories


class Template(MakoTemplate):
    def render(self, context):
        context_dict = {}
        for d in context.dicts:
            context_dict.update(d)
        return super(Template, self).render(**context_dict)


class Loader(app_directories.Loader):
    is_usable = True

    def load_template(self, template_name, template_dirs=None):
        source, origin = self.load_template_source(template_name, template_dirs)
        template = PlimTemplate(source)
        return template, origin


PlimTemplate = partial(MakoTemplate,
                       preprocessor=plim_preprocessor)
