#!/usr/bin/env python
# -*- coding: <utf-8> -*-


import pickle 
from core import serialize


def action_process(server_instance, msg):
    """
    从message 判断消息所要执行的操作, 并执行
    :param server_instance:
    :param msg:
    :return:
    """
    msg = pickle.loads(msg[2])
    print(msg)
    func_name = list(msg.keys())[0]
    func = getattr(serialize, func_name)
    
    func(server_instance, msg[func_name])
   


