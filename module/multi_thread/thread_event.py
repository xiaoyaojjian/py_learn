"""
事件驱动
"""


import threading
import time


def producer():
    print('chef: 等人买')
    event.wait()
    event.clear()
    print('chef: person is coming for cook')
    print('chef: make a cook')
    time.sleep(3)

    print('chef: you cook is ok')
    event.set()

def consumer():
    print('ao: go to buy a cook')
    event.set()
    time.sleep(1)
    print('ao: waiting a cook')
    event.wait()
    print('ao: Thanks')

event = threading.Event()

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)

p.start()
c.start()