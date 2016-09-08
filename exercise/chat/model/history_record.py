"""
历史记录模块
"""

from utility.sqlhelper import SqlHelper
import time


class HistoryRecord(object):
    def __init__(self, user_id):
        self.__user_id = user_id

    def write_record(self, message):

        write = SqlHelper()
        sql = 'insert into record (user_id, date, time, message) VALUES (%s,%s,%s,%s)'
        param = (self.__user_id,
                 time.strftime("%Y-%m-%d", time.gmtime()),
                 time.strftime("%H:%M:%S", time.gmtime()),
                 message
                 )
        write.sql_exec(sql, param)

'''
shiina = HistoryRecord(1)
shiina.write_record('asdfsdf')
'''