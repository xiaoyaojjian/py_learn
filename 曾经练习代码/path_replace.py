#_*_coding:utf-8_*_
'''
win:
将path中'\'替换成'/'
linux:
或将path中'/'替换成'\'
'''
def path_replace(path,sys='win'):
	if sys == 'win':
		path = str(path).replace('\\','/')
	if sys == 'lin':
		path = str(path).replace('/', '\\')
	return path