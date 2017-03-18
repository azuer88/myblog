#/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Blue Cuenca'
SITENAME = u'azuer88'
SITEURL = 'https://azuer88.github.io/myblog'

PATH = 'content'

TIMEZONE = 'Asia/Manila'

DEFAULT_LANG = u'en'

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
        )

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/azuer88/'),
         )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME="./themes/pelican-bootstrap3"
