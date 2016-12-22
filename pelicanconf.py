#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'OpenClassrooms'
SITENAME = "Parcours Développeur d'Application"
SITEURL = ''
GOOGLE_ANALYTICS = "44"

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'Europe/Paris'
CSS_FILE = 'stylesheet.css'
JS_FILE = 'scripts.js'

DEFAULT_LANG = 'fr'

# Our variables
PRIVACY_LINK = "https://openclassrooms.com/privacy-policy#personal-data-gathering"
PAGE_PATHS = ['students']
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'students'
DELETE_OUTPUT_DIRECTORY = True
PATH = 'content'
PAGE_URL = '{category}/{slug}.html'
PAGE_SAVE_AS = '{category}/{slug}.html'

# Local only. For production, see publishconf.py
# SITEURL = 'alumnis/' 

# Plugins

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-md-metayaml']


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 9

THEME = 'openclassrooms'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
