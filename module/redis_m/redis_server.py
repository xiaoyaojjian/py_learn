from module.redis_m.redis_helper import RedisHelper


red = RedisHelper()
while True:
    res = red.subscribe()
    print(res.parse_response())
