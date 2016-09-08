"""
使用 multiprocessing 中的 Queue 队列, 实现进程间数据共享
"""

from multiprocessing import Process, Queue


def fun(q, n):
    q.put(['hi, ', n])

if __name__ == '__main__':
    q = Queue()
    q.put('Ao')

    for i in range(5):
        p = Process(target=fun, args=(q, i))
        p.start()

    while True:
        print(q.get())