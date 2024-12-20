from pprint import pprint

import inspect


class Class:
    def __init__(self, a):
        self.value = None
        self.atrib = a

    def method(self, value):
        self.value = value


def info(obj):
    print('Object', obj)
    i = {}
    i['type'] = type(obj).__name__
    i['attrib'] = dir(obj)
    met = []
    i['met'] = met
    for d in dir(obj):
        dd = getattr(obj, d)
        if callable(dd):
            met.append(d)
    mod = inspect.getmodule(obj)
    i['module'] = mod
    return i


pprint(info(Class))
pprint(info(4))
