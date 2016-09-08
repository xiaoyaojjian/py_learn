#-*-coding:utf-8-*-
__author__ = 'zlxs'
'''
day 2:asyc web application
'''
# by aiohttp make a based app.py
import logging
logging.basicConfig(level=logging.INFO)
import asyncio
import os
import json
import time
from datetime import datetime
from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1',9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
#Only one usage of each socket address (protocol/network address/port) is normally permitted
#port = 9000可能正在被占用