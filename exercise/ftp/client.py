"""
文件上传客户端
"""

import socket
import os

ip_port = ('127.0.0.1', 9999)
sk = socket.socket()
sk.connect(ip_port)

while True:
    up_file = input('path:')
    cmd, path = up_file.split('|')
    file_name = os.path.basename(path)
    file_size = os.stat(path).st_size
    operate = '%s|%s|%s' % (cmd, file_name, str(file_size))
    sk.send(operate.encode())
    # sk.send(b"'%s|%s|%s' % (cmd, file_name, str(file_size))")
    send_size = 0
    f = open(path, 'rb')
    flag = True
    while flag:
        if send_size + 1024 > file_size:
            data = f.read(file_size - send_size)
            flag = False
        else:
            data = f.read(1024)
            send_size += 1024
        sk.send(data)
    f.close()

sk.close()
