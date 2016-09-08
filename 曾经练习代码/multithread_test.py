# multithread多线程 多任务可由multiprocess完成亦可由一个进程完成（多线程）
# 由于线程是os直接支持の执行单元 于是高级语言通常内置多线程支持
# Pythonの线程是POSIX Thread 而不是模拟出来的（有别于process）
# start a thread 即 把一个函数传入同时创建Thread实例后调用start()
import time
import threading
# new thread execute


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)
'''
任何进程默认启动一个线程--主线程by it 可启动new Thread
Python模块下threading有个current_thread方法永远返回当前线程的实例
主线程实例的名字叫MainThread，subthread在创建时指定名字以LoopTread来命名
名字仅仅在打印时用来显示（完全无意义）
if 不去起名字Python自动会给线程命名Thread-1 Thread-2 Thread-3.....
'''
'''
multithread and multiprocess 最大不同是
multiprocess下，同一变量各自有一份拷贝存在于每个进程 互不影响
multithread下，所有变量都有所有线程共享 so 任何一个变量都可被任何一个线程修改(dangerous)
'''
# LOCK
# test multithread 同时操作 a var 修改 导致 数据不一致性
# assume this is your bank 存款
balace = 0


def change_it(n):
        # 先存后取 结果为零
    global balace  # 定义共享变量
    balace = balace + n
    balace = balace - n


def run_thread(n):
    for i in range(100000):
        change_it(n)
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balace)
# 究其原因，修改balance 需要修改多条语句 execute 这几条指令 Thread可能会中断
# 导致多个线程将同一个对象的内容改乱了（DBMS 并发控制 ）t1与t2交替进行
# 并发控制－－一级封锁协议
# 创建一个锁通过threading.Lock()实现
balace = 0
lock = threading.Lock()


def run_thread(n):
    for i in range(100000):
        # 先要获取锁
        lock.acquire()
        try:
            print('放心の修改吧...')
        finally:
            print('改完了一定哟啊释放锁...')
            lock.release()
# 当多个线程同时executelock.acquire 只有一个线程能成功获取锁，然后执行代码其他线程就等着
# 获得锁用完该数据后一定要释放锁，否则形成死锁
#############我竟然是是双核#############
# 死循环
'''
import threading
import multiprocessing


def looping():
    x = 0
    while True:
        x = x ^ 1
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=looping)
    t.start()
# 这尼玛还真的会跑跑跑啊
'''
# exist GIL == global interpreter lock 全局(共享) 解释器 锁
# Python虽然不能利用多线程实现多核任务
# 但可以通过多进程实现多核任务,多个Python进程有各自独立的GIL锁，互不影响
# Python解释器 由于设计时有GIL全局锁 导致多线程无法利用多核
# multithread parallel is a beautiful dream in Python