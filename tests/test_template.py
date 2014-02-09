#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from unittest import TestCase

from django_plim.template import Template, find_template_dirs


class TemplateTestCase(TestCase):

    def test_template_render(self):
        t = Template('h1 hello')
        self.assertEqual(t.render(), '<h1>hello</h1>')

    def test_context(self):
        t = Template('h2\n  ${hello}')
        context = {'hello': u'你好'}
        self.assertEqual(t.render(**context), u'<h2>你好</h2>')

    def test_template_dirs(self):
        dirs = find_template_dirs()
        self.assertEqual(dirs, [])
