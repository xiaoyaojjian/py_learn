#错误处理
#利用错误代码
def foo():
	r = some_fun()
	if  r == -1:
		return -1
	return r
def var():
	r  = foo()
	if r == -1:
		print('Error')
	else:
		pass
#short：一旦出错，var()上报至foo进行处理，很麻烦
##利用try except finally 错误处理机制
try:
	print('try...')
	r = 10/a
	print('result:',r)
except ZeroDivisionError as e:
	print('except:',e)
finally:
	print('finally...')
print('END')
##错误很多种类
try:
	print('try...')
	r = 10/int('a')
	print('result:',r)
except ValueError as e:
	print('ValueError:',e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:',e)
finally:
	print('finally...')
print('END')
##若错误没有发生(或者说try时出错并没有在捕获的错误种类之中???)
try:
	print('try...')
	r = 10/int('a')
except ValueError as e:
	print('ValueError:',e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:',e)
else:
	print('no Error!')
finally:
	print('finally...')
print('END')
'''
python 错误是class 所有的错误都继承BASEEXCEPT
注意：不但捕获该类型的错误,且将其子类也捕获了
'''
try:
	foo()
except ValueError as e:
	print('ValueError:',e)
except UnicodeError as e:
	print('UnicodeError:',e)
'''
第二个except永远不能捕获到UnicodeError is ValueError的子类，
就算真的存在UnicodeError 亦被ValueError捕获过了，
因为这个错误不仅属于Unicode，那更是Value!
BaseExcept : 
https://docs.python.org/3/library/exceptions.html#exception-hierarchy
'''
def foo(s):
	return 10/int(s)
def bar(s):
	return foo(s)*2
def main():
	try:
		bar('0')
	except Exception as e:
		print('Error:',e)
	finally:
		print('finally...')
print('END')
##sulve 14 の short只要在合适的层次捕获错误即可
###若错误没有被捕获，就会一直向上抛啊抛
###最后被Python解释器捕获打印出错误信息，然后程序退出
def main_stack():
	bar('0')
#执行main_stack()后，结果：整个过程并没有人为说明捕获错误
'''
$ err.py
从上往下可以看到整个错误的调用函数链：
	错误信息第1行：告诉我们这是错误的跟踪信息
Traceback (most recent call last):
	第2~3行：调用main()出错了，在代码文件err.py的第11行代码，但原因是第9行
  File "err.py", line 11, in <module>
    main()
    调用bar('0')出错了，在代码文件err.py的第9行代码，但原因是第6行：
  File "err.py", line 9, in main
    bar('0')
    原因是return foo(s) * 2这个语句出错了，但这还不是最终原因，继续往下看：
  File "err.py", line 6, in bar
    return foo(s) * 2
    原因是return 10 / int(s)这个语句出错了，这是错误产生的源头
  File "err.py", line 3, in foo
    return 10 / int(s)
    于是下面打印了：
ZeroDivisionError: division by zero #eroDivisionError: integer division or modulo by zero#
根据错误类型ZeroDivisionError，我们判断，int(s)本身并没有出错，但是int(s)返回0，在计算10 / 0时出错，至此，找到错误源头
'''
#执行main_stack()后，如果不捕获错误 自然可让解释器自己打印出错误堆栈
###记录错误
###这里利用exception中的打印日志处理相同于未进行logging处理
def main_logging():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)
	print('END')
###抛出错误利用class
##自定义class
class FooError(ValueError):
	pass
def fooo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value: %s' % s)
	return 10/n
fooo('0')