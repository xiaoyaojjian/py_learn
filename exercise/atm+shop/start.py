from atm import login, operate, pay
from shop import shop

op = '''
取现 ==> 1 金额
查询 ==> 2
还款 ==> 3 金额
转账 ==> 4 谁 金额
退出 ==> 5
'''
# print(pay.shop_pay('aaa', 123, 20))
cho = input('Pleasr input \033[33;1matm\033[0m or \033[33;0mshop\033[0m:')
if cho == 'atm':
    res, user = login.auth()
    print(user)
    if res:
        while True:
            print(op)
            opt = str(input('Please choice you operate:')).split(' ')
            print(opt)
            if opt[0] == '1':
                operate.get_money(user, opt[1])
            elif opt[0] == '2':
                operate.show_operate(user)
                operate.show(user)
            elif opt[0] == '3':
                operate.repayment(user, opt[1])
            elif opt[0] == '4':
                operate.transfers(user, opt[1], opt[2])
            elif opt[0] == '5':
                exit('see you again.')
            else:
                print('给我输个对的!')
                continue
            print('操作完成!')
    else:
        print('认证失败')
elif cho == 'shop':
    numb = shop.shop()
    username = input('Plesse input you username:')
    password = int(input('Please input you password:'))
    print(pay.shop_pay(username, password, numb))


