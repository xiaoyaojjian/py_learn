#!/usr/bin/env python
# -*- coding: <utf-8> -*-

import pickle
from redishelper import RedisHelper
import time
import sys
import threading
from plugins import plugin_api

client_ip = '192.168.1.11'


class MonitorClient(object):
    def __init__(self, server, port):
        self.server = server
        self.port = port
        self.configs = {}
        self.lock = threading.Lock()
        self.redis = RedisHelper()

    def format_msg(self, key, value):
        """
        将 message 序列化
        :param key:
        :param value:
        :return:
        """
        msg = {key: value}
        return pickle.dumps(msg)

    def get_configs(self):
        """
        向 server 发送 client ip 获取 监控指标
        :return:
        """
        msg = self.format_msg('get_host_configs', {'ip': client_ip})

        print('-----get host monitor configs----')  # ,msg
        redis_pub = self.redis.public(msg)

        count = 1
        while count < 30:  # 重复30 次, 从 redis 中获取 client 的监控指标数据
            configs = self.redis.get(client_ip)
            if configs:
                # print configs
                return pickle.loads(configs)
            else:
                count += 1
                time.sleep(1)
        sys.exit('Error:could not get client monitor configurations!')

    def handle(self):
        """
        循环处理
        :return:
        """
        self.configs = self.get_configs()
        if self.configs['services']:
            print('--going to monitor ---', self.configs)
            # {'services': {'linux_memory': [30, 'get_memory_info', 0], 'linux_cpu': [30, 'get_cpu_status', 0]}}
            while True:  # 依据监控指标进行循环执行脚本
                for service_name, val in self.configs['services'].items():
                    interval, plugin_name, last_check = val
                    next_run_time = interval - (time.time() - last_check)
                    if time.time() - last_check >= interval:
                        print('service\033[32;1m%s\033[0m has reached monitor interval' % service_name)
                        t = threading.Thread(target=self.task_run, args=[service_name, plugin_name, ])
                        t.start()
                        self.configs['services'][service_name][2] = time.time()
                    else:
                        print('service\033[34;1m%s\033[0m next run time is \033[34;1m%s\033[0m seconds later' % (service_name, next_run_time))
                        time.sleep(1)
                        # print self.configs
        else:
            print('---nothing to monitor,configs dict is empty---')

    def task_run(self, service_name, plugin_name):
        """
        执行监控脚本, 向 redis 发布数据
        :param service_name:
        :param plugin_name:
        :return:
        """
        plugin_func = getattr(plugin_api, plugin_name)
        result = plugin_func()
        msg = self.format_msg('report_service_data',
                              {'ip': client_ip,
                               'service_name': service_name,
                               'data': result,
                               })
        self.redis.public(msg)

    def run(self):
        self.handle()


if __name__ == '__main__':
    c = MonitorClient('192.168.1.11', '3333')
    c.run()