import os, time, json

# 操作money 数据
def modify_money(username, numb):
    with open('./data/money.txt', 'r') as f:
        data = dict(json.load(f))
        data[username][1] += numb
    with open('./data/money.txt', 'w') as f:
        json.dump(data, f)
'''
def modify_money(username, numb):
    with open('./data/money.txt', 'r') as rf, open('./data/money.tmp', 'w') as wf:
        for line in rf:
            if username == line.split()[0]:
                print(int(line.split()[1]), numb, int(line.split()[1]) + numb)
                wf.write('%s %s\n' % (username, int(line.split()[1]) + numb))
            else:
                wf.write(line)
    os.remove('./data/money.txt')
    os.renames('./data/money.tmp', './data/money.txt')
'''
# 记录操作日志
def log(username, operate):
    with open('./data/%s.log' % username, 'a', encoding='utf-8') as f:
        f.write('\n%s ==> %s' % (time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()), operate))

# 集合 pay, repayment
def all_option(username, numb, option):
    numb = int(numb)
    with open('./data/money.txt') as f:
        data = dict(json.load(f))
        if username in data.keys():
            if option == 'get_money':
                if numb * 1.05 <= data[username][0] / 2:
                    f.close()
                    modify_money(username, -numb)
                    log(username, '提现%s' % -numb)
            if option == 'pay':
                if numb <= data[username][1]:
                    f.close()
                    modify_money(username, -numb)
                    log(username, '支付%s' % -numb)
            elif option == 'repayment':
                f.close()
                modify_money(username, +numb)
                log(username, '还款%s' % +numb)
            return 1
        else:
            return 0

# 查询余额
def show(username):
    with open('./data/money.txt') as f:
        data = dict(json.load(f))
        if username in data.keys():
            print('你的可用额度为: %s' % data[username][1])

'''
da = {
    'aaa': [20000, 19000],
    'bbb': [30000, 31000],
    'ccc': [66666, 15000],
    'ddd': [10000, 5000]
}
with open('../data/money.txt','w') as f:
    data = json.dumps(da)
    f.write(data)
'''

# 查看账户操作记录
def show_operate(username):
    if os.path.isfile('./data/%s.log' % username):
        with open('./data/%s.log' % username,encoding='utf-8') as f:
            print(f.read())
            # for line in f:
            #     print(line)
    else:
        print('%s暂时没有操作记录' % username)

# 提现
def get_money(username, numb):
    all_option(username, numb, 'get_money')
# 支付
def pay(username, numb):
    all_option(username, numb, 'pay')
# 还款
def repayment(username, numb):
    all_option(username, numb, 'repayment')
# 转账
def transfers(username, to_username, numb):
    numb = int(numb)
    with open('./data/money.txt') as f:
        data = dict(json.load(f))
        if username in data.keys() and to_username in data.keys():
            if numb <= data[username][1]:
                f.close()
                modify_money(username, -numb)
                log(username, '转账%s' % -numb)
                modify_money(to_username, +numb)
                log(to_username, '转账%s' % +numb)
                return 1
            else:
                return 0


# get_money('aaa', 1000)
# modify_money('ccc', 66666)