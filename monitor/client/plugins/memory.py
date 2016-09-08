#!/usr/bin/env python
# -*- coding: <utf-8> -*-

"""
Get memory's data
"""

import subprocess


def monitor(frist_invoke=1):
    command = "grep 'MemTotal\|MemFree\|Buffers\|^Cached\|SwapTotal\|SwapFree' /proc/meminfo"
    result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout = result.stdout.read().decode()
    status = result.stderr.read()
    monitor_dic = {
        'SwapUsage': 'percentage',
        'MemUsage': 'percentage',
    }

    if status:  #cmd exec error
        value_dic = {'status': status}
    else:
        value_dic = {'status': status}
        for i in stdout.split('kB\n'):
            if not i:  # 使用 kB\n 分割为列表, 会报 IndexError: list index out of range, 因为最后还有一个 '' 空行
                break
            key = i.split()[0].strip(':')  # factor name
            value = i.split()[1]   # factor value
            value_dic[key] = value
            print(value_dic)

        if monitor_dic['SwapUsage'] == 'percentage':
            value_dic['SwapUsage_p'] = str(100 - int(value_dic['SwapFree']) * 100 / int(value_dic['SwapTotal']))
        #real SwapUsage value
        value_dic['SwapUsage'] = int(value_dic['SwapTotal']) - int(value_dic['SwapFree'])

        MemUsage = int(value_dic['MemTotal']) - (int(value_dic['MemFree']) + int(value_dic['Buffers'])  + int(value_dic['Cached']))
        if monitor_dic['MemUsage'] == 'percentage':
            value_dic['MemUsage_p'] = str(int(MemUsage) * 100 / int(value_dic['MemTotal']))
        #real MemUsage value
        value_dic['MemUsage'] = MemUsage
    # return value_dic

    # tset
    return {'SwapTotal': '976892', 'MemUsage': 66848, 'SwapFree': '976892', 'MemFree': '1776264', 'SwapUsage': 0, 'status': '', 'MemUsage_p': '3.262972718096105', 'Buffers': '18324', 'SwapUsage_p': '0.0', 'MemTotal': '2048684', 'Cached': '187248'}

