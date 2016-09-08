import json

def auth():
    count = 0
    while count < 3:
        data = {}
        username = input('Please input your username:')
        password = input('Input your password:')
        with open('./data/user.txt', 'r') as f:
            data = dict(json.load(f))
            if username in data.keys():
                if data[username][0] == 0:
                    return 110
                if int(password) == data[username][1]:
                    return 1, username
                    # exit('Login OK!')
                else:
                    print('Password Error')
            else:
                print('Information Error')
            count += 1
    else:
        with open('./data/user.txt', 'w') as f:
            data[username][0] = 0
            json.dump(data, f)
        print('Count greater than 3! You will be black!')
