#-*-coding:utf-8-*-
# socket is 套接字 接口
# 1 Socket
# 2 打印设备名 and ipv4 地址
import socket
def print_machine_info():
	host_name = socket.gethostname()
	print 'Host name: %s' % host_name
	ip_address = socket.gethostbyname(host_name)
	print 'Ip Address: %s' % ip_address
if __name__ == '__main__':
	print_machine_info()
# 3 打印远程设备 IP地址
import socket
def print_remote_machine_info():
	remote_host_name = 'www.python.org'
	try:
		print "Ip Address of %s: %s" % (remote_host_name,socket.gethostbyname(remote_host_name))
	except socket.error, err_msg:
		print "%s: %s" % (remote_host_name,err_msg)
if __name__ == '__main__':
	print_remote_machine_info()
# 4 将ip4 地址转换成不同格式
import socket
from binascii import hexlify	#以十六进制形式表示二进制
def convert_ip4_address():
	for ip_addr in ['127.0.0.1','192.168.0.1']:
		packed_ip_addr = socket.inet_aton(ip_addr)	# 将ipaddr转换成打包的32位二进制
		unpacked_addr = socket.inet_ntoa(packed_ip_addr)
		print "Ip Address: %s => Paked: %s, Unpacked: %s" % (ip_addr,hexlify(packed_ip_addr),unpacked_addr)
if __name__ == '__main__':
	convert_ip4_address()
# 5 by指定端口找到服务名
# if wants to find net service TCP or UDP which port
import socket
def find_service_name():
	protocol_name = 'tcp'
	for port in [80,53,25]:
		print "Port: %s => Service name: %s" % (port,socket.getservbyport(port,protocol_name))
if __name__ == '__main__':
	find_service_name()
# 6 主机字节序与网络字节序相互转换 host byte ordr and network byte order
import socket
def convert_integer():
	data = 1234
	# 32 bit
	print "Original: %s => Long host byte order: %s,Network byte order: %s" % (data,socket.ntohl(data),socket.htonl(data))
	# 16 bit
	print "Original: %s => Short host byte order: %s,Network byte order: %s" % (data,socket.ntohs(data),socket.ntohs(data))
if __name__ == '__main__':
	convert_integer()
# 7 设定并获取默认の 套接字超时时间
import socket
def test_socket_timeout():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print "Default socket timeout: %s" % s.gettimeout()
	s.settimeout(100)
	print "Current socket timeout: %s" % s.gettimeout()
if __name__ == '__main__':
	test_socket_timeout()
# 8 handler Socket Error
# 在网络应用中 一方尝试连接 但由于另一方网络媒介失效或其他原因导致无法响应
import sys
import socket
import argparse
def handle_socket():
	# setup argument parsing
	parser = argparse.ArgumentParser(description='Socket Error Exmples')
	parser.add_argument('--host',action="store",dest="host",required=False)
	parser.add_argument('--port',action="store",dest="port",type=int,required=False)
	parser.add_argument('--file',action="store",dest="file",required=False)
	given_args = parser.parse_args()
	host = given_args.host
	port = given_args.port
	filename = given_args.file
	# First try except block --create socket
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	except socket.error, e:
		print "Error creating socket: %s" % e
		sys.exit(1)
	# Second try except block --connect to given host/port
	try:
		s.connect((host,port))
	except socket.gaierror, e:
		print "Address-resulted error connecting to server: %s" % e
		sys.exit(1)
	except socket.error, e:
		print "Connection error: %s" % e
		sys.exit(1)
	# Third try except block --sending data
	try:
		s.sendall("Get %s HTTP/1.0\r\n\r\n" % filename)
	except socket.error, e:
		print "Error sending data: %s" % e
		sys.exit(1)

	while 1:
		# Fourth try except block --waiting to receive data from remote host
		try:
			buf = s.recv(2048)
		except socket.error, e:
			print "Error receiving data: %s" % e
			sys.exit(4)
		if not len(buf):
			break
			# vwrite the received daata
			sys.stdout.write(buf)
if __name__ == '__main__':
	handle_socket()