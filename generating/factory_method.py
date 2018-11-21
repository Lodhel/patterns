# coding: utf-8

"""
Фабричный метод (Factory Method) - паттерн, порождающий классы.

Определяет интерфейс для создания объекта, но оставляет подклассам решение о том, какой класс инстанцировать.
Позволяет делегировать инстанцирование подклассам.

Абстрактная фабрика часто реализуется с помощью фабричных методов.
Фабричные методы часто вызываются внутри шаблонных методов.
"""


class Car(object):
    def show(self):
        raise NotImplementedError()


class Bmw(Car):
    def show(self):
        print('Create Bmw')


class Nissan(Car):
    def skyline(self, model):
        if model == 'R34':
            return SkyR34()

class SkyR34(Nissan):
    def show(self):
        print('Create Nissan Skyline R34')

class Application(object):
    def create_auto(self, type_):
        # параметризованный фабричный метод `create_document`
        raise NotImplementedError()


class MyApplication(Application):
    def create_auto(self, type_):
        if type_ == 'nissan':
            return Nissan()
        elif type_ == 'bmw':
            return Bmw()


app = MyApplication()
app.create_auto('bmw').show() # bmw
app.create_auto('nissan').skyline('R34') .show() # nissan
