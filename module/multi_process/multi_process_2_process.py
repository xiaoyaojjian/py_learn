"""
多进程
"""

from multiprocessing import Process
import os
import time


def fun(name):
    info(name)
    time.sleep(1)
    print('say hi', name)


def info(title):
    print(title, 'module name:', __name__)
    print(title, 'parent process:', os.getppid())
    print(title, 'process id:', os.getpid())


if __name__ == '__main__':
    info('main line')
    for i in range(3):
        p = Process(target=fun, args=(i,))
        p.start()
