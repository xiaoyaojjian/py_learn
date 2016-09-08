"""
类的静态方法, 私有方法和私有字段
"""


class WhoAreYou(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有字段

    # 私有方法
    def __delete(self):
        print('delete %s' % self.name)

    def shachu(self):
        self.__delete()

    def show(self):
        print(self.__age)

    def select(self):
        print('%s login' % self.name)

    # 静态方法
    @staticmethod
    def funv():
        print('okk.')

me = WhoAreYou('shiina', 19)
me.select()

# 调用私有方法的两种方式
me.shachu()  # 由类中其他的函数从内部调用
me._WhoAreYou__delete()  # 强制调用私有方法

# 静态方法
me.show()
WhoAreYou.funv()



