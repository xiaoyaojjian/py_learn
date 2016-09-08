#循环操作
#此指：将list names中的所有元素【mzc,lm,gp】全部依次代入name中进行print 操作
names = ['mzc','lm','gp']
for name in names:
    print(name)
#1+2+3....10
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum = sum+x
	'''
	这里一定要对print（）进行撤销缩进，
	否则会使print（）作为循环体，加一次，循环一次
	'''
print(sum)
#1*2*3....
product = 1
for product2 in [1,2,3,4,5,6,7,8,9,10]:
    product = product*product2
print(product)
#100以内累加
sum = 0
for x in range(100):
    sum = sum + x
print(sum)
#while循环
sum = 0
n = 10
while n>0:
    sum = sum + n
    n=n-1
print(sum)
#衔接第一个
for name in names:
    print('hello,',name)
