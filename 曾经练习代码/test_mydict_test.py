#!/usr/bin/env python3
#-*-coding:utf-8-*-
# 创建测试需要测试的类的类
# 定义TestDict类
# 添加unitset Dict
import unittest
from test_mydict import Dict  # 从test_mydict文件(模块)类调用Dict类


class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))  # error-ed

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')  # error-ed

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')
    # 两个方法会分别在每调用一个测试方法的前后分别被执行
    # 不必在每个测试方法中重复相同的代码
    # 显示嘞嘞嘞嘞嘞嘞嘞嘞嘞嘞嘞嘞嘞嘞嘞嘞嘞嘞嘞嘞
if __name__ == '__main__':
    unittest.main()
# 以上即测试Dict类的测试类TestDict类
'''
以test开头的方法就是测试方法,
不以之开头就不会被认为是测试方法,测试时不会被执行
类unittest.TestCase中有很多内置的条件判断
只需调用这些方法就可断言输出是否是我们所期望的
1 assertEqual  此断言函数返回的结果是否相等
2 assertRaises 此断言函数会抛出指定Error
eg：1通过d['empty']方式访问不存在的key时，断言函数抛出keyerror
    2通过d.empty   方式访问不存在的key时，断言函数抛出AttributeError
'''
'''
#运行单元测试两种方式：
    #1 将test_mydict_test.py当做正常的Python脚本运行
	if __name__ =='__main__':
		unittest.main()
	#2 在命令行通过参数-m unitset直接运行单元测试
	-m unittest test_mydict_test
'''
