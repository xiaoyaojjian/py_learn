"""
socket 服务模块
"""

import socketserver

from model import history_record


class ChatServer(socketserver.BaseRequestHandler):  # 实例化一个 server 对象, 继承 BaseRequestHandler 类

    flag = True

    def handle(self):
        conn = self.request
        user_id = int(conn.recv(1024))
        print(user_id)

        conn.sendall(b'welcome to AoChat!')
        client = history_record.HistoryRecord(user_id)

        while ChatServer.flag:
            receive = conn.recv(1024)
            if receive == b'bye':
                ChatServer.flag = False
                break
            client.write_record(receive)
            conn.send(b'You say')
        conn.close()


'''
if __name__ == '__main__':
    # server = socketserver.ForkingTCPServer(('127.0.0.1', 8000), MyServer)  # 多进程
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8000), ChatServer)  # 多线程
    server.serve_forever()
'''
