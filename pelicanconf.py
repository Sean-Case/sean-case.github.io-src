#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sean Case'
SITENAME = u"Sean Case's Portfolio Site"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'EN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS =  ( ('Back home', '/'),
			('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('ggplot2', 'http://ggplot2.org/'))

# Social widget
SOCIAL =  (('Twitter', 'https://twitter.com/SeaninDK'),
           ( 'Github', 'http://github.com/sean-case'),
		   ('Email', 's_case@hotmail.com'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['C:/Users/s_cas/Documents/GitHub/pelican-plugins','C:/Users/s_cas/Documents/GitHub/pelican-plugins']
PLUGINS = ['extract_toc','rmd_reader']

STATIC_PATHS = ['figure']
RMD_READER_RENAME_PLOT = 'directory'
RMD_READER_KNITR_OPTS_CHUNK = {'fig.path': 'figure/'}

THEME = 'themes/sober'

# Display pages list on the top menu
DISPLAY_PAGES_ON_MENU  = True

PELICAN_SOBER_STICKY_SIDEBAR = True

# Display categories list on the top menu
DISPLAY_CATEGORIES_ON_MENU  = True

# Display categories list as a submenu of the top menu
DISPLAY_CATEGORIES_ON_SUBMENU  = False

# Display the category in the article's info
DISPLAY_CATEGORIES_ON_POSTINFO  = False

# Display the author in the article's info
DISPLAY_AUTHOR_ON_POSTINFO  = False

# Display the search form
DISPLAY_SEARCH_FORM  = False

# Sort pages list by a given attribute
PAGES_SORT_ATTRIBUTE  = 'Title'

# Display the "Fork me on Github" banner
GITHUB_URL  = None

GOOGLE_ANALYTICS = 'UA-29489330-2'

MD_EXTENSIONS = ['toc']

DISQUS_SITENAME = "seancase"
