# coding: utf-8


class Singleton(type):
    def __init__(cls, name, bases, class_dict):
        super(Singleton, cls).__init__(name, bases, class_dict)
        cls._instance = None

    def __call__(cls, *args):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args)
        return cls._instance
