"""
生成斐波那契数列
"""


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

l = []
for i in range(20):
    l.append(fib(i))
print(l)