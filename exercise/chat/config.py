"""
数据库配置文件
"""

import pymysql
db_conf = dict(host='127.0.0.1',
               user='root',
               password='',
               db='chat',
               cursorclass=pymysql.cursors.DictCursor)
