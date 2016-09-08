#_*_coding:utf-8_*_

import os
import sqlite3
db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# init data
    # conn SQLite DB
    # dbfile is test.db
    # if file isn't exist,auto to create
conn = sqlite3.connect(db_file)
# create a Cursor
cursor = conn.cursor()
# execute a SQL sent,create talbe
cursor.execute(
    'create table user(if varchar(20) primary key,name varchar(20), score int)')
# execute 3 SQL sent,insert 3 record
cursor.execute(r"insert into user values ('A-001','Adam',95)")
cursor.execute(r"insert into user values ('A-002','Bart',64)")
cursor.execute(r"insert into user values ('A-003','Caca',78)")
# close Cursor
cursor.close()
# 提交事务
conn.commit()
# close 连接
conn.close()


def get_score_in(low, high):
    # return 指定分数区间 の 名字 按分数从低到高排序
    try:
        # connect to SQLite DB
        conn = sqlite3.connect('test.db')
        # creat a Cursor
        cursor = conn.cursor()
        # execute select sent
        cursor.execute(
            'select name from user where score between ? and ? order by score asc', (low, high))
        # collect select result set
        values = cursor.fetchall()
    finally:
        # close Cursor
        cursor.close()
        conn.close()
    # if result set is empty call select is fail
    if len(values) == 0:
        print(u'select record is fail,it is Empty')
        return None
    else:
        # return result
        return values
# call fun
print(get_score_in(99, 100))
'''
>>> conn = sqlite3.connect('test.db')
>>> cursor = conn.cursor()
>>> cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')
>>> cursor.execute('insert into user (id,name) values (\'1\',\'MA\')')
>>> cursor.rowcount
>>> cursor.close()
>>> conn.commit()
>>> conn.close()
>>> conn = sqlite3.connect('test.db')
>>> cursor = conn.cursor()
>>> cursor.execute('select * from user where id=?','1')
>>> values = cursor.fetchall()
>>> values
'''
