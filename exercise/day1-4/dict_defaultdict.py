from collections import defaultdict

tx = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]
dic1 = defaultdict(list)  # 设置字典的 value 默认是 list 类型
for n in tx:
    if n > 66:
        dic1['k1'].append(n)
    else:
        dic1['k2'].append(n)
print(dic1)

'''
dic = {}
for n in tx:
    if n < 60:
        if 'k2' in dic.keys():
            dic['k2'].append(n)
        else:
            dic.setdefault('k2',[n,])
    else:
        if 'k1' in dic.keys():
            dic['k1'].append(n)
        else:
            dic.setdefault('k1',[n,])
print(dic)
'''