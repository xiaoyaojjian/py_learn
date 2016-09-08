#-*-coding:utf-8-*-
# use asyncio coroutine net to connect to collect sina,sohu and 163's HOME
########################## 2 段 program 独立运行即可 ####################################
'''
import asyncio


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP /1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        # Ignore the body close the socket
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
        writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host)
         for host in ['www.sina.com', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
'''
###########################################################
# 利用PY3.5新语法进行执行WGET coroutine
'''
import asyncio


async def wget2(host):
    print('wget %s...' % host)
    connect2 = asyncio.open_connection(host, 80)
    reader2, writer2 = await connect2
    header2 = 'GET / HTTP /1.0\r\nHost: %s\r\n\r\n' % host
    writer2.write(header2.encode('utf-8'))
    await writer2.drain()
    while True:
        line2 = await reader2.readline()
        if line2 == b'\r\n':
            break
        # Ignore the body close the socket
        print('%s header > %s' % (host, line2.decode('utf-8').rstrip()))
        writer2.close()

loop2 = asyncio.get_event_loop()
tasks2 = [wget2(host)
         for host in ['www.sina.com', 'www.sohu.com', 'www.163.com']]
loop2.run_until_complete(asyncio.wait(tasks2))
loop2.close()
'''