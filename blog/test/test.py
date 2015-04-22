#!/usr/bin/env python

# decretor  wrapper
def log(fun):
    def wrapper(*arg, **kw):
        print 'call %s' % fun.__name__
        fun(*arg, **kw)
        print 'eend'
    return wrapper


@log
def now():
    print '1234'


class Next:
    List = []

    def __init__(self, low, high):
        for Num in range(low, high):
            self.List.append(Num ** 2)

    def __call__(self, Nu):
        return self.List[Nu]

b = Next(1, 7)
print b.List
print b(2)
