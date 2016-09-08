"""
多线程线程安全锁
"""


import threading
import time

numb = 0

# 三种不同类型的锁
lock = threading.Lock()  # 实例化 lock
# lock = threading.RLock()  # recursion --> 递归锁, 可以锁多次, 避免死锁状况
# lock = threading.BoundedSemaphore(5)  # 同时允许几个线程同时获得锁


def plus():
    global numb
    lock.acquire()  # 获得锁
    numb += 1
    time.sleep(0.01)  # sleep 之后, 线程之间会发生抢夺
    print(numb)
    lock.release()  # 释放锁

for i in range(100):
    temp = threading.Thread(target=plus)
    temp.start()
