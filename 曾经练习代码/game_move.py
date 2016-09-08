import math
'''
定义a fun return 多个值
EG：游戏中经常要从一个点移动另一个点，给出坐标，位移，角度，就可以计算出新的坐标
'''
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny
