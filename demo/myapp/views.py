#!/usr/bin/venv python
# -*- coding: UTF-8 -*-

from django.http import HttpResponse
from django_plim.loaders import Loader
from django.template import Context, Template


def home(request):
    template = Template('h2\n  ${hello}')
    context = {'hello': u'你好'}
    return HttpResponse(template.render(context))
