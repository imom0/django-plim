#!/usr/bin/env python

from setuptools import setup


setup(
    name='django_plim',
    version='0.1.0',
    author='iMom0',
    author_email='mobeiheart@gmail.com',
    description=('Introduce plim to django'),
    license='BSD',
    keywords='plim mako django slim',
    url='https://github.com/imom0/django-plim',
    install_requires=[
        'django',
        'plim>=0.9.1',
    ],
    test_suite='nose.collector',
    tests_require='nose==1.3.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: BSD License',
    ],
)
