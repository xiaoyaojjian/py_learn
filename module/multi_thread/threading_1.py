from threading import Thread
import time


def fun(arg,sleep_time):
    time.sleep(sleep_time)
    print(arg)

# 实例化一个线程
t1 = Thread(target=fun, args=('Thread 1', 1))
t2 = Thread(target=fun, args=('Thread 2', 0))

# 修改,查看线程名
t1.setName('th001')
print('thread name: ', t1.getName())

# 查看,并设置 t1 为守护线程 --> 当主线程结束后, 一起结束
print(t1.isDaemon())
t1.setDaemon(True)
print(t1.isDaemon())

# 启动线程
t1.start()
t2.start()

print('finally')
