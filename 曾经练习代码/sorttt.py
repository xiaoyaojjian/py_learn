t1 = [3,5,1,24,22,334,55]
t2 =({2:'A',5:'B',3:'C',4:'D'})
s1 = sorted('This is A BBB sin(x)'.split(), key=str.lower)
#一组tuple表示学生名字和成绩
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#对上述列表分别按名字排序
L1 = sorted(L)
lo=[]
for l in L:
    lo.append(l[1])
#按成绩从高到低排序
#L2 = sorted(L,key=L[::][1])
lo=sorted(lo)
#按成绩从高到低排序
#L2 = sorted(L,key=L[::][1])
