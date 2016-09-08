import random

# 随机一个 [0.0, 1.0) 之间的数
print(random.random())

# 从指定范围内随机一个数
print(random.randint(1, 1000))

# 从指定范围内随机一个数, 可指定步长(不指定默认为1)
print(random.randrange(0, 1000, 10))
