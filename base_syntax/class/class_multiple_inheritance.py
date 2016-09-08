"""
类的多重继承, 经典类: 深度优先, 新式类: 广度优先 <-- 教学和博客里是这么说,
但是后来的版本好像是做了修改, 经典类.新式类都是广度优先
"""

# 经典类 深度优先
class A:
    def __init__(self):
        print('this is A')

    def show(self):
        print('show method from A')


class B(A):
    def __init__(self):
        print('this is B')


class C(A):
    def __init__(self):
        print('this is C')

    def show(self):
        print('show method from C, 广度优先')


class D(B, C):
    def __init__(self):
        print('this is D')

me = D()
me.show()


# 新式类 广度优先
class Q(object):
    def __init__(self):
        print('this is Q')

    def show(self):
        print('show method from Q, 深度优先')


class W(Q):
    def __init__(self):
        print('this is W')


class E(Q):
    def __init__(self):
        print('this is E')

    def show(self):
        print('show method from E, 广度优先')


class R(W, E):
    def __init__(self):
        print('this is R')

me2 = R()
me2.show()
