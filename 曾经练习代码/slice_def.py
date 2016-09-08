#!/usr/bin/env/ python3
# _*_ coding : utf-8 _*_

#高级特性_切片
#取List L 中前三个元素
L = ['M','S','T','B','J']
#苯办法
L = [L[0],L[1],L[2]]
#循环
r = []
n = 3
for i in range(n):
    r.append(L[i])
r 
#利用切片
L[0:3]
L[:3]
#扩展使用切片函数
print(L[0:100])
R = list(range(100))
print('R=',R)
print('R[10:20]=',R[10:20])
print('R[-10:]=',R[-10:])
print('R[:10:2]=',R[:10:2])
print('R[::5]=',R[::5])
'abcdef'[:3]#其中【0:3】就是slicefun本身
