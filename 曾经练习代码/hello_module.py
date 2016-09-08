#/usr/bin/env python3
#_*_coding:utf-8_*_
'a test module'
__author__ = 'zlxs'
import sys
def test():
    args = sys.argv
    if len(args) == 1:
        print('HeiHei,Nima')
    else:
        print('Too many argument1')
if __name__ == '__main__':
    test()
#第1行注释是指此文件可直接在Unix，Linux，Mac上运行
#第2行注释是指此文件本身使用标准UTF-8B编码
#第4行使用__author__变量将作者写入
#以上是Python模块标准文件模板
###以下是代码真正部分##################################
##第5行是使用sys模块德尔第一步：导入该模块
'''
导入sys模块后，即有变量sys指向给模块，利用sys变量即可访问sys模块的所有功能
sys模块中有argv变量，利用list存储命令行的所有参数(like matlab whos)
(argv至少有一个元素，because第一个参数永远是该py文件的名称)
'''
'''
当在命令行执行hello_module模块文件时，
Python解释器将一个特殊变量__name__置为__main__
而如果在其他地方执行hello_module模块文件时，
if判断将失败
SO，这种if测试可让一个模块通过命令行运行时执行一些额外代码，
最常见的是运行测试
'''
###测试private函数 _xxxxx ##是以下划线为首的定义
def _private_1(name):
    return 'HeiHei,%s' % name
def _private_2(name):
    return 'HHHHH,%s' % name 
def greeting(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)
'''
在module工开greeting函数，而在内部逻辑用private函数隐藏起来，这样，调用greeting
函数不用关心内部定义的private函数细节：代码封装：
'''
