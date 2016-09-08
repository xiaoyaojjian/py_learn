####返回函数，在返回函数时，该函数没有执行，再要调用时才会
####返回函数中不要引用任何可能变化的变量
#可变参数求和
Lv = [1,2,3,4,5,6,7,8]
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
#调用
def lazy_sum(*args):
    print('这是利用lazy_sum调用了sum函数，so不显示求和结果，会返回求和的函数')
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
'''
在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，
相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
两次调用的lazy_sum函数返回的值都不一样
所谓 新的函数是指 功能一样的函数，只是在内存存的地方不一样
'''
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
#尝试计算f1 f2 f3 = count()
#改进版###添加一个函数g()让值进行j*j，而将循环的作用放在count（）中
def count0():
    def f(j):
        def g():
            return j*j
        return g
    fs =[]
    for i in range(1,4):
        fs.append(f(i))#f(i)立即被执行
    return fs
#####匿名函数lambda
lll = list(map(lambda x:x*x,Lv))
def f1(x):
    return x*x
f2 = lambda x: x*x
def f3(x,y):
    return lambda: x*x + y*y
#####未添加装饰器####DEcorator
def now():
    print('2015,11,24')
####添加装饰器###########
def log1(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper
#####丰富自定义log文本###
def log2(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s,%s():' %(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
#####完整的decorator#####
import functools
def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % (text,fun.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
##偏函数###
#创建偏函数时，可接受3个参数：函数对象，*args **kw
int2 = functools.partial(int,base = 2)
int2('10010')
#当传入以上函数操作时，相当于输入一下操作
# kw ={'base':2}
# int('10010',kw)
max2 = functools.partial(max,10)
max2(5,6,8)
#当传入以上函数时，相当于输入以下操作
#args = (10,5,6,8) 自动将10作为*args参数的一部分添加到左边
#max(*args)
