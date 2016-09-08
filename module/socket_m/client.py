"""
socket 客户端
"""

from socket import socket

client = socket()
ip_port = ('127.0.0.1', 8000)
client.connect(ip_port)  # 创建连接

while True:
    data = client.recv(1024)
    print(data)
    inp = input('client:').encode()  # 对输入内容进行编码
    client.send(inp)
    if inp == b'bye':
        break
