# 分布式进程
# 在Thread and Process 优选 Process 更稳定 可将分布到多台机器上 Thread 最多能分布到一台机器
# 利用multiprocess中のmanagers子模块支持多进程分布
# 一个服务进程作为调度者将任务分布到其他多个进程 通过网络通信
'''
如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行
现在，由于处理任务的进程任务繁重
希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现
原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去
就可以让其他机器的进程访问Queue了
'''
##############################################################
#讲一下两个master与worker分别在两个文件运行，在前者运行成功后调用后者即可
##############################################################
# 1 我们先看服务进程，服务进程负责启动Queue，把Queue注册到网络上 然后往Queue里面写入任务
import random
import time
import queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support  # Win7添加
# send task's queue
task_queue = queue.Queue()
# receive result's queue
result_queue = queue.Queue()
# from BaseManager 继承のQueueManager


class QueueManager(BaseManager):
    pass
# 将两个queue都注册到网上 callable 参数关联Queue对象
'''
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
'''


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


def test():
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
# 绑定port5000.设置密码'abc'
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
# start queue
    manager.start()
# by network call Queue object
    task = manager.get_task_queue()
    result = manager.get_result_queue()
# 放几个任务进去(写入任务)
    print('Put task...')
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
# 读取Result队列中队伍结果
    print('Try get result...')
    for i in range(10):
        r = result.get(timeout=10)
    print('Result: %s' % r)
# close
    manager.shutdown()
    print('master exit...')
if __name__ == '__main__':
    freeze_support()
    test()
##################################################
# 2 在另台机器上启动任务进程（本机也可）
import time
import sys
import queue
from multiprocessing.managers import BaseManager
# create similar QueueManager


class QueueManager(BaseManager):
    pass
# 由于这个QueueManager只从网络获取Queue so注册时只提供name
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
# link network server 即运行本机
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# port name and authkey 注意保持一致
ma = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# form net link
ma.connect()
# 获取Queue对象
task = ma.get_task_queue()
result = ma.get_result_queue()
# from task queue get task,return result to result queue
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('Run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty')
# process is over
print('worker exit...')
