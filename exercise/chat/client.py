"""
客户端服务
"""

from socket import socket

from model import login

client = socket()
ip_port = ('127.0.0.1', 8000)
client.connect(ip_port)  # 创建连接

flag = True
while flag:
    username = input('Please input you username:')
    password = input('Password:')
    user_id = str(login.login_chack(username, password)).encode()
    if not user_id:
        print('account error')
    else:
        client.sendall(user_id)
        flag = False
while True:
    data = client.recv(1024)
    print(data)
    inp = input('client:').encode()  # 对输入内容进行编码
    client.sendall(inp)
    if inp == b'bye':
        client.close()
        break


