#!/usr/bin/env python
# -*- coding: <utf-8> -*-

"""
Get CPU's data, need more than a little time
Depend: sysstat
"""

import subprocess


def monitor(frist_invoke=1):
    command = 'sar 1 3| grep "^Average:"'
    result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout = result.stdout.read().decode()
    status = result.stderr.read()
    if status:  # 如果有 status 返回, 将 status 作为 status 返回
        value_dic = {'status': status}
    else:
        value_dic = {}
        user, nice, system, iowait, steal, idle = stdout.split()[2:]  # 读取 stdout 赋值, 需要 decode()
        value_dic = {
            'user': user,
            'nice': nice,
            'system': system,
            'iowait': iowait,
            'steal': steal,
            'idle': idle,
            'status': status
        }
    print(value_dic)
    # return value_dic

    # test
    return {'nice': '0.00', 'steal': '0.00', 'iowait': '0.00', 'status': '', 'system': '0.00', 'idle': '100.00', 'user': '0.00'}
