#_*_ coding utf-8 _*_
#######################版本.4逆函数版#########################
def kaisai_jia():
    plain = input('请输入你所要加密の明文(小写字母):\n')
    KEY = int(input('请输入你所需の密钥(0-->25):\n'))
    letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    LETTER = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    p=[]
    p.append(letter)
    letter_new = letter[:]
    i=0
    while i<25:
        i=i+1
        letter_new = letter_new[:]#if 不加[:]就会进行浅复制，意思是LETTER_NEW与LETTER指向同一个对象
        letter_new.extend(letter_new[0:1])
        del(letter_new[0:1])
        p.append(letter_new)
    d=[]
    i=0
    while i<25:
        d.append(dict(zip(p[i],LETTER)))
        i=i+1
    cipher = []
    i=0
    while i<25:
        cipher.append('')
        i=i+1
    i=0
    while i<25:
        for ci in plain:
            for key,value in d[i].items():
                if key == ci:
                    cipher[i] = cipher[i] +(d[i][key])
        i=i+1
    print('这次加密后の密文是:\n')
    print(cipher[KEY])
    '''
    print( '以下是按凯撒密码破解の所有可能:\n')
    i=0
    while i<25:
        print('平移',i,'次:',cipher[i],'\n')
        i=i+1
    '''
#######################版本.3函数版###########################
def kaisai_jie():
    cipher = input('请输入你所要破解の密文(大写字母):\n')
    KEY = int(input('请输入你所需の密钥(0-->25):\n'))
    letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    LETTER = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    p=[]
    p.append(LETTER)
    LETTER_NEW = LETTER[:]
    i=0
    while i<25:
        i=i+1
        LETTER_NEW = LETTER_NEW[:]#if 不加[:]就会进行浅复制，意思是LETTER_NEW与LETTER指向同一个对象
        LETTER_NEW.extend(LETTER_NEW[0:1])
        del(LETTER_NEW[0:1])
        p.append(LETTER_NEW)
    d=[]
    i=0
    while i<25:
        d.append(dict(zip(p[i],letter)))
        i=i+1
    plain = []
    i=0
    while i<25:
        plain.append('')
        i=i+1
    i=0
    while i<25:
        for ci in cipher:
            for key,value in d[i].items():
                if key == ci:
                    plain[i] = plain[i] +(d[i][key])
        i=i+1
    print('这次解密后の明文是:\n')
    print(plain[KEY])
    '''
    print( '以下是按凯撒密码破解の所有可能:\n')
    i=0
    while i<25:
        print('平移',i,'次:',plain[i],'\n')
        i=i+1
    '''
