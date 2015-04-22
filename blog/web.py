#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Liu Zhigang'
import logging;log=logging.info;logging.basicConfig(level=logging.INFO)
import os
class jiaja2TemplateEngine(object):
    def __init__(self, templ_dir, **kw):
        from jinja2 import Environment,FileSystemLoader
        self._env = Environment(loader=FileSystemLoader(templ_dir), **kw)
    def __call__(self, path, model):
        self._env.get_template(path).render(**model).encode('utf-8')

class WebApp(object):
    """docstring for WebApp"""
    def __init__(self):
        pass
        # super(WebApp, self).__init__()
        # self.arg = arg

    def get_wsgi_application(self):
        def wsgi(env, start_response):
            pass
        return wsgi

    @property
    def template_engine(self):
        pass

    def run(self, host='localhost', port=8000):
        from wsgiref.simple_server import make_server
        server = make_server(host, port, self.get_wsgi_application)
        log('server start running ')
        server.serve_forever()

wsgi = WebApp()
if __name__ == '__main__':
    wsgi.run()
else:
    aplication = wsgi.get_wsgi_application()
        