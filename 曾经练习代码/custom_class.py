#定制类 __XXX__ var or functinoname = 属性，方法 特殊用处 eg:__slot__,__len__
###__str__返回字符串（修饰）
###__getattr__试图（在没有找到属性的情况下才调用）获得属性
###__call__直接对实例本身进行调用
class Student(object):
    """docstring for Student"""
    def __init__(self, name):
        self.name = name
    ###仅有__init__不好
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    ###仅有__init__ __str__不用print依然不好
    ##if 无 print 仅是调用 __repr__ 而不是__str__
    #__str__返回用户看到的字符串
    #__repr__返回程序员看到的字符串
    ###添加一个__repr__(like __str__) 偷个懒
    __repr__ = __str__
###__iter__将此类转换成可迭代对象
###__getitem__表现成like list 按下标取出元素
    def __getattr__(self,attr):
        if attr == 'score':
            return 99       #返回score值
        if attr == 'age':
            return lambda:25#返回age函数
        ##要让class只响应特定几个属性，则按照约定抛出错误(若没有抛出指令则默认返回None)
        raise AttributeError('\'Student\' object has no this attribute \'%s\'' % attr)
###将对象与函数之间弱化，将创建的实例编程可调用的对象
    def __call__(self):
        print('My name is %s' % self.name)
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1#初始化计数器a b
    def __iter__(self):
        return self        #实例本身就是迭代对象 返回自己
    def __next__(self):
        self.a,self.b = self.b,self.a + self.b #算下一个值
        if self.a >10000:      #退出循环条件
            raise StopIteration()
        return self.a          #返回下一个值
    def __getitem__(self,n):#####同时实现slice
        if isinstance(n,int):#判断传入参数n是否为int索引
            a,b = 1,1 
            for x in range(n):
                a,b = a,a + b
            return a
        if isinstance(n,slice):#判断传入参数n是否为slice切片
            start = n.start
            stop  = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x >=start:
                    L.append(a)
                a,b = b,a+b
            return L        #返回对应list
'''
实现__iter__
for x in Fib():
    print('将Fib()实例作用于for循环中：\n',x)
实现__getitem__
print('可访问f中任意一项：\n')
f = Fib()
f[0]
f[10]
实现 list 中 slice切片功能
print('可利用切片功能:\n')
f[0:5]
f[:8]
'''
##利用完全动态__getattr__ 链式调用
class Chain(object):
    def __init__(self,path=''):
        self._path = path
    def __getattr__(self,path):
        return Chain('%s\%s' % (self._path,path))
    def __str__(self):
        return self._path
    __repr__ = __str__ 
