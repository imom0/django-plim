#!/usr/bin/venv python
# -*- coding: UTF-8 -*-

from django.http import HttpResponse
from django.conf import settings
from mako.lookup import TemplateLookup
from plim import preprocessor as plim_preprocessor


def home(request):
    lookup = TemplateLookup(directories=settings.TEMPLATE_DIRS,
                            preprocessor=plim_preprocessor)
    return HttpResponse(lookup.get_template('index.html').render(hello=u'你好'))
