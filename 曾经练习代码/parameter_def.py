#测试函数の 参数parameter
'''
def power(x):   #对于power 函数 x is a 位置参数
    return x*x
'''
#位置参数
def power(x,n=2):   #这里默认参数n为2，当调用fun时未输入parameter n则系统默认为2
    pow = 1
    while n>0:      #这里不易使用for，根本不知道循环几次
        pow = x*pow
        n = n-1
    return pow
#默认参数
def enroll(name,gender,age=6,city='xian'):#在顺序调用默认参数，若要跳跃调用则加上参数名
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
#可变参数(允许0个或多个参数)
def calc(*numbers):#calc(numbers):这里の*是指将numbers可变化,准确来说是个数可变
	sum = 0		   #若是无*则调用时应以一个list or tuple来调用如calc([1,2,3])
	for n in numbers:
		sum = sum + n*n
		return sum
#关键字参数(允许0个或多个含参数名的参数)
def person(na,ag,**kw):#这里的kw是一个关键字，dict化，可传入必选参数，作为扩展函数
	print('name:',na,'age:',ag,'other:',kw)
#命名关键字参数
def person1(na,ag,**kw):#传入任意不受控制的关键字控制
#参数组合（必选参数，默认参数，可变参数/命名关键字参数，关键字参数混合(有顺序)）
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=','c=',c,'args=','kw=',kw)
def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
