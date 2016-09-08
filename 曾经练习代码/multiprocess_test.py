# 在cmd模式下进行调用
# 为给Python程序实现multiprocessing
import os
print('Process (%s) start ...' % os.getpid())
# Only works on Unix Linux Mac
'''
Windows 没有fork调用 以下代码无法winos调用
pid = os.fork()#pid = process ID(Identification)
# 操作系统里指进程识别号，也就是进程标识符
# 操作系统里每打开一个程序都会创建一个进程ID，即PID
if pid == 0:
	print('I am child process (%s) and my parent is %s' %
	      (os.getpid(),os.getpid()))
else:
	print('I (%s) just created a child process (%s)' % (os.getpid(),pid))
'''
# 为了实现在windows下使用Python编写多进程程序
from multiprocessing import Process
# child process


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end')
# 创建子程序时，只需要传入一个执行函数和函数的参数（目标）target
# 创建一个Process实例，用start方法启动，比fork更简单,join方法可等待子进程结束后再继续往下运行通常用于进程间的同步
######################################################################
# 若要启动大量子进程可用进程池的方式批量创建child process
from multiprocessing import Pool
import os
import time
import random


def long_time_task(name):
	print('Run task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds' % (name, (end - start)))
if __name__ == '__main__':
	print('Parent process %s ' % osl.getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print('Waiting for all subprocess done...')  # 根据CPU数进行等待
	p.close()
	p.join()
	print('All subprocess done...')
# Pool对象调用join方法会等待所有child process执行完毕
# 调用join之前需先调用close 调用clos后就不可添加新的process
# 由输出结果task 0 1 2 3是即刻进行而task 4要等待前面某个task完成后才执行
# Pool默认大小是根据cpu核数 由以上Pool(4)可知有意限制，isn't os limit or Pool(5)可同时跑5个进程
####################################################################
# 子进程有时会是外部进程 建立subprocess,还需要控制其IO--subprocess
import subprocess
print('$ nslookup www.sohu.com')  # name server lookup域名查询
r = subprocess.call(['nslookup', 'www.sohu.com'])
print('Exit code', r)
# 若subprocess还有输入 则可通过communicate方法input
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE])
output, err = p.communicate(b'set q = mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
######################################################################
# process 间通信
# os提供很多进制来实现进程间通信Python提供queue pipes来交换数据
# Queue create 2 subprocesses in parent process 1 往queue中写数据，一个从queue中读数据
import Queue
# write data-process
def write(q):
	print('Process to write: %s' % os.getpid())
	for value in ['a', 'b', 'c']:
		s = time.time()
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())
		e = time.time()
		print('Put %s needs %0.2f seconds...' % (value, (e-s)))
# read data-process
def read(q):
	print('Process to read: %s' % os.getpid())
	while True:
		s = time.time()
		value = q.get(True)
		print('Get %s from queue...' % value)
		e = time.time()
		print('Get %s needs %0.2f seconds...' % (value, (e-s)))
if __name__ == '__main__':
	# parent process create Queue and transport to every subproess
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	# start subprocess pw,write:
	pw.start()
	# start subprocess pr,read:
	pr.start()
	# wait pw end:
	pw.join()
	# pr is a dead loop cant wait it end only must stop:
	pr.terminate()
#####################以上程序分别在cmd模式下调用#################################
'''
在Unix,Linux下multiprocess模块封装fork调用 使之不需要关注fork细节
windows 下无fork multiprocessing需要模拟出fork效果
父进程所有Python对象必须通过pickle序列化再传到子程序
若multiprcoess在windows下调用失败 考虑是否是pickle失败
'''
