####获取对象(类型)
print('123的类型：',type(123))
print('\'st\'的类型：',type('st'))
print('None的类型：',type(None))
print('abs的类型：',type(abs))
#a = Animal()#a is Animal对象
#print('a的类型：',type(a = animal()))
isinstance('st',str)
isinstance(12,int)
isinstance([1,2,3],(list,tuple))
isinstance([1,2,3],tuple)
isinstance((1,2),tuple)
#使用dir（）调用一个对象所欲属性和方法
print('\'abc\'の所欲属性和方法可通过dir显示：')
dir('abc')
print('两种方法调用出‘abc’长度')
len('abc')
'abc'.__len__()
'abc'.upper()
#使用自己の类
class myDog(object):
    def __len__(self):
        return 100
dog = myDog()
len(dog)
print('接下来通过类来说明操作对象的状态')
class myObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = myObject()
hasattr(obj,'x')#有'x'这个属性吗？
hasattr(obj,'y')#有'y'这个属性吗？
setattr(obj,'y',99)#设置一个属性'y'
hasattr(obj,'y')#有'y'这个属性吗？
getattr(obj,'x')
getattr(obj,'y')#获取属性xy
obj.x
obj.y
getattr(obj,'z',404)#本身属性中没有z，如果不存在，就返回设置好的默认值404
