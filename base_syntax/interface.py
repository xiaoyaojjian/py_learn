"""
抽象类 + 抽象方法 = 接口
和教学讲的完全不一样, Foo 没有定义 Fun 方法也没有报错
"""


from abc import ABCMeta, abstractclassmethod

class Bar():
    __metaclass__ = ABCMeta

    @abstractclassmethod
    def Fun(self):pass

class Foo(Bar):
    def __init__(self):
        print('__init__')

f = Foo()
f.Fun()