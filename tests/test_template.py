#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from unittest import TestCase

from django_plim.template import Template


class TemplateTestCase(TestCase):

    def test_template_render(self):
        t = Template('h1 hello')
        self.assertEqual(t.render(), '<h1>hello</h1>')
