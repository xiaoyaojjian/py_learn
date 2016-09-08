# create a HTTP Server
# handle URLs
# 1 /-HOME return '<h1>Index</h1>'
# 2 /hello/{name}-according to URL argument return text "hello,%s"
# -*-coding:utf-8-*-
import asyncio
from aiohttp import web
async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello,%s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init(loop):  # also initialize fun is a coroutine
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    # by asyncio to create TCP Server
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000')
    return srv
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
# 在地址栏里输入 http://127.0.0.1:8000即可显示Index  http://127.0.0.1:8000/hello/zlxs即可显示hello zlxs