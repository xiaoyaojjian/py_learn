# hashlib
# Python supply some abstruct(摘要--抽象)algorithm(算法)
# abstruct algorithm = hash algorithm = 散列算法
# by a function let 任意长度的DATA转换成一个长度固定地数据串
import hashlib
# MD5 is common algorithm speed is fast
# product result is fixed 138 bit byte == 32位16进制string
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
summ = md5.hexdigest()
print('md5:', summ)
# 分块调用update()，与以上结果相同 when data is too huge
md51 = hashlib.md5()
md51.update('how to use md5 '.encode('utf-8'))
md51.update('in python hashlib?'.encode('utf-8'))
fenn = md51.hexdigest()
print('md5:', fenn)
md52 = hashlib.md5()
md52.update('how to use md5'.encode('utf-8'))  # 相比上式少了个空格
md52.update('in python hashlib?'.encode('utf-8'))
fennn = md52.hexdigest()
print('md5:', fennn)  # 不同于上式md5码
# SHA! is 160 bit byte == 40位16进制string
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in python hashlib?'.encode('utf-8'))
print('sha1:', sha1.hexdigest())
# 采用碰撞————>>两个不同数据通过某种abstruct algorithm 获得相同摘要 is very complex
# 摘要算法运用在用户登录的用户名和口令存储上，以防信息泄露
'''
name    | password
--------+----------
michael | 123456
bob     | abc999
alice   | alice2008
###############################################
username | password
---------+---------------------------------
michael  | e10adc3949ba59abbe56e057f20f883e
bob      | 878ef96e86145580c38c87f0410ad153
alice    | 99b1c2188db85afee403b1536010c2c9
'''
# exercise
# 1 根据用户输入的口令，计算存储在数据库中的MD5口令 函数


def calc_md5(password):
    import hashlib
    md5 = hashlib.md5()  # 在这里可以插入判断符合格式的密码，利用到re及Errorのraise 利用到doctest进行TDD
    md5.update(password.encode('utf-8'))
    save = md5.hexdigest()
    return save
# 2 设计一个验证用户登录 函数 根据用户输入是否正确 返回True or False


def login(username, password):
    import hashlib
    db = {
        'michael': 'e10adc3949ba59abbe56e057f20f883e',
        'bob': '878ef96e86145580c38c87f0410ad153',
        'alice': '99b1c2188db85afee403b1536010c2c9'
    }
    md5 = hashlib.md5()
    for i in db.keys():
        if i == username:
            md5.update(password.encode('utf-8'))
            if db[i] == md5.hexdigest():
                return True
            else:
                return False
# 3 加盐==>用户的简单口令导致更易破解，so在程序上使password复杂些，使之md5后不易破解


def calc_md5_salt(password):
    return calc_md5(password + 'the-Salt')
'''
根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：

db = {}

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
然后，根据修改后的MD5算法实现用户登录的验证：

def login(username, password):
    pass

test dict
>>> d ={}
>>> d['1']='A'
>>> d
{'1': 'A'}
>>> d['2']='B'
>>> d
{'1': 'A', '2': 'B'}
'''
# 4 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5
userdb = {}
# 保存用户信息
def saveuser(username,password):
	userdb[username] = password
# 注册 logon
def logon(username,password):
	username = calc_md5(username+'use_salt')
	password = calc_md5(password+'password_salt')
	saveuser(username,password)		#保存の数据对应都是加盐のMD5
# 登录 login