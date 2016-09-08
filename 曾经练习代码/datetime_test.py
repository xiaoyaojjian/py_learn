# _*_coding:utf-8_*_
# datetime is python process date and time standrad library
from datetime import datetime
# collect 当前 date time
now = datetime.now()
print(now)
print(type(now))
# datetime is module include a class datetime
# collect 指定 date time
dt = datetime(2015, 4, 19, 12, 34, 11)  # defult format
# datetime toto timestamp 时间戳
# epoch time = 1970 1 1 00:00:00 UTC
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
# beijing_timestamp = 0 = 1970-1-1 00:00:00 UTC+8:00
stampdt = datetime.now()
stampdt.timestamp()  # 将datetime转换为timestamp float 秒数.毫米数
timedt = stampdt.timestamp()
datetime.fromtimestamp(timedt)  # 无时区概念 datetime有时区（与本地时间 os 做转换）UTC8:00
datetime.utcfromtimestamp(timedt)  # 直接转换到UTC标准时区时间（GMT）UTC0:00
# string to datetime
cuday = datetime.strptime(
    '2015-12-21 21:34:19', '%Y-%m-%d %H:%M:%S')  # 此时datetime无时区信息
print(cuday)
# datetime to string
print(now.strftime('%a, %b %d %H:%M'))  # 格式化string
# datetime plus minus
from datetime import timedelta
now
now + timedelta(hours=10)
now - timedelta(days=1)
now + timedelta(hours=12, days=2)  # parameter 无顺序
# local time 北京时间UTC8:00 to UTC timeUTC0:00
# use type datetime timezone attribute tzinfo == None(defult) 强行执之一个timezone
from datetime import timezone
tz_bj = timezone(timedelta(hours=8))  # create timezone UTC800
now
nowdt = now.replace(tzinfo=tz_bj)  # 强行设置为UTC800
nowdt
# time zone transform
# by utcnow 获得当前UTC时间 在转换到任意时区时间
# collect UTC time 强制设置zone为UTC000
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('当前协调世界时间UTC0:00:', utc_dt)
# astimezone()将转换时区为北京
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('北京时区时间UTC8:00:', bj_dt)
# astimezone()将转换时区为东京
dj_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print('东京时区时间UTC9:00:', dj_dt)
# 不是必须从UTC+0:00时区转换到其他时区，任何带 时区 的datetime都可以正确转换
# astimezone()将北京时间转换为东京时区
bj2dj = bj_dt.astimezone(timezone(timedelta(hours=9)))
print('北京UTC8:00转换东京时间UTC9:00:', bj2dj)
# the key of time zone transform:拿到一个datetime时，应获知其正确时区 后强行设置时区 作为基准时间
# 利用带时区的datetime by astimezone方法 可转换到任意时区
# 根据timedelta(hours=X)转换
# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关
##################################3333333
# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta


def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S') # 此时dt无timezone信息
    tz = int(re.match(r'^UTC[+-](\d):00$',tz_str).group(1)) # 取出timezone参数
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    tz_dt = utc_dt.astimezone(timezone(timedelta(hours=tz)))
    print(tz_dt.timestamp())
'''
假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，
以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp
'''