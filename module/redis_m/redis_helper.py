import redis


class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host='103.11.64.44',)
        self.chan_sub = 'nu1'
        self.chan_pub = 'nu1'

    def get(self, key):
        return self.__conn.get(key)

    def set(self, key, value):
        self.__conn.set(key, value)

    # 发信息
    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)

    # 取信息
    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)

        pub.parse_response()
        return pub


if __name__ == '__main__':
    red = RedisHelper()
    red.public('shiina')