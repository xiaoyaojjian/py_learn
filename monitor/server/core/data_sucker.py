#!/usr/bin/env python
# -*- coding: <utf-8> -*-


import serialize
import pickle
from redishelper import RedisHelper

class sucker(object):
    def __init__(self):
        self.hosts = serialize.all_host_configs()
        self.redis = RedisHelper()
    
    def handle(self):
        for host_ip,v in self.hosts['hosts'].items():
            self.hosts['hosts'][host_ip]['configs'] =  serialize.config_serializer(host_ip,detail=True)
            print(host_ip,v)
            print('status data:',self.pull_host_data(host_ip))
    def pull_host_data(self,ip):
        key = 'StatusData::%s' % ip 
        data =self.redis.get(key)
        if data:
            return pickle.loads(data)
if __name__ == '__main__':
    t = sucker()
    t.handle()