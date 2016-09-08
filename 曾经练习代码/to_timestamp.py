# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta


def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S') # 此时dt无timezone信息
    tz = int(re.match(r'^UTC[+-](\d):00$',tz_str).group(1)) # 取出timezone参数
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    tz_dt = utc_dt.astimezone(timezone(timedelta(hours=tz)))
    print(tz_dt.timestamp())
