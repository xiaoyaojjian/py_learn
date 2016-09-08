#定义function my_abs 取绝对值
def my_abs(x):
    if x>0:
        return x
    else:
        return -x
#定义function nop 什么也不做作占位符
def nop():
    pass

#修改my_abs()添加参数检查
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if x >=0:
        return x
    else:
        return -x
'''
添加参数检查后，若传入错误的参数类型，函数就抛出 错误提示：
TypeError：bad operand type
'''
