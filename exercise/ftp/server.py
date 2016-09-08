"""
文件上传服务端
"""

import socketserver
import os


class FtpServer(socketserver.BaseRequestHandler):
    def handle(self):
        base_path = 'E:\\code\\ftp\\upload'
        conn = self.request
        print('connected')
        while True:
            pre_data = bytes.decode(conn.recv(1024))
            print(pre_data)
            # 获取请求方法、文件名、文件大小
            cmd, file_name, file_size = pre_data.split('|')
            # 已经接收文件的大小
            recv_size = 0
            # 上传文件路径拼接
            file_dir = os.path.join(base_path, file_name)
            f = open(file_dir, 'ab')
            flag = True
            while flag:
                # 未上传完毕，
                print(recv_size)
                if int(file_size) > recv_size:
                    # 最多接收1024，可能接收的小于1024
                    data = conn.recv(1024)
                    # with open(file_dir, 'ab') as f:
                    f.write(data)
                    recv_size += len(data)
                # 上传完毕，则退出循环
                else:
                    recv_size = 0
                    flag = False
            f.close()
            print('upload successed.')


instance = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), FtpServer)
instance.serve_forever()
