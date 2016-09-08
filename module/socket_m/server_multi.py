"""
多线程服务
"""

import socketserver


class MyServer(socketserver.BaseRequestHandler):  # 实例化一个 server 对象, 继承 BaseRequestHandler 类
    def handle(self):
        conn = self.request
        conn.sendall(b'hi, girl')
        flag = True
        while flag:
            receive = conn.recv(1024)
            print(receive)
            if receive == 'bye':
                flag = False
            conn.send(b'you will be a lily!')
        conn.close()

if __name__ == '__main__':
    # server = socketserver.ForkingTCPServer(('127.0.0.1', 8000), MyServer)  # 多进程
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8000), MyServer)  # 多线程
    server.serve_forever()
