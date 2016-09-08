"""
迭代器
"""

import time


# 定义一个生成器
def cousumer(name):
    print('%s 想要吃个包子.' % name)
    while True:
        baozi = yield
        print('包子[%s]来了, 被[%s]吃了.' % (baozi, name))


# 由生成器创建一个迭代器
def producer(name):
    c = cousumer('me')
    c2 = cousumer('gy')
    c.__next__()
    c2.__next__()
    print('包子准备中...')
    for i in range(10):
        time.sleep(1)
        print('生成了两个包子')
        c.send(i)
        c2.send(i)
producer('god')