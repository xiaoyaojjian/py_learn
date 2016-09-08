# doctest文档测试
# 该模块可直接提取注释中代码并执行测试
'''
注释的目的调用该函数所期望的输入和输出
doctest严格按照Python交互式命令行的输入和输出老判断测试结果是否正确
只有测试异常的时候用表示中间一大段的输出
'''
import re
m = re.search('(?<=abc)def', 'abcdef')
m.group(0)
###################################


class Dict(dict):
'''
Simple dict but also support access as x.y style
>>> from test_mydict import Dict
>>> d1 = Dict()
>>> d1['x']=100
>>> d1.x
100
>>> d1.y = 200
>>> d1['y']
200
>>> d2 = Dict(a=1,b=2,c='3')
>>> d2.c
'3'
>>> d2['empty']
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d2['empty']
KeyError: 'empty'
'''

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
if __name__ = '__main__':
    import doctest
    doctest.testmod()