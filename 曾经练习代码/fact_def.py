#利用递归计算阶乘
def fact(n):
    return fact_iter(1,1,n)
#防止出现栈溢出_通过尾递归优化（循环）两者相互等价
def fact_iter(product,count,max):
    if count>max:
        return product
    return fact_iter(product*count,count+1,max)
#然而，并没有什么卵用，pyhton仍然是无法进行尾递归，靠！可利用decorater @tail_call_optimized

