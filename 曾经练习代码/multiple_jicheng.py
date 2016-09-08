#实现多重继承
########################
#哺乳类and鸟类
class Animal(object):
    pass
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
#各种动物
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass
########################
#奔跑类and飞翔类（功能）
class Runnable(object):
    def run(self):
        print('Running...')
class Flyable(object):
    def fly(self):
        print('Flying...')
#添加所需功能
class Dogg(Mammal,Runnable):
    pass
class Batt(Mammal,Flyable):
    pass
########################
#“混入” 通过多重继承
#让Ostrich除了继承Bird还要有Runnable，这种设计是指MixIn
#for 更好看出继承关系将Runnable改为RunnableMixIn以示区别：这是混进来的，多了
class RunnableMixIn(object):
    def run(self):
        print('Running...')
class Ostrichh(Bird,RunnableMixIn):
    pass
'''
##########
####python库中很多利用MixIn
###Python自带TCPSever and UDPSever 两类网络服务
##需同时服务很多用户即必须使用
#多进程 (ForkingMixIn)or 多线程(ThreadingMixIn)
#编写一个多进程模式 TCP 服务
class MyTCPSever(TCPSever,ForkingMixIn):
    pass
#编写一个多线程模式 UDP 服务
class MyUDPSever(UDPSever,ThreadingMixIn):
    pass
#编写一个更先进 协程模型 添加 CoroutineMixIn
class MyTCPSever(TCPSever,CoroutineMixIn):
    pass
########################
#由于PYthon可允许多重继承，于是，MixIn是一种常见模式（设计）
#只要选择组合不同的类的功能 即可快速构造所需的子类
'''
