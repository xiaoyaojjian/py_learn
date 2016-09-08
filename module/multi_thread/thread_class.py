"""
继承 Thread class 实现多线程
"""

from threading import Thread

class MyThread(Thread):

    def run(self):
        print('I am run()')
        Thread.run(self)

def fun():
    print('I am fun()')

tt = MyThread(target=fun)

tt.start()
