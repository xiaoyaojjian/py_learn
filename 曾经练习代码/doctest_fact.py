# _*_coding :utf-8 _*_
def fact(n):
	'''>>> fact(-1)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    fact(-1)
  File "F:\Save\python\doctest_fact.py", line 6, in fact
    raise ValueError()
ValueError
>>> fact(0)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    fact(0)
  File "F:\Save\python\doctest_fact.py", line 6, in fact
    raise ValueError()
ValueError
>>> fact(1)
1
>>> fact(2)
2
>>> 
	'''
	if n < 1:
		raise ValueError()
	if n==1:
		return 1
	return n*fact(n-1)
if __name__=='__main__':
        import doctest
        doctest.testmod()
print('doctest测试合格...')
