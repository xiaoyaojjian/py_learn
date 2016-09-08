# _*_coding:utf-8 _*_
# 实现文件读写
f1 = open('F:/Save/python/io_test.txt', 'r')
f1.read()
f1.close()
# 由于文件读写都有可能产生IOError 一旦出错后面的f.close就不会调用
# so为保证无论是否出错都可正确关闭文件 两个方法实现同样功能
# 1 try ... finally实现
try:
    f2 = open('F:/Save/python/io_test.txt', 'r')
    print(f2.read())
finally:
    if f2:
        f2.close()
# 2 with实现
with open('F:/Save/python/io_test.txt', 'r') as f3:
    print(f3.read())
#乙方一次性读取太多 内存耐不住 保险起见 
#反复调用：不能确定文件大小时--read(size) 读size个字节 or 读取配置文件--readlines() 读一行
    '''
for line in f3.readlines():
	print(line.strip())#去掉'\n'
	'''
#file-like-object
#以上是utf-8编码の文本文件
#binary if读取二进制文件：图片，视频等'rb'
f4 = open('F:/Save/python/io_binary_test.jpg','rb')
f4.read()#十六进制表示的字节内容
#字符编码  if不是utf-8编码の文本文件需给open函数传入参数encoding
f5 = open('F:/Save/python/io_test_encoding.txt','r',encoding='gbk')
f5.read()
#若是已说明了编码参数，但依然还有非法编码，则在定义个参数errors
f6 = open('F:/Save/python/io_test_encoding.txt','r',encoding='gbk',errors = 'ingore')
f6.read()
#写文件
f7 = open('F:/Save/python/io_test.txt','w')
f7.write('nmb7')
f7.close
# with 实现文件数据的全部写入
with open('F:/Save/python/io_test.txt','w') as f8:
	f8.write('nmb8')
# if 写入不同的编码格式 文本文件 则传入encoding参数
with open('F:/Save/python/io_test.txt','w',encoding='gbk') as f9:
	f9.write('nmb9')
#写到此刻，已经将txt文件内容改成 nmb9
#文件读写通过open函数打开文件对象完成
#使用with语句操作文件IO是个好习惯