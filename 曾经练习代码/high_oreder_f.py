#from high_oreder_f import 
#借用高阶函数定义来实战map
#先定义一个（内函数）f=x2
def f(x):
    return x * x
#实现reduce
#实现序列求和
def add(x,y):
    return x + y
#将[1,2,3,4,5]变换成整数12345
#reduce
def fnn(x,y):
    return x*10+y
#整理str2int
def str2int2(s):
    def fnn(x,y):
    return x * 10 + y
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,
         ...'7':7,'8':8,'9':9}[s]
#好扯淡~~~
#规范名字函数
#将不规范的名字规范化
#in ['adam', 'LISA', 'barT'];out ['Adam', 'Lisa', 'Bart']
#istitle判断首字母大写
#str.upper
#str.lower
def nor_name(name):

