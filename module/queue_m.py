from queue import Queue

que = Queue(10)

print(que.qsize())
que.put('1')
que.put('2')
print(que.qsize())
print('Get:', que.get())
print('Get:', que.get())
print('Get:', que.get())