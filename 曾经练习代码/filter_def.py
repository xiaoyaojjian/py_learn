#filter返回的是Iterator，依然是一个惰性序列
#删掉偶数，保留奇数list(filter(is_odd,l))
def is_odd(n):
    return n%2==1
#删除空字符串
def not_empty(s):#list(filter,l)
    return s and s.strip()
# _*_ coding: utf-8 _*_
#计算n以内的所有素数
#1啥也不是,删掉
#取剩下序列第一个数2，他是，他的倍数不是，删掉
#取剩下序列第一个数3，他是，他的倍数不是，删掉
#取剩下序列第一个数5，他是，他的倍数不是，删掉
#---------------------------------------------
#构造一个从3开始的奇数序列（生成器）
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
#筛选函数
def _not_divisible(n):
    return lambda x:x%n>0
#不断返回下一个素数（生成器）
def prime_ai():
    yield 2             #第一个素数是2
    it = _odd_iter()    #初始化序列
    while True:
        n = next(it)    #返回下一素数
        yield n        
        it = filter(_not_divisible(n),it)#重新构造序列
#素数产生实例
for n in prime_ai():
    if n<1000:
        print(n)
    else:
        break
