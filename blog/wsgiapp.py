#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Liu Zhigang'


import os,sys

#get root dir
root_dir = os.path.dirname(os.path.abspath(__file__))
print root_dir

from base.web import WebApp, jiaja2TemplateEngine

import logging;logging.basicConfig(level=logging.INFO)




#init a wsgi app
wsgi = WebApp()

template_engine = jiaja2TemplateEngine

wsgi._template_engine = template_engine

import urls



