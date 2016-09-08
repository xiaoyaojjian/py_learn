############Regular Expression##############
# Escape（避开） Sequence 转义字符串
# re module
# python の string（本身也有escape）
s = 'ABC\\-001'
# 对应Regular Expression 'ABC\-100'
# 利用r前缀 不用考虑escape问题
s_n = r'ABC\-001'
# 对应Regular Expression 与之相同
import re
re.match(r'^\d{3}\-\d{3,8}$', '010-12345')  # 判断匹配是否成功
re.match(r'^d{3}\-\d{3,8}$', '010 12345')
# match() method 判断是否匹配 若匹配则返回一个object Match 否则返回一个None
test = '用户输入的字符串'
if re.match(r'Regular Expression', test):
    print('yes')
else:
    print('no')
############切分string##############
# 正常切分
str = 'a b  c'
str.split(' ')
# 无法识别连续空格b与c之间
# 正则表达式切分
re.split(r'\s+', str)
# 加入,
re.split(r'[\s\,]+', 'a,b,c  d')
# 加入;
re.split(r'[\s\,\;]+', 'a,b,c;;  d')
# 用户输入一组标签 要利用Regular Expression将不规范的输入转换成正确的数组
# 分组############## 提取子串() is want to 提取 的分组(Group)
# '^(\d{3})-(\d{3,8})$' 分别定义两组 可直接从匹配度string张提取出区号与本地号码
num = '010-12345'
m = re.match('^(\d{3})-(\d{3,8})$', num)
print('原始未分组string:', m.group(0))
print('分组1string:', m.group(1))
print('分组2string:', m.group(2))
# if Regular Expression def group 可利用Match对象中 用group方法提取出子串
# 匹配识别 合法时间 格式
t = '19:27:11'
mt = re.match(
    r'^(0[0-9]|1[0-9]|2[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|6[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|6[0-9]|[0-9])$', t)
mt.groups()
############贪婪匹配##############
# re.match默认是贪婪匹配 匹配尽可能更多字符
# 目的是匹配出 分组出后面的0
re.match(r'^(\d+)(0*)$', '102300').groups()
# 由于\d+采用贪婪匹配 直接将后面0 全部匹配 结果0*只能匹配空字符串
# 则应将\d+采用非贪婪(即尽可能少的去匹配) 处理method：在后面加？既可以非贪婪匹配
re.match(r'^(\d+?)(0*)$', '102300').groups()
###############complies############
'''
在我使用Python RegularExpression re module 内部会:
1 compile regular expression:if regular expression is invalid error
2 use compiled regular expression to macth string
BUT if a regular expression repeat use 几千次 for efficient: 
预编译Regular Expression 不重复1compile 直接跳过 execute 2 match
'''
# compile
re_tel = re.compile(r'^(\d{3})-(\d{3,8})$')
# use it
re_tel.match('010-12345').groups()
# compiled 生成Regular Expression 对象 该对象自己包含饿了Regular Expression
re_tel.match('010-8088').groups()
'''
尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
someone@gmail.com
bill.gates@microsoft.com
版本二可以验证并提取出带名字的Email地址：
<Tom Paris> tom@voyager.org
'''
# Email Address [_a-zA-Z\d\-\./]+@[_a-zA-Z\d\-]+(\.[_a-zA-Z\d\-]+)+ OR [_a-z\d\-\./]+@[_a-z\d\-]+(\.[_a-z\d\-]+)*(\.(info|biz|com|edu|gov|net|am|bz|cn|cx|hk|jp|tw|vc|vn))$
re_email_ver1 = re.compile(r'^[_a-zA-Z\d\-\./]+@[_a-zA-Z\d\-]+(\.[_a-zA-Z\d\-]+)+$')
re_email_ver2 = re.compile(r'^[_a-z\d\-\./]+@[_a-z\d\-]+(\.[_a-z\d\-]+)*(\.(info|biz|com|edu|gov|net|am|bz|cn|cx|hk|jp|tw|vc|vn))$')
re_email_ver1.match('a111@22.aa').groups()
re_email_ver2,match('zlxs@sina.com').groups()