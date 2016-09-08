#generator是通过某种算法来推算出 可以通过循环 推算出后续元素
#就不必创建完整list
#list comprehension
L = [x * x for x in range(10)]  #L is a list
#generator_1
g = (x * x for x in range(10))  #g is a generator
#调用g时 需要next函数(很少用)
next(g)
#可用for循环一次调用出来
for s in g:
    print(s)
#获取斐波那契数列_定义函数获得_顺序执行
def fib1(num): #num指推算到第num个fib数
    n,a,b = 0,1,1  #fib前两个不能推算
    while n < num:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
#generator_2
#获取斐波那契数列_这是一个generator_调用next(),遇到yield返回
def fib2(num):
    n,a,b = 0,1,1
    while n < num:  
        yield(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
#以odd函数来解释yield返回执行
def odd():
    print('st1')
    yield 1
    print('st2')
    yield 2
    print('st3')
    yield 3
#上述函数没有返回值     
