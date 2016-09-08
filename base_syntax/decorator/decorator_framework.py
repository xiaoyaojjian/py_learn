"""
装饰器框架: 带参数的装饰器
"""


def before(request, kargs):
    print('before')


def after(request, kargs):
    print('after')


def filter(before_func, after_func):
    def outer(main_func):
        def wrapper(request, kargs):
            before_result = before_func(request, kargs)
            if before_result != None:
                return before_result

            main_result = main_func(request, kargs)
            if main_result != None:
                return main_result

            after_result = after_func(request, kargs)
            if after_result != None:
                return after_result
        return wrapper
    return outer


@filter(before, after)
def Index(request, kargs):
    print('index: %s %s' % (request, kargs))

Index('me', 'gy')
