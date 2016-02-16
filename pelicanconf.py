#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# This file is only used if you explicitly specify it as your config file.
  
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *
 
SITENAME = u"""<span style="color:#EB2D2D;">Fox</span> <span style="color:black;">OSS Information</span>"""
SITEURL = 'http://localhost:8000'
RELATIVE_URLS = True
  
  
TIMEZONE = 'Europe/Zurich'
DEFAULT_LANG = u'en'
DATE_FORMATS = {'en': '%Y-%m-%d'}
OUTPUT_PATH = 'output/'
DEFAULT_PAGINATION = 10
PATH = 'content'
  
# Plugins and extensions
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid',
                'toc(permalink=true)']
PLUGIN_PATHS = ['plugins', 'pelican-plugins/']
PLUGINS = ['sitemap', 'extract_toc', 'liquid_tags.img',
           'neighbors', 'latex', 'related_posts', 'assets', 'share_post',
           'multi_part']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
 
# Appearance
TYPOGRIFY = True
THEME = 'bbTheme/'
 
# Elegant theme
STATIC_PATHS = ['theme/images', 'images']
DIRECT_TEMPLATES = (('index', 'authors', 'tags', 'categories', 'archives', 'search', '404', 'feeds'))
USE_SHORTCUT_ICONS = True
 
# Elegant Labels
SOCIAL_PROFILE_LABEL = u'Social Links'
RELATED_POSTS_LABEL = 'Related Posts'
SHARE_POST_INTRO = 'Like this post? Share it on:'
COMMENTS_INTRO = u'Feel free to leave your comments below.'
 
# Defaults
DEFAULT_CATEGORY = 'Miscellaneous'
SUMMARY_MAX_LENGTH = 50
 
# Legal
SITE_LICENSE = u'<span xmlns:dct="http://purl.org/dc/terms/" property="dct:title"> Fox OSS Information</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://www.your-url-here.org" property="cc:attributionName" rel="cc:attributionURL">Your Name</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.'
 
# SEO
SITE_DESCRIPTION = u'Fox Open Source Strategy Information'
 
# Landing Page
PROJECTS = [
        {
            'name': 'Check out my GitHub page',
            'url':
            'https://github.com/yourname',
            'description': ' for a list of my projects'},
        {
            'name': 'FancyProject',
            'url':
            'https://github.com/yourname',
            'description': ' a very fancy project I made'},
        {
            'name': 'AwesomeProject',
            'url':
            'https://github.com/yourname',
            'description': ' another awesome project I made'},
        ]
         
LANDING_PAGE_ABOUT = {'title': 'My blog title goes here',
        'details': """<p>Here you can write a nice welcome message!</p><p>Then you maybe want to write something about your organisation, maybe with a <a href="https://www.your-url-org">link</a>.</p><p>Then you can descripe what kind of content people will find in your blog</p><p>Finally I recommend to add contact possibilities, maybe an address to send an <a href="mailto:yourmail@your-url-here.org">E-Mail</a>.</p>"""}
 
# Feeds
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
  
# Blogroll
LINKS = (('Your', 'https://www.your-url-here.org'),)
  
# Social
SOCIAL = (
        ('Github', 'http://github.com/yournamehere'),
        ('Email', 'mailto:yourmail@your-url-here.org'),
          )

