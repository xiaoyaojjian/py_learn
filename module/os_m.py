import os

print(os.getcwd()) #当前目录
print(os.listdir()) #以列表形式打印指定目录下的所有文件和子目录
print(os.name) #显示系统类型
aa = os.system('dir c:') #执行shell 命令
print(aa) #返回状态码
os.listdir('c:')
print(os.path.abspath(__file__)) #获取文件的绝对路径
print(os.path.dirname(__file__)) #获取文件所在目录
print(os.path.basename(__file__)) #获取文件名
print(os.path.isfile(__file__))
print(os.path.isdir(__file__))