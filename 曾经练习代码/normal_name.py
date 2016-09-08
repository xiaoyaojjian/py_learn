'''
name='adam'
import string
if str.isupper(name(0))=='False':
    str.upper(name(0))
    print(name)
'''
#将不规范的名字规范化
#in ['adam', 'LISA', 'barT'];out ['Adam', 'Lisa', 'Bart']
#str.istitle判断首字母大写 只能判断或者计算一个str
#str.upper
#str.lower
#输入一个name->str规范化
#判断输入的name中是否istitle了
#若满足了则直接输出name
#若不满足则先将首字母upper下
#          后将循环将name后面all字母小写lower
#输出name
# _*_ coding:utf-8 _*_
from functools import reduce
def nor_name(name):
    if str.istitle(name) == 'True':
        print(name)
    else:
        head_name=str.upper(name[0])
        tail_name=str.lower(name[1:])
        name=head_name + tail_name
        print(name)
#原来这么简单用字符串函数，甚至用循环，不用
#def prod()函数求list积利用reduce
def prod(x,y):
    return x * y
#利用map and reduce 编写一个str2float函数（字符串转换成浮点数）
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2float(s):
    return reduce(lambda x,y: x*10 +y,map(char2num,s))#未完成，这是str2int的，没有实现小数点
