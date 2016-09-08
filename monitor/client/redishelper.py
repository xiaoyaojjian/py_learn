#!/usr/bin/env python
# -*- coding: <utf-8> -*-

"""

"""

import redis
import setting


class RedisHelper:
    __conn_info = setting.connection

    def __init__(self):
        self.__conn = redis.Redis(**self.__conn_info)
        self.chan_sub = setting.channel
        self.chan_pub = setting.channel

    def get(self, key):
        return self.__conn.get(key)

    def set(self, key, value):
        self.__conn.set(key, value)

    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub


if __name__ == '__main__':
    red = RedisHelper()
    # red.set('name', 'shiina1')
    # print(red.get('name'))
    red.public('message')

