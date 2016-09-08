"""
进程池什么的
"""

from multiprocessing import Pool
import time


def fang(n):
    time.sleep(1)
    print(n*n)

if __name__ == '__main__':
    p = Pool(2)  # 定义进程池内的进程数
    res_list = []
    for i in range(10):
        res = p.apply_async(fang, (i,))  # apply_async 异步模式, 使用 apply 将会变成串行
        print('%s apply ok.'% i)
        res_list.append(res)
    for item in res_list:
        item.get()

    # 诡异的写法, 但是 get 的 timeout 会报错
    # res.get()  # 这句和上面3句的效果是一样的, 不需要创建res_list 也可以执行?
    # get() 将会在这里等待返回结果, question: 为什么 res 没有被循环覆盖, 和教学里不大一样啊


    # 上面所有的的 --> 另一种写法
    # li = range(1, 10)
    # p.map(fang, li)
