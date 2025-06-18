#!/usr/bin/env python
# Copyright (C) 2019-present  Ben Spiller

import codecs, os, glob, sys, shutil

ROOTDIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(ROOTDIR)

import sphinxcontrib_autodocgen

import setuptools
print('using setuptools v%s'%setuptools.__version__)
from setuptools import setup, find_packages

# Conditional dependencies were added before v37, so need that version when building from source. 
# (end-users should be using the wheel so won't be affected).
assert int(setuptools.__version__.split(".", 1)[0]) >= 37, 'Please upgrade setuptools and wheel to latest versions (pip install --upgrade setuptools wheel); current setuptools=%s'%setuptools.__version__


# classifiers come from PyPi's official list https://pypi.org/classifiers/
PLATFORMS_CLASSIFIERS = [
	"Operating System :: OS Independent",
]
CLASSIFIERS = [
	"Development Status :: 5 - Production/Stable",
	"Intended Audience :: Developers",
	"Framework :: Sphinx :: Extension",
	"Programming Language :: Python :: Implementation :: CPython",
	"Intended Audience :: Developers",
	"Natural Language :: English",
]+PLATFORMS_CLASSIFIERS
KEYWORDS = ['sphinx', 'autodoc']

with codecs.open(ROOTDIR+'/README.rst', "rb", "ascii") as f:
	long_description = f.read()

setup(
	name='sphinx-autodocgen',
	description='Sphinx AutoDocGen extension',
	
	url="https://github.com/ben-spiller/sphinx-autodocgen",
	project_urls={ # see PEP-0459
		'Repository':        'https://github.com/ben-spiller/sphinx-autodocgen',
	},

	version=sphinxcontrib_autodocgen.__version__,
	author=sphinxcontrib_autodocgen.__author__, 
	maintainer='Ben Spiller',
	license=sphinxcontrib_autodocgen.__license__,
	keywords=KEYWORDS,
	classifiers=CLASSIFIERS,
	platforms=PLATFORMS_CLASSIFIERS,
	long_description=long_description,
	long_description_content_type='text/x-rst',

	python_requires=">=3.6", # be flexible

	packages=setuptools.find_packages(),

	install_requires=[
		"sphinx"
	],

	)
	
