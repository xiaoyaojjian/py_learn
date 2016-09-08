# itertools is 用于操作迭代对象的fun
import itertools
# count(n)
naturals = itertools.count(1)  # create a limitless iter
'''
for n in naturals:
	print(n)
'''
# cycle(a)
cs = itretools.cycle('ABC')  # create a order limitless
'''
for n in cs:
	print(n)
'''
# repeat(a,times)
ns = itertools.repeat('A', 3)  # 3 times print(A)
'''
for i in ns:
	print(i)
'''
# by takewhile() 根据条件判断截取出有效（限）の序列
# 修改1
# takewhile(f)
nss = itertools.takewhile(lambda x: x <= 10, naturals)
list(nss)
# chain(a,b,c) 将abc 3个迭代队形串联出来 形成更大迭代器
nn = itertools.chain('ABC', 'XYZ')
'''
for i in nn:
	print(i)
'''
# groupby 将迭代中相邻重复元素分组
for key, group in itertools.groupby('AABBCCCDDDDAAA'):
    print(key, list(group))  # 打印出键与对应值
# 修改是上
for key, group in itertools.groupby('AABbCCcDDcAAs', lambda c: c.upper()):
    print(key, list(group))
'''
# 挑选规则是通过函数完成
只要作用于funの两个元素返回值相等 则两个元素就被认为是在一组
而fun返回值作为组のkey
if 我们忽略大小写分组 即可让元素'A''a'返回同样のkey
'''
########################################################
# itertools module 提供的是处理迭代功能的fun 其返回值为Iterator 不是list
# 只有通过for循环迭代时才会有真正的计算
########################################################
