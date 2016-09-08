# _*_coding:utf-8_*_
# asyncio is to support coroutine IO 异步
# asyncio is a EventLoop program model
########################## 3 段 program 独立运行即可 ####################################
'''
import asyncio

@asyncio.coroutine	# 把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行
def hello():
    print("Hello World!")	#方便地调用另一个generator
    # coroutine IO asyncio.sleep()
    r = yield from asyncio.sleep(1)	# this also be coroutine.directly interrupt and execute next eventloop
    print('Hello Again!')

# collect EvevtLoop
loop = asyncio.get_event_loop()
# execute coroutine
loop.run_until_complete(hello())
loop.close()
'''
###########################################################
#####这段程序亦可执行#####
# 将helloworld 与helloagain一起作为一组tasks 封装一起进行多个协程由同一个线程并发执行
'''
import asyncio
import threading
@asyncio.coroutine
def hello1():
    print("Hello1 World! [%s]" % threading.currentThread())
    # coroutine IO asyncio.sleep()
    r = yield from asyncio.sleep(1)	# this also be coroutine.directly interrupt and execute next eventloop
    print('Hello1 Again! [%s]' % threading.currentThread())

# collect EvevtLoop
loop1 = asyncio.get_event_loop()
tasks = [hello1(),hello1()]
# execute coroutine
loop1.run_until_complete(asyncio.wait(tasks))
loop1.close()
'''
###########################################################
# 利用PY3.5新语法进行执行hellocoroutine
'''
import asyncio
async def hello2():
	print("Hello2 World!")
	r = await asyncio.sleep(1)
	print("Hello2 Again!")
loop2 = asyncio.get_event_loop()
loop2.run_until_complete(hello2())
loop2.close()
'''
