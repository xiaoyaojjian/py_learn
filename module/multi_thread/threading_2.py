from threading import Thread
import time


def pt():
    for item in range(10):
        time.sleep(1)
        print(item)


t1 = Thread(target=pt,)

t1.start()
t1.join(5)  # 设置 timeout = 5, 在此超时时间内主进程不执行

print('finally')
