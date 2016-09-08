import json
from atm.operate import pay

def shop_pay(username, password, numb):
    with open('./data/user.txt') as f:
        data = dict(json.load(f))
        if username in data.keys():
            if data[username][0] == 1:
                if password == data[username][1]:
                    with open('./data/money.txt') as m:
                        m_data = json.load(m)
                        if numb <= m_data[username][1]:
                            pay(username, numb)
                        else:return 'no money'
                else:return 'password error'
            else:return 'you were black'
        else:return 'username does not exist'
    return 1
