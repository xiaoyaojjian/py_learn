a = '''02H,00H,02H,00H,02H,10H,7FH,0F8H,
42H,10H,42H,10H,7FH,0F0H,42H,10H,
42H,10H,7FH,0F0H,42H,10H,02H,00H,
02H,04H,02H,04H,01H,0FCH,00H,00H'''
'''
这是一个实现a 所示的copy 的字库 对他进行处理(十六进制 二进制 字符串)并输出含有多少个1,0
'''
ls = a.split(',')

for i in [8,16,24]:
	ls[i] = ls[i][1:]

for k in range(32):
	if len(ls[k]) == 4:
		ls[k] = ls[k][1:].rstrip('H')
	else:
		ls[k] = ls[k].rstrip('H')

s = []
for j in range(16):
	s.append(ls[2*j]+ls[2*j+1])

for i in range(16):
	s[i] = bin(int(s[i],16))[2:]
	delta = 16 - len(s[i])
	s[i] = '0'*delta + s[i]
	if i >= 10:
		print 'Line %s is %s' % (i,s[i])
	else:
		print 'Line 0%s is %s' % (i,s[i])

for i in range(16):
	if s[i].count('1') == 0 or s[i].count('0') == 0:
		if s[i].count('1') == 0:
			if i >= 10:
				print 'Line %s the whole is "0"' % i
			else:
				print 'Line 0%s the whole is "0"' % i
		else:
			if i >= 10:
				print 'Line %s the whole is "1"' % i
			else:
				print 'Line 0%s the whole is "1"' % i
	elif s[i].count('1') <= s[i].count('0'):
		index1 = [si for si in range(16) if s[i][si] == '1']
		if i >= 10:
			print 'Line %s equal "1" %s sums is : %s' % (i,len(index1),sorted(map(lambda x:15-x,index1)))
		else:
			print 'Line 0%s equal "1" %s sums is : %s' % (i,len(index1),sorted(map(lambda x:15-x,index1)))
	else:
		index0= [si for si in range(16) if s[i][si] == '0']
		if i >= 10:
			print 'Line %s equal "0" %s sums is : %s' % (i,len(index0),sorted(map(lambda x:15-x,index0)))
		else:
			print 'Line 0%s equal "0" %s sums is : %s' % (i,len(index0),sorted(map(lambda x:15-x,index0)))
#print index
'''
#判断s有多少个1 0
bin(int(s[3],16))
# return 0b
re[2:]
# 与16判断大小
小则 要前面补0
'''