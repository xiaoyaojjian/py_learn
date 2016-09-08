#iteration
#by dict
d = {'a':1,'b':2,'c':3,'d':4}
print('key=\n')
for key in d:
    print(key)
#dict 不按顺序 not like list，so 输出解雇顺序很可能不一样
#默认情况下，dict迭代の是key，if want to iter value，shuold 
#for value in d.values
print('value=\n')
for  value in d.values():
    print(value)
#if need to 迭代key value ，可以用for k,v in d.items()
print('key,value=\n')
print('value,key=\n')
for  key,value in d.items():
    print(key,value)
    print(value,key)
#char(string)亦是迭代，so 作用于for 循环
print('ch=\n')
for ch in 'ABC':
    print(ch)
#判断一个对象是否是一个可迭代对象
from collections import Iterable
isinstance('abc',Iterable) #str 是否可迭代
isinstance('[1,2,3]',Iterable) #list 是否可迭代
isinstance(123,Iterable) # int 是否可迭代
#将list 实现类似Java下表循环，Python enumerate（枚举，列举）
#将list 变成 index-element
print('i,value=\n')
for i,value in enumerate(['A','B','C']):
    print(i,value)
#for 循环引用两个或多个var
print('x,y,z=\n')
for x,y,z in [(1,2,3),(4,5,6),(7,8,9)]:
    print(x,y,z)
