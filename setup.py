#!/usr/bin/env python

from distutils.core import setup, Command
# you can also import from setuptools

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)


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
    cmdclass = {'test': PyTest},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: BSD License',
    ],
)
