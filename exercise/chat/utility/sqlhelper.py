"""
数据库操作模块
"""

import pymysql

from config import db_conf


class SqlHelper(object):
    __db_conf = db_conf

    def __init__(self):
         pass

    # execute sql inquire fetchone
    def sql_fetchone(self, sql, param):
        conn = pymysql.connect(**SqlHelper.__db_conf)
        try:
            cursor = conn.cursor()
            cursor.execute(sql, param)
            data = cursor.fetchone()
            return data
        finally:
            conn.close()

    # execute sql inquire fetchall
    def sql_fetchall(self, sql, param):
        conn = pymysql.connect(**SqlHelper.__db_conf)
        try:
            cursor = conn.cursor()
            cursor.execute(sql, param)
            data = cursor.fetchall()
            return data
        finally:
            conn.close()

    def sql_exec(self, sql, param):
        conn = pymysql.connect(**SqlHelper.__db_conf)
        try:
            cursor = conn.cursor()
            cursor.execute(sql, param)
            data = cursor.fetchall()
            conn.commit()
            return data
        finally:
            conn.close()


# helper = SqlHelper()
# sql = 'select user_id,username from user WHERE username=%s AND password=%s'
# param = ('shiina', 'shiina')
# res = helper.sql_fetchone(sql, param)
# print(res)

