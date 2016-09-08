"""
标准装饰器
"""


def login(func):
    def inner(*args,**kwargs):
        print('login ok!')
        return func(*args,**kwargs)
    return inner


@login
def index(name):
    print('This is %s\'s Index' % name)

index('shiina')


