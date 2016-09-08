# _*_ coding:utf-8 _*_
# under multiThread 每个数据都有自己的数据
# 一个Thread使用自己局部变量比全局变量好
# local var vs global var
# local var 只有Thread自己看见 不会影响其他线程 而global var 修改必须加锁
# local var 传递 较为麻烦
from student_class_def import Student


def process_student(name):
    std = Student(name)
    # std is local var.but every fun all use it.so must transport in
    do_task1(std)
    do_task2(std)


def do_task1(std):
    do_subtask1(std)
    do_subtask2(std)


def do_task2(std):
    do_subtask1(std)
    do_subtask2(std)
# 以上函数每层调用 都得传参数std 太麻烦
# 使用global var 亦是不行，会导致每个线程处理不同Student对象，不可共享
# 解决上述多次调用问题
# 将一个全局dict存放所有的Student对象后以Thread自身作为key获得线程对应のStudent对象
import threading
global_dict = {}


def std_thread(name):
    std = Student(name)
    # 将std放到全局变量global_dict中
    global_dict[threading.current_thread()] = std
    do_task3()
    do_task4()


def do_task3():
    # 不许传入std 而是根据当前线程进行查找
    std = global_dict[threading.current_thread()]


def do_task4():
    # 任何函数都可查找出当前线程的std对象
    std = global_dict[threading.current_thread()]
# 理论可行 消除了std对象在每层函数的传递问题 但太麻烦
######################################################
# ThreadLocal 不用查找dict 帮我自动处理
# create global var ThreadLocal object
local_school = threading.local()


def process_student():
    # 获取当前Thread关联的Student
    std = local_school.student
    print('Hello, %s (in %s )' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定Thread的student
    local_school.student = name
    process_student()
t1 = threading.Thread(target=process_thread, args=('Aaaa',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bbbb',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
################################################
'''
全局变量local_school是一个ThreadLocal对象
每个Thread对他都可以读写student属性
但互不影响
你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，
可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
可以理解为全局变量local_school是一个dict，不但可以用local_school.student，
还可以绑定其他变量，如local_school.teacher等等。
ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
一个ThreadLocal变量虽然是全局变量，
但每个线程都只能读写自己线程的独立副本，互不干扰
ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题
'''
###############################################