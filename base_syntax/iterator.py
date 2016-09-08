"""
生成器, 迭代器
"""

# function a builder
def bank(amount):
    while amount > 0:
        amount -= 100
        yield 100
        print('取个钱花.')

# create a iterator
atm = bank(500)
print(atm.__next__())
print(atm.__next__())
print('小份鸡公煲,,,,')
print(atm.__next__())
print(atm.__next__())
print(atm.__next__())
# 继续取则会返回StopIteration
print(atm.__next__())
