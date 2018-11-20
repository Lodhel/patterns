# coding: utf-8

"""
Прототип - паттерн, порождающий объекты.

Задает виды создаваемых объектов с помощью экземпляра-прототипа
и создает новые объекты путем копирования этого прототипа.
"""

import copy


class Prototype(object):
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, attrs):
        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(attrs)
        return obj

    def __str__(self):
        return self._objects


class User(object):
    """Птица"""


prototype = Prototype()
prototype.register('user',  User())

data = prototype.clone('user', {
    'first_name': 'Jack',
    'last_name': "Word"
})
print(data.first_name) # <class '__main__.Bird'> Owl

