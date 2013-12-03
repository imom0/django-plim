#!/usr/bin/venv python
# -*- coding: UTF-8 -*-

from django.http import HttpResponse
from django.template.loader import get_template


def home(request):
    template = get_template('index.html')
    return HttpResponse(template.render(hello=u'你好'))
