"""
socket 服务端
"""

from socket import socket


sk = socket()  # 实例化一个 socket 对象
ip_port = ('127.0.0.1', 8000)
sk.bind(ip_port)
sk.listen(5)  # 设定可接受的连接数, 并启动服务

while True:
    conn, remote_address = sk.accept()  # accept 将获取一个元组 (客户端对象, (客户端地址, 端口))
    conn.send(b'hi,gay')  # 向客户端发送数据, 不接受 type 'str', 需要发送二进制字符串
    flag = True
    while flag:
        receive = conn.recv(1024)  # 设置缓冲区大小为 1024 byte, 接收数据
        print(receive, len(receive))
        if receive == 'bye':
            flag = False
        conn.send(b'you will be a gay!')
    conn.close()  # 断开连接
