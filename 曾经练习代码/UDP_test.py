# UDP用户数据报协议
# User Dataprogram Protocol
import socket
# create socket
# sever
# SOCK_DGRAN 指定socket 类型是UDP不需要监听listen
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定port
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')
while True:
    # receive data
    # recvfrom() return data and clientの addr and port
    data, addr = s.recvfrom(1024)
    print('Receviced from %s: %s.' % addr)
    # sever received data directly 利用sendto将data用UDP 发给client
    s.sendto(b'Hello,%s' % data, addr)
# 这里取消multithreadings this is easy
# client
# 这里client use 1 create based on UDP の socket 不需调用connect
# 直接通过sendto将sever to data
sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'M', b'Z', b'C']:
    # send data
    sc.sendto(data, ('127.0.0.1', 9999))
    # receive data
    print(sc.recv(1024).decode('utf-8'))
sc.close()
# from sever also use recv()
