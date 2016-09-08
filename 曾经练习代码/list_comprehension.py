#_*_ coding: utf-8 _*_

#List Comprahension列表生成式
#生成list[1,2,3,4,5,6,7,8,9,10]
list(range(1,11))
#生成[1x1, 2x2, 3x3, ..., 10x10]
L = []
for x in range(1,1):
    L.append(x*x)
L
#过于繁琐，利用list comprehension
[x * x for x in range(1,11)]
[x * x for x in range(1,11) if x%2==0] 
[m + n for m in 'ABC' for n in 'DEF' ]
#利用 list comprehension 列出当前目录所用文件和目录名
import os
#os.listdir可列出文件and目录单引号里可以调用任意路径下(仅仅是下一目录下)
[d for d in os.listdir('.')]#这里の . 是指当前环境路径
#同是迭代key value
d = {'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,'=',v)
#利用list comp
[k + '=' + v for k,v in d.items()]
#可将变换大小写
L = ['Aa','Bb','Cc','Dd']
[s.lower() for s in L]
[s.upper() for s in L]
#if list include string or int isn't non_str 上述列表生成会报错
L1 = ['Apple',18,'StudenT','World',None]
#利用isinstance判断是否为string if 满足则执行
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)
