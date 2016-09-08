#!/usr/bin/env python
# -*- coding: <utf-8> -*-

"""
Get  load's data
"""

import subprocess


def monitor():
    command = 'uptime'
    result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout = result.stdout.read().decode()
    status = result.stderr.read().decode()
    if status:  # 如果有 status 返回, 将 status 作为 status 返回
        value_dic = {'status': status}
    else:
        value_dic = {}
        uptime = stdout.split(',')[:1][0]
        load1, load5, load15 = stdout.split('load average:')[1].split(',')
        value_dic = {
            'uptime': uptime,
            'load1': load1,
            'load5': load5,
            'load15': load15,
            'status': status
        }
    # return value_dic

    # test
    return {'load5': ' 0.01', 'load15': ' 0.02\n', 'uptime': ' 03:43:07 up 10 min', 'load1': ' 0.00', 'status': ''}

