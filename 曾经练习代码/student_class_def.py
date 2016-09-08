std1 = {'name':'maz','score':98}
std2 = {'name':'boo','score':88}
def print_score(std):
    print('%s: %s' % (std['name'],std['score']))
#对象化
class Student(object):
    """docstring for Student"""
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score_class(self):
        print('%s: %s' % (self.name,self.score))
    def get_grade(self):
        if self.score >=90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'
#为Student类添加访问限制#已经从外部无法访问实例变量__name,实例变量__score
class Student_p(object):
    """docstring for Student1"""
    def __init__(self,name,score):
       self.__name = name
       self.__score = score
    def print_score_class(self):
        print('%s: %s' % (self.__name,self.__score))
    #若是想获得实例的name 和 score
    def get_name(self):
        print('%s' % (self.__name))
    def get_score(self):
        print('%s' % (self.__score))
    #若是想进行修改实例的name 和 score
    def set_name(self,name):
        self.__name = name
    def set_score(self,score):
        self.__score = score
########################################
class Student_a(object):
    name = 'Student_a'####create class attribute
s = Student_a()#create 实例 s
print(s.name)#输出s 的 name 属性，so会继续查找class-》Student的name 属性
print(Student_a.name)#输出 Student的name属性
s.name = 'maz'#给实例s赋给name属性
print(s.name)#输出实例s的name属性
print(Student_a.name)#butclass 属性未消失用Student 仍然可访问
del s.name#若删除实例s的name属性
print(s.name)#由于实例s的属性不在了，所以类的属性就显示出来
####为实例绑定任何属性和方法+++动态语言的灵活性
from types import MethodType
###绑定属性和方法
class Student_s(object):
    pass
s = Student_s()
s.name = 'maaa'#绑定一个属性
print(s.name)#调用属性
def set_age(self,age):
    self.age = age
s.set_age = MethodType(set_age,s)#给实例s直接绑定一个方法
s.set_age(25)#调用方法
s.age#测试结果
###给一个实例绑定的方法是对另一个实例不起作用
s2 = Student_s()
try:
    s2.set_age(24)#尝试调用s绑定的方法
except:
    print('@@@@抛出错误：s2.set_age(24)——实例绑定方法不可假借（s中的绑定，s2无用）')
###为给所有实例都绑定方法 则给class绑定方法
class Student_ss(object):
    pass
def set_score(self,score):
    self.score = score
Student_ss.set_score = MethodType(set_score,Student_ss)###给对象Student_s直接绑定一个方法
s3 = Student_ss()
s4 = Student_ss()
s3.set_score(1200)
s4.set_score(100)
#####限制实例的属性
##只允许对Stu类实例添加name age
class  Student_slot(object):
    __slots__ = ('name','age')#用tuple定义允许绑定的属性名称
sl = Student_slot()
sl.name = 'mm'#绑定属性name
sl.age = 22#绑定属性age
try:
    sl.score = 100#绑定属性score
except:
    print('@@@@抛出错误：类Student_slot定义限制不能绑定属性score')

###测试__slot__ 对于子类是否起作用
class Student_son(Student_slot):
    pass
sson = Student_son()
sson.score = 9999
print('父类Student_slot中__slot__限制对子类Student_son不起作用，依然可添加score')
#####class定义中绑定属性添加规定属性
##此例子中不能对score 夏季吧 绑定数据了
class Student_f(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value <0 or value >100:
            raise ValueError('score must be between 0 and 100!')
        self._score = value
####改进上述使用属性的 使用@property装饰器
class Student_fp(object):
    @property
    def score(self):
        return self._score#***replace**#
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value <0 or value >100:
            raise ValueError('score must be between 0 to 100')
        self._score = value#***replace**#
###########################################################
'''
若替换：
class Student_fp(object):
    @property
    def score(self):
        return self.score#***replace**#
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value <0 or value >100:
            raise ValueError('score must be between 0 to 100')
        self.score = value#***replace**#
在这里_score是一个变量
       score是一个方法
self.score实际上是调方法，而不是变量。
不是需要下划线，而是需要不同的变量名区分
####在这里我们需要调用变量（成员） 而不是 方法（成员函数）
在需要替换的两行中
return 变量 self._score
value 赋值给 变量self._score
self.scoreの调用method会不停调用score这个方法（函数本身）
进而形成递归！！！！！！！！！！！！！！！！！！！
'''
###########################################################
'''
#***replace**#行中的_score 替换成 score
当不对score进行保护时，即_score 出现 递归bla bla bla
File "F:\Save\python\test.py", line 11, in score
    self.score = value
RecursionError: maximum recursion depth exceeded
'''
###########################################################
#利用@property装饰器来控制属性的读写属性
class  Student_gs(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def  birth(self,value):
        self._birth = value
    @property
    def age(self):
        return 2015 - self._birth
