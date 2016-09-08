import os
os.getcwd()
os.name  # 操作系统类型
# if posix 则 Linux,Unix or Mac os x else nt windowa
# 非windows系统可调用uname()获取详细系统信息
# 操作文件与目录函数一部分在os模块中，也有在os.path模块中
# 查看当前目录的绝对路径
os.path.abspath('.')
# 在某个目录下创建一个出来新目录，首先把新目录的完整路径表示
os.path.join('F:\Save\python', 'test_dir')
# 然后创建一个目录
os.mkdir('F:\Save\python/test_dir')
# 删除一个目录
# os.rmdir('F:\Save\python/test_dir')
# 并不需要真正路径，即若不存在目录及文件，只对字符串进行操作
# 连接两个路径 通过连接函数
os.path.join('uer', 'ddd')
# 拆分路径
os.path.split('uer//ddd')
os.path.split('F:\Save\python\io_test.txt')
# 获得文件扩展名
os.path.splitext(('F:\Save\python\io_test.txt')
############################分开运行####################################
# 文件重命名
os.chdir('F:\Save\python')
os.rename('test.txt','ttest.txt')
os.remove('ttest.txt')
# 复制文件函数os中没有，复制文件并非由操作系统提供的系统调用
# 可利用对文件的读写课完成文件复制
# 可利用shutil.copyfile()函数 看做对os补充
# 列出当前目录下所有目录
#[x for x in os.listdir('.') if os.path.isdir(x)]
# 要列出所有py文件 利用22行
#[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']