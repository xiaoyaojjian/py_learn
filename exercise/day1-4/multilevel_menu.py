'''
三级菜单选择, 任何时候输入q 可退出, 输入b 可跳到一级菜单,
question: 输入不存在的值时,没有处理
'''
data = {
    'a': {'a1': ['a11','a12','a13'], 'a2': ['a21','a22','a32'], 'a3': ['a31','a32','a33']},
    'b': {'b1': ['b11','b12','b13'], 'b2': ['b21','b22','b32'], 'b3': ['b31','b32','b33']},
    'c': {'c1': ['c11','c12','c13'], 'c2': ['c21','c22','c32'], 'c3': ['c31','c32','c33']}
}


def choose():
    choose_val = input('Please input you choose:')
    return choose_val
'''
打印三级列表
'''


def one_list():
    for one in data.keys():
        print('#:'+one)


def two_list(cho1):
    if cho1 in data.keys():
        for two in data.get(cho1).keys():
            print('#:%s' % two)


def three_list(cho2):
    if cho2 in data[cho1].keys():
        for three in data.get(cho1).get(cho2):
            print('#:%s' % three)

for i in range(3):
    one_list()
    cho1 = choose()
    if cho1 == 'q':exit('qiut')
    if cho1 == 'b':print('this is the first level list')
    two_list(cho1)
    two_list(cho1)
    cho2 = choose()
    if cho2 == 'q':exit('qiut')
    if cho2 == 'b':continue
    three_list(cho2)
    cho3 = choose()
    if cho3 == 'q':exit('qiut')
    elif cho3 == 'b':continue
    else:break
print('你的选择是:%s' % cho3)
