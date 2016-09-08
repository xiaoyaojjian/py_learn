"""
计算器, 用了eval() 没有任何意义了, 四则运算应该单独写一个函数处理
"""


import re
a = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
print(eval(a))


def get_brackets_data(formula):
    return re.findall('\(([^()]+)\)', formula)

while re.search('[()]', a):
    for i in get_brackets_data(a):
        a = a.replace('(%s)' % i, str(eval(i)))
    print(a)
print(eval(a))