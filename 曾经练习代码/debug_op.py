#DEbug操作
# 1 print option 简单粗暴 将有可能的变量打印出来
def foo1(s):
	n = int(s)
	print('>>>n = %d' % n)
	return  10/n
#利用print判断（调试）完后，print语句本身会存在程序中，下次调用依然运行
def main1():
	foo1(0)
main1()
# 2 assert option 将print 用assert进行替代
def foo2(s):
	n = int(s)
	assert n != 0,'n is zero!' 
	#表达式 n!=0应该是true 否则根据程序运行逻辑后面代码肯定会出差错
	#若断言失败，assert语句本身会抛出错误AssertionError
	return 10/n
def main2():
	foo2(0)
#利用assert判断（调试）完后，assert语句会当做pass来看，不会影响下次运行
main2()
# 3 logging option 将print 用logging进行替代
	#与asset相比，logging 不会跑出错误，且输出到文件里，当做日志
import logging
logging.basicConfig(level = logging.INFO)
#配置logging记录信息的级别：按照自己需求进行输出不同级别的信息
#debug(1)，info(2)，warning(3)，error(4)等几个级别
#当指定level = 某一级别后，高级别的就不起作用
##如，当指定level=info后，logging.debug就不起作用；
##同理，当指定level=error后，logging.debug,logging.info,logging.warning都不起作用了
###可通过logging通过配置将一条语句同时输出到不同地方：console操纵台和日志文件中
s1 = '0'
n1 = int(s1)
logging.info('n1 = %d' % n1)
print(10/n1)
#利用logging后，可输出一端文本:
#除了ZeroDivisionError，若是不进行logging配置，则无任何信息输出
#若进行不同级别信息配置可按自己要求进行输出信息
# 4 pdb option 启动Python 调试器pdb program database file 使程序一行一行单步运行
import pdb
#Python pdb调试 http://www.cnblogs.com/chencheng/p/3161778.html
s2 = '0'
n2 = int(s2)
print(10/n2)
# $ python3 -m pdb test.py cmd调用她
# 5 pdb.set_trace() option 自动暂停进入pdb调试环境
s3 = '0'
n3 = int(s3)
pdb.set_trace() #程序运行到这里会自动暂停 然后进行调试了
print(10/n)
#解决4中单步运行的麻烦，直接转到需要调试的地方才进行调试，by命令p c
#命令p查看变量内容 如输入p n 即 查看n的内容
#命令c继续运行下一行
#效率高于直接启动pdb单步调试4
# 5 IDE 设置断点，单步执行 支持调试功能 Python IDE Python 
#PyCharm http://www.jetbrains.com/pycharm/下载地址