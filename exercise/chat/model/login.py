"""
用户登录验证模块
"""

from utility.sqlhelper import SqlHelper


def login_chack(username, password):

    helper = SqlHelper()
    sql = 'select user_id,username from user WHERE username=%s AND password=%s'
    param = (username, password)
    data = helper.sql_fetchone(sql, param)
    if not data:
        return False
    else:
        return data['user_id']

# login_chack('shiina', 'shiina')