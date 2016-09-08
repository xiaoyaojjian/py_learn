#define fun 公式求解一元二次方程
import math
def quadratic(a,b,c):
    if not isinstance(a|b|c,(int,float)):
        raise TypeError("bad operand type")
    d = b*b-4*a*c
    if d>0:
        return (-b+math.sqrt(d))/(2*a),(-b-math.sqrt(d))/(2*a)
    elif d<0:
        return
        print('超出实数范围!')
    else:
        return -b/(2*a)
