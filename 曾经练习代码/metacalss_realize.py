#使用元类
##metaclass:类class是元类metaclass创建出来の实例
'''
metaclass可给自定义のMyList增加一个add方法:定义ListMetaclass
按照默认习惯metaclass总以Metaclass结尾，以示其为一个Metaclass
'''
#metaclass 是创建类so必须从type类型派生
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)
class MyList(list):
        __metaclass__ = ListMetaclass #说明使用ListMetaclass来定制类
'''
create l1 = MyList() should l1.add(1)
create l2 = list()   can't
可是没出现啊！
'''
