#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Liu Zhigang'

import logging;log=logging.info;logging.basicConfig(level=logging.INFO)
import os,functools


class jiaja2TemplateEngine(object):
    def __init__(self, templ_dir, **kw):
        from jinja2 import Environment,FileSystemLoader
        self._env = Environment(loader=FileSystemLoader(templ_dir), **kw)
    def __call__(self, path, model):
        self._env.get_template(path).render(**model).encode('utf-8')

class WebApp(object):
    """docstring for WebApp"""
    def __init__(self):
        self._template_engine = None
        pass
        # super(WebApp, self).__init__()
        # self.arg = arg

    def get_wsgi_application(self):
        def wsgi(env, start_response):
            start_response('200 OK', [('Content-Type', 'text/html')])
            # return self._template_engine()
            return "<h1>hello</h1>"
        return wsgi

    @property
    def template_engine(self):
        pass

    def run(self, host='localhost', port=8000):
        from wsgiref.simple_server import make_server
        server = make_server(host, port, self.get_wsgi_application)
        log('server start running ')
        server.serve_forever()

def view(path):
    "a @view decorator"
    def _decorator(func):
        @functools.wraps(func)
        def _wrapper(*args, **kw):
            r = func(*args, **kw)
            if isinstance(r, dict):
                log('return template')
                return Template(path, r)
            raise ValueError('expect a dict when using a @view decorator')
        return _wrapper
    return _decorator


def get(path):
    "a @get decorator define a URL"
    def _decorator(func):
        func.__web__route__ = path
        func.__web__method__ = 'GET'
        return func
    return _decorator


def post(path):
    "a @post decorator define a URL"
    def _decorator(func):
        func.__web__route__ = path
        func.__web__method__ = 'POST'
        return func
    return _decorator



wsgi = WebApp()
if __name__ == '__main__':
    wsgi.run()
else:
    aplication = wsgi.get_wsgi_application()
        