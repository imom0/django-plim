#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.template.loader import BaseLoader


class Loader(BaseLoader):
    is_usable = True

    def load_template_source(self, template_name, template_dirs=None):
        pass

    def get_template_sources(self, template_name, template_dirs=None):
        pass