#######################版本.2简洁版###########################
'''
#d = dict(zip(letter,LETTER))#可以讲aA相互对应
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
LETTER = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
p=[]
p.append(LETTER)
LETTER_NEW = LETTER[:]
i=0
while i<25:
    i =i + 1
    LETTER_NEW = LETTER_NEW[:]#if 不加[:]就会进行浅复制，意思是LETTER_NEW与LETTER指向同一个对象
    LETTER_NEW.extend(LETTER_NEW[0:1])
    del(LETTER_NEW[0:1])
    p.append(LETTER_NEW)
d = []
i = 0
while i<25:
    d.append(dict(zip(p[i],letter)))
    i=i+1
cipher = 'ZW PFL NREK KF CVRIE DFIV RSFLK TIPGKFXIRGYP Z IVTFDDVEU RE FECZEV TFLIJV ZEJKILTKVU SP GIFWVJJFI URE SFEVY WIFD JKREWFIU LEZMVIJZKP ALJK JVRITY TIPGKFXIRGYP RK TFLIJVIR.FIX'
plain = []
i = 0
while i<25:
    plain.append('')
    i=i+1
i = 0
while i<25:
    for ci in cipher:
        for key,value in d[i].items():
            if key == ci:
                plain[i] = plain[i] +(d[i][key])
    i=i+1
i = 0
while i<25:
    print('平移',i,'次:',plain[i],'\n')
    i=i+1
cipher = 'ZW PFL NREK KF CVRIE DFIV RSFLK TIPGKFXIRGYP Z IVTFDDVEU RE FECZEV TFLIJV ZEJKILTKVU SP GIFWVJJFI URE SFEVY WIFD JKREWFIU LEZMVIJZKP ALJK JVRITY TIPGKFXIRGYP RK TFLIJVIR.FIX'
plain='If you want to learn more about cryptography I recommend an online course instructed by professor Dan Boneh from stanford university just search cryptography at coursera.org'
print('明文是第17次：',plain)
'''
#######################版本.1复杂版###########################
'''
#d = dict(zip(letter,LETTER))#可以讲aA相互对应
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
LETTER = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
p=[]
p.append(LETTER)
LETTER_NEW = LETTER[:]
i=0
while i<25:
    i =i + 1
    LETTER_NEW = LETTER_NEW[:]#if 不加[:]就会进行浅复制，意思是LETTER_NEW与LETTER指向同一个对象
    LETTER_NEW.extend(LETTER_NEW[0:1])
    del(LETTER_NEW[0:1])
    p.append(LETTER_NEW)
d0 = dict(zip(p[0],letter))
d1 = dict(zip(p[1],letter))
d2 = dict(zip(p[2],letter))
d3 = dict(zip(p[3],letter))
d4 = dict(zip(p[4],letter))
d5 = dict(zip(p[5],letter))
d6 = dict(zip(p[6],letter))
d7 = dict(zip(p[7],letter))
d8 = dict(zip(p[8],letter))
d9 = dict(zip(p[9],letter))
d10 = dict(zip(p[10],letter))
d11 = dict(zip(p[11],letter))
d12 = dict(zip(p[12],letter))
d13 = dict(zip(p[13],letter))
d14 = dict(zip(p[14],letter))
d15 = dict(zip(p[15],letter))
d16 = dict(zip(p[16],letter))
d17 = dict(zip(p[17],letter))
d18 = dict(zip(p[18],letter))
d19 = dict(zip(p[19],letter))
d20 = dict(zip(p[20],letter))
d21 = dict(zip(p[21],letter))
d22 = dict(zip(p[22],letter))
d23 = dict(zip(p[23],letter))
d24 = dict(zip(p[24],letter))
d25 = dict(zip(p[25],letter))
plain0 = ''
plain1 = ''
plain2 = ''
plain3 = ''
plain4 = ''
plain5 = ''
plain6 = ''
plain7 = ''
plain8 = ''
plain9 = ''
plain10 = ''
plain11 = ''
plain12 = ''
plain13 = ''
plain14 = ''
plain15 = ''
plain16 = ''
plain17 = ''
plain18 = ''
plain19 = ''
plain20 = ''
plain21 = ''
plain22 = ''
plain23 = ''
plain24 = ''
plain25 = ''
cipher = 'ZW PFL NREK KF CVRIE DFIV RSFLK TIPGKFXIRGYP Z IVTFDDVEU RE FECZEV TFLIJV ZEJKILTKVU SP GIFWVJJFI URE SFEVY WIFD JKREWFIU LEZMVIJZKP ALJK JVRITY TIPGKFXIRGYP RK TFLIJVIR.FIX'
for ci in cipher:
    for key,value in d0.items():
        if key == ci:
            plain0 = plain0 +(d0[key])
    for key,value in d1.items():
        if key == ci:
            plain1 = plain1 +(d1[key])
    for key,value in d2.items():
        if key == ci:
            plain2 = plain2 +(d2[key])
    for key,value in d3.items():
        if key == ci:
            plain3 = plain3 +(d3[key])
    for key,value in d4.items():
        if key == ci:
            plain4 = plain4 +(d4[key])
    for key,value in d5.items():
        if key == ci:
            plain5 = plain5 +(d5[key])
    for key,value in d6.items():
        if key == ci:
            plain6 = plain6 +(d6[key])
    for key,value in d7.items():
        if key == ci:
            plain7 = plain7 +(d7[key])
    for key,value in d8.items():
        if key == ci:
            plain8 = plain8 +(d8[key])
    for key,value in d9.items():
        if key == ci:
            plain9 = plain9 +(d9[key])
    for key,value in d10.items():
        if key == ci:
            plain10 = plain10 +(d10[key])
    for key,value in d11.items():
        if key == ci:
            plain11 = plain11 +(d11[key])
    for key,value in d12.items():
        if key == ci:
            plain12 = plain12 +(d12[key])
    for key,value in d13.items():
        if key == ci:
            plain13 = plain13 +(d13[key])
    for key,value in d14.items():
        if key == ci:
            plain14 = plain14 +(d14[key])
    for key,value in d15.items():
        if key == ci:
            plain15 = plain15 +(d15[key])
    for key,value in d16.items():
        if key == ci:
            plain16 = plain16 +(d16[key])
    for key,value in d17.items():
        if key == ci:
            plain17 = plain17 +(d17[key])
    for key,value in d18.items():
        if key == ci:
            plain18 = plain18 +(d18[key])
    for key,value in d19.items():
        if key == ci:
            plain19 = plain19 +(d19[key])
    for key,value in d20.items():
        if key == ci:
            plain20 = plain20 +(d20[key])
    for key,value in d21.items():
        if key == ci:
            plain21 = plain21 +(d21[key])
    for key,value in d22.items():
        if key == ci:
            plain22 = plain22 +(d22[key])
    for key,value in d23.items():
        if key == ci:
            plain23 = plain23 +(d23[key])
    for key,value in d24.items():
        if key == ci:
            plain24 = plain24 +(d24[key])
    for key,value in d25.items():
        if key == ci:
            plain25 = plain25 +(d25[key])
print('平移0次:',plain0,'\n')
print('平移1次:',plain1,'\n')
print('平移2次:',plain2,'\n')
print('平移3次:',plain3,'\n')
print('平移4次:',plain4,'\n')
print('平移5次:',plain5,'\n')
print('平移6次:',plain6,'\n')
print('平移7次:',plain7,'\n')
print('平移8次:',plain8,'\n')
print('平移9次:',plain9,'\n')
print('平移10次:',plain10,'\n')
print('平移11次:',plain11,'\n')
print('平移12次:',plain12,'\n')
print('平移13次:',plain13,'\n')
print('平移14次:',plain14,'\n')
print('平移15次:',plain15,'\n')
print('平移16次:',plain16,'\n')
print('平移17次:',plain17,'\n')
print('平移18次:',plain18,'\n')
print('平移19次:',plain19,'\n')
print('平移20次:',plain20,'\n')
print('平移21次:',plain21,'\n')
print('平移22次:',plain22,'\n')
print('平移23次:',plain23,'\n')
print('平移24次:',plain24,'\n')
print('平移25次:',plain25,'\n')
cipher = 'ZW PFL NREK KF CVRIE DFIV RSFLK TIPGKFXIRGYP Z IVTFDDVEU RE FECZEV TFLIJV ZEJKILTKVU SP GIFWVJJFI URE SFEVY WIFD JKREWFIU LEZMVIJZKP ALJK JVRITY TIPGKFXIRGYP RK TFLIJVIR.FIX'
plain='If you want to learn more about cryptography I recommend an online course instructed by professor Dan Boneh from stanford university just search cryptography at coursera.org'
print('明文是第17次：',plain)
'''
