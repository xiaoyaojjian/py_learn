"""
经典类，具有一种@property装饰器
"""


class Goods:

    @property
    def pwd(self):
        return "shiina"
# ############### 调用 ###############
obj = Goods()
result = obj.pwd  # 自动执行 @property 修饰的 pwd 方法，并获取方法的返回值
print(result)


print('Level line'.center(80, '*'))

"""
新式类有三种@property装饰器
"""


class Goods(object):
    def __init__(self, password):
        self.__pwd = password

    # 只读
    @property
    def pwd(self):
        print('property')
        return self.__pwd

    # 只写
    @pwd.setter
    def pwd(self, value):
        print('pwd.setter')
        self.__pwd = value

    @pwd.deleter
    def pwd(self):
        print('pwd.deleter')
        print(self.__pwd)

# ############### 调用 ###############
obj = Goods('pass')

print(obj.pwd)          # 自动执行 @property 修饰的 pwd 方法，并获取方法的返回值

obj.pwd = 123    # 自动执行 @pwd.setter 修饰的 pwd 方法，并将  123 赋值给方法的参数

del obj.pwd      # 自动执行 @pwd.deleter 修饰的 pwd 方法