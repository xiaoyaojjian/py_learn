'''
读取user.txt 文件中的信息,每次重新输入前重新生成字典
'''
count = 0
while count < 3:
    data = {}
    with open('user.txt','r') as f:
        for line in f.readlines():
            u,p = line.split()
            data[u] = p
    print(data.keys(),data.values())
    username = input('Please input your username:')
    password = input('Input your password:')
    if username in data.keys():
        if password == data[username]:
            exit('Login OK!')
        else:print('Password Error')
    else:
        print('Information Error')
    count += 1
else:
    print('Count greater than 3!')



