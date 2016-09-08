data = {
    'aaa': 123,
    'bbb': 123
}

count = 0
while count < 3:
    username = input('Please input your username:')
    password = input('Input your password:')
    if username in data.keys():
        if int(password) == data[username]:
            exit('Login OK!')
    else:
        print('Information Error')
    count += 1
else:
    exit('Count greater than 3!')



