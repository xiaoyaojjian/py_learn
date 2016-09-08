# doctest文档测试
# 该模块可直接提取注释中代码并执行测试
# 注释的目的调用该函数所期望的输入和输出
# doctest严格按照Python交互式命令行的输入和输出老判断测试结果是否正确
# 只有测试异常的时候用表示中间一大段的输出
# import re
# m = re.search('(?<=abc)def', 'abcdef')
# m.group(0)
###################################
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Dict(dict):
    '''
    Simple dict but also support access as x.y style.
    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()

'''
若不注释其中函数则说明其中类doctest运行是正确的，否则:
如若将Dict类中method getattr函数注释掉会出现：
**********************************************************************
File "F:\Save\python\test.py", line 9, in __main__.Dict
Failed example:
    d1.x
Exception raised:
    Traceback (most recent call last):
      File "C:\Program Files\Python\lib\doctest.py", line 1320, in __run
        compileflags, 1), test.globs)
      File "<doctest __main__.Dict[2]>", line 1, in <module>
        d1.x
    AttributeError: 'Dict' object has no attribute 'x'
**********************************************************************
File "F:\Save\python\test.py", line 12, in __main__.Dict
Failed example:
    d1['y']
Exception raised:
    Traceback (most recent call last):
      File "C:\Program Files\Python\lib\doctest.py", line 1320, in __run
        compileflags, 1), test.globs)
      File "<doctest __main__.Dict[4]>", line 1, in <module>
        d1['y']
    KeyError: 'y'
**********************************************************************
File "F:\Save\python\test.py", line 15, in __main__.Dict
Failed example:
    d2.c
Exception raised:
    Traceback (most recent call last):
      File "C:\Program Files\Python\lib\doctest.py", line 1320, in __run
        compileflags, 1), test.globs)
      File "<doctest __main__.Dict[6]>", line 1, in <module>
        d2.c
    AttributeError: 'Dict' object has no attribute 'c'
**********************************************************************
1 items had failures:
   3 of   9 in __main__.Dict
***Test Failed*** 3 failures.
'''
