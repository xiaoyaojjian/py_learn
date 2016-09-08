"""
将二维数组顺时针旋转90度
"""

data = [[col for col in range(5)] for row in range(5)]

for i in data:
    print(i)
# 重读并重新创建list
print('after my rotating'.center(40,'*'))
da = []
for n in range(len(data[0])):
    da.append([data[i][n] for i in range(len(data)).__reversed__()])
for i in da:
    print(i)
# 在原list内部直接替换
print('replace'.center(40,'*'))
for r_index,row in enumerate(data):
    for c_index in range(r_index,len(row)):
        data[c_index][r_index],data[r_index][c_index] = data[r_index][c_index],data[c_index][r_index]
for i in data:
    print(i)
