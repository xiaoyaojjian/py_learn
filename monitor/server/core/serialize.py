#!/usr/bin/env python
# -*- coding: <utf-8> -*-


import pickle, time
from conf.hosts import monitored_groups

    
def config_serializer(client_ip, detail=False):
    """
    依据 client ip 获取, 客户端监控项的监控指标
    :param client_ip: 客户端 ip
    :param detail:
    :return: 客户端个监控项的监控指标
    """
    '''fetch configurations according to provided ip address,client will monitor themselves depending on this configs'''
    applied_services = []
    configs = {
               'services': {},
               }
    for group in monitored_groups:
        for monitor_ip in group.hosts:
            if monitor_ip == client_ip:
                # print('found it :', group.group_name ,group.services)
                applied_services.extend(group.services)  # 根据 client ip 的所在组, 将client 所定义的监控项添加到列表中
    
    applied_services = set(applied_services)  # 去重
    if detail is True:
        return applied_services
    for service_class in applied_services:  # serialize instance to dict
        service_ins = service_class()  # 实例化监控项
        # print(service_ins.name, service_ins.interval,service_ins.plugin_name)
        configs['services'][service_ins.name] = [service_ins.interval, service_ins.plugin_name, 0]  # 将监控项的监控指标添加到 dict 中, 列表最后一项 0 是监控脚本上一次执行时间
        
    return configs


def all_host_configs():
    """
    判断 client ip 在哪些组里, 此函数未使用
    :return:
    """
    configs ={'hosts': {}}
    for group in monitored_groups:
        for host_ip in group.hosts:
            # if not configs['hosts'].has_key(host_ip):
            configs['hosts'][host_ip]= {}

    return configs

    
def get_host_configs(server_instance, msg):
    """
    client 请求后, 将监控指标写入 redis
    :param server_instance:
    :param msg:
    :return:
    """
    ipaddr = msg.get('ip')
    print('get here ...')
    configs = config_serializer(ipaddr)  # 依据 ip 获取监控指标
    server_instance.redis.set(ipaddr, pickle.dumps(configs))  # 将监控指标序列化写入 redis


def report_service_data(server_instance,msg):
    """
    处理订阅的信息, 添加时间戳后写入 redis
    :param server_instance:
    :param msg: 监控脚本返回的监控记录
    :return:
    """
    # print('recv:',msg)
    host_ip = msg['ip']
    service_status_data = msg['data']
    service_name = msg['service_name']
    
    server_instance.hosts['hosts'][host_ip][service_name] ={ 
                    'data':service_status_data,
                    'time_stamp': time.time()
    
                    }
    key = 'StatusData::%s' % host_ip 
    server_instance.redis.set(key, pickle.dumps(server_instance.hosts['hosts'][host_ip]))
    
if __name__ == '__main__':
    # print (config_serializer('10.168.44.3'))
    all_host_configs()