"""
A manager object returned by Manager() controls a server process which holds Python objects and allows other processes
to manipulate them using proxies.

Manager 可以支持更多数据结构的共享, 甚至可以通过网络在不同的设备上共享,
但是他比 Array,Value 这种 内存共享(shared memory)要慢
"""

from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=f, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)