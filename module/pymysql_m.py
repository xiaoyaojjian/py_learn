"""
Mysql 数据库操作模块
"""

import pymysql.cursors

# 建立连接
connection = pymysql.connect(host='127.0.0.1',
                             user='root', password='',
                             db='test',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    cursor = connection.cursor()

    # 执行 SQL 语句, 插入数据
    res1 = cursor.execute('insert courses (name,passwd) values ("shiina","123456")')

    # 查询数据
    res2 = cursor.execute('select * from courses')

    # 获取查询结果
    data = cursor.fetchall()

    # 执行 SQL 方法二
    sql = 'delete from courses where passwd = %s'
    params = ('123456')
    res3 = cursor.execute(sql,params)

    # 有数据改动的话, 需要执行 commit
    connection.commit()

finally:
    # 关闭连接
    connection.close()

print(data)
print(res1, res2)
