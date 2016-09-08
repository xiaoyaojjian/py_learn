# 数据读写不一定是文件，也可以是内存中读写
# StringIO==在内存中读写str
# 写入str
from io import StringIO
f = StringIO()
f.write('haloooo')
f.write('hh')
f.write('hhhhhh0')
# getvalue()用于获得写入后的str
print(f.getvalue())
# 读取str like读取文件般
f2 = StringIO('hhh1\nhhhhh2\nhh3\n')
while True:
    s = f2.readline()
    if s == '':
        break
    print(s.strip())
# BytesIO操作二进制数 实现内存中读写bytes
from io import BytesIO
f3.BytesIO()
f3.write('中华', encode('utf-8'))  # 写入的不是str 而是经过UTF-8编码的bytes
print(f3.getvalue())
# 读取bytes 立刻读取文件般
f4 = BytesIO(b''\xe4\xb8\xad\xaa\x00\x98)
f4.read()
# StringIO and BytesIO 在内存中操作str and bytes的方法（函数）使之有和读写文件一致接口
# StringIO不需要close，需要close()的stream也不建议手动close，而是用with自动close