import re
s = 'asd21234asdf5645'

# 从字符串首部开始查找
m = re.match('asd',s)
print(m.group())

# 从左向右开始匹配, 只匹配一次
m = re.search('23',s)
print(m.group())

# 匹配所有符合条件的内容组成的列表
m = re.findall('[0-9]+',s)
print(m)

# 找到匹配项, 并替换为指定字符串
m = re.sub('234','kkkkk',s)
print(m)

# 先生成一个匹配规则, 再进行匹配
m = re.compile('[0-9]*')
n = m.search(s)
print(n.group())

