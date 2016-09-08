#!/usr/bin/env python
# -*- coding: <utf-8> -*-


from redishelper import RedisHelper
from core import serialize

from core import action_process


class MonitorServer(object):
    def __init__(self, ip, port):
        self.ip = ip 
        self.port = port 
        self.hosts = serialize.all_host_configs()
        self.redis = RedisHelper()

    def handle(self):
        redis_sub = self.redis.subscribe()
        redis_sub.parse_response()
        while True:
            msg = redis_sub.parse_response()
            # print('recv:', msg)
            action_process.action_process(self, msg)  # 传入 self 实例本身, 和订阅的数据
            print('----waiting for new msg ---')
            
            # received data
            for host, val in self.hosts['hosts'].items():
                print(host, val)
    
    def run(self):
        print('----starting monitor server----')
        self.handle() 
    
    def process(self):
        pass 
            
