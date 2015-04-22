#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Liu Zhigang'


from base.web import get,view


class NAME(object):

    def __init__(self, name='o_o', email='1@!'):
        self.name = name
        self.email = email

a = NAME('aaaa', 'aaa@aaaa')
b = NAME('bbbb', 'bb@bbbb')

di = {'a': a, 'b': b}


@view('test_user.html')
@get('/')
def get_user():
    return di
