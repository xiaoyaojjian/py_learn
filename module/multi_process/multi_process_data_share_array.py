"""
多进程数据共享, 使用特殊的数据结构 array
"""


from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)  # 'd' --> double
    arr = Array('i', range(10))  # 'i' --> integer

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])  # 打印时使用 : , 否则会打印这个对象

