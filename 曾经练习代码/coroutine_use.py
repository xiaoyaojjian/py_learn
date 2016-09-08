'''
Resume the execution and 'send' a value into the generator fun
the value argument becomes the result of the current yield expression
the send() method return the value yield by the generator
OR raises StopIteration if the generator exits without yield another value
when send() is called to start the generator if must be called with None the argument
because there is no yield expression that could receive the value.
'''
def consumer():
    r = ''
    while True:
    	  # because there is unlimited looping
        # so 从send(None) start 每次yield返回值结汇停止于此
        #值为send(msg)传递的msg，返回的为r的值，第一次send(None)时，yield直接返回r值后，便停止于此
        n = yield r # this is a expression
        if not n:
        	#此处的判断条件其实一次都没有True过，也就是里面的代码没有被执行过：
    # 因为第一次调用send(None)时，在yield处直接返回等待下一次的send()调用了，返回的值为r=''，其后n的值分别为1~5：
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK' + r

def produce(c):
    c.send(None)	# this is a standard
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
         #此处c.send(n)在传递完n的值后，每次都返回(yield r)的值，也就是r的值
        r = c.send(n)
        print('[PRODUCER] Consumer Return: %s.' % r)
    c.close()
c = consumer()
produce(c)
