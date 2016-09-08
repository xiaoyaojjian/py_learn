"""
程序入口, 先启动
"""

from model.server import ChatServer
import socketserver

ip_prot = ('127.0.0.1', 8000)
server = socketserver.ThreadingTCPServer(ip_prot, ChatServer)
server.serve_forever()