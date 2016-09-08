#迭代器Iterator
#Python for 本质 通过不断调用next（）函数实现
for x in [1,2,3,45]:
    pass
#in fact 完全等价为
#首先获得Iterator object
it = iter([1,2,3,4,5])
#循环
while True:
    try:
        #获得下一值
        x = next(it)
        #遇到不可迭代时停止
    except StopIteration:
        #遇到stopiteration时退出循环
        break
