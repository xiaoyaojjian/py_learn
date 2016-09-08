# TCP-program
# Socket is netprogram a abstrct concept 插座Socket
# 通常以一个Socket表示"打开了一个网络编程"
# 打开一个Socket需要知道目标计算机のIP地址与端口号，再指定protocol类型即可
# 大多数连接都是可靠TCP连接
# 客户端Client
# create a base on TCP连接のSocket
# 1 import socket lib
import socket
# 2 cretae a socket #采用AF_INET指IPv4协议 SOCK_STREAM指使用面向流のTCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3 create link-connect
# method connect() の parameter is tuple(ipaddress,portnum)
s.connect(('www.sina.com.cn', 80))
# 客户端主动发起TCP连接，须知道服务器のIP address and port number
# sina's IP address 可用域名自动转换至IP address
# sina's port num 作为服务器，提供什么样の服务 端口号即固定下来
# created TCP 可向sina sever send request ask 首页内容
# 4 发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# TCPconnect create double channel 双方都可同时给对方发送数据
# 5 接受数据
bufferr = []
while True:
    # every 最多接受1k字节
    # recv(max)一次最多接收指定字节数 so in a while loop 直到recv返回空数据表示接收完毕
    d = s.recv(1024)
    if d:
        bufferr.append(d)
    else:
        break
data = b''.join(bufferr)
# ６ close connect
s.close()
# 以上，一次完整网络通信结束
# 接收到数据包
header, html = data.split(b'\r\n\r\n', 1)
print('HTTP header:', header.decode('utf-8'))
print('html content save in sina.html')
with open('sina.html', 'wb') as f:
    f.write(html)

# 服务器Sever
# 针对Sever Socket依赖:Sever IPaddress,Sever port num,Client IPaddress,Client portnum
# 唯一确定一个Socket
# 接受Client connect 将Client 发来のstring 加上hello 再返回去
# 1 create a Base on IPv4 and TCP Socket

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2 绑定监听のaddress and port
# 0.0.0.0->all net address
# 127.0.0.1->本机 address
# 监听端口
sc.bind('127.0.0.1', 9999)  # this is not standard sever(9999>1024)
sc.listen(5)  # 监听端口，parameter 指定等待connectの最大数量
print('Waiting for connection...')
# 3 by 永久循环来接受clientのconnect
# accept会等待并返回 一个clientの连接
while True:
    # receive a new connect
    sock, addr = sc.accept()
    # create a new thread to handle TCP connect
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
# every connect needs to create a new thread(process) to
# handle,否则单线程处理连接时，无法接受其他client的连接


def tcplink(sock, addr):
    print('Accept new connection from %s: %s...' % addr)  # created connect
    sock.send(b'Welcome!')  # 欢迎消息
    while True:
        data = sock.recv(1024)  # 等待 client send data
        time.sleep(1)
        # 若receive client 给的'exit'则断开连接
        if not data or data.decode('utf-8') == 'exit':
            break
        # 若无则加上hello后发送给client更新文本消息
        sock.send(('Hello,%s' data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('connection %s' % addr)

# for testing 服务器Sever program to code a client program
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# create connect
cs.connect('127.0.0.1', 9999)
# receive welcome mess
print(cs.recv(1024).decode('utf-8'))
for data in [b'm', b'z', b'c']:
        # send data
    cs.send(data)
    print(cs.recv(1024).decode('utf-8'))
cs.send(b'exit')
cs.close()
