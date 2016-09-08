"""
用名字索引的列表
"""

from collections import namedtuple
sub = namedtuple('sub', ['x', 'y', 'z'])
a = sub(1, 2, 3)
print(a)
