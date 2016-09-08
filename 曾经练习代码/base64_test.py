# _*_coding:utf-8_*_
# Base64 binary to string
# is a way of 用64个字符来表示任意二进制数据
'''
binary(3bytes) -->> string(4bytes)
'''

import base64
base64.b64encode(b'binary to string')
base64.b64decode(b'YmluYXJ5IHRvIHN0cmluZw==')
# 由于标准の Base64 encode 后会出现char + or / 在URL中就不可以直接作为参数
# so 有种'url safe' の base64 encode 其实将char + or - 替换成char - or  _
base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
base64.urlsafe_b64decode('abcd--___')
# 还可自定义BAse64编码(无必要)
# 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义
# 所以，很多Base64编码后会把=去掉
# 可以处理去掉=的base64解码函数
# judge s 多长
# 若是4的倍数直接解码
# 取其余数判断还差多少是4的倍数 添够 再解码
import base64


def re_eq_base64_decode(s):
    re_eq_length = len(s) % 4
    if re_eq_length == 0:
        return base64.b64decode(s)
    if re_eq_length == 1:
        s += '='
        return base64.b64decode(s)
    if re_eq_length == 2:
        s += '=='
        return base64.b64decode(s)
