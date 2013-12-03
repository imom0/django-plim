#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.template.loader import BaseLoader

from django.conf import settings
from mako.lookup import TemplateLookup
from plim import preprocessor as plim_preprocessor


class Loader(BaseLoader):
    is_usable = True

    def load_template_source(self, template_name, template_dirs=None):
        lookup = TemplateLookup(directories=settings.TEMPLATE_DIRS,
                                preprocessor=plim_preprocessor)
        return lookup.get_template('index.html'), 'index.html'

    def get_template_sources(self, template_name, template_dirs=None):
        pass
