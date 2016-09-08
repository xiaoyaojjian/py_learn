age = 3;
if age>=18:
	print('小伙子可以看片子了O(∩_∩)O~')
	print('adult')
else:
	print('小朋友可要注意身体营养要跟上嘿')
	print('kid')
#next
birth = input('birth:')
birth = int(birth)
if birth <2000:
	print('00前~')
else:
	print('00后~')
#BMI expression
high = input('请输入身高：')
high = float(high)
weight = input('请输入体重：')
weight = float(weight)
bmi = weight/(high*high)
if bmi<18.5:
	print('过轻~')
elif bmi<25:
	print('正常~')
elif bmi<28:
	print('过重~')
elif bmi<32:
	print('肥胖~')
else:
    print('完了~')	
