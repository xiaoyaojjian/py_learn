# struct
# in pythom if want to unsign 32 int to bytes (4 bytes)
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = n & 0xff
bs = bytes([b1,b2,b3,b4])
print('bs = ',bs)
# strcut(structure is to solve bytes <==> 其他binary 数据类型 の 转换)
# struct.pack fun 将任意数据类型编出bytes
import struct
struct.pack('>I',10240099)
'''
pack第一个参数是 处理指令
'>I': > 表示字节顺序 是big-endian 即 网络序 I 表示 4 字节无符号整数
后main参数个数要和处理指令一致
'''
struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80')
# bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数
# _*_coding:utf-8_*_
import struct
class bmpinfo(dict):
	def __init(self,filepath):
		with open(filepath,'rb') as f:
			bmp_type = f.read(2)
			bmp_type = ''.join(map(bytes.decode,strcut.unpack('<cc',bmp_type)))
			if bmp_type not in('BM','BA'):
				raise FormatError('%s is not bmp format' % filepath)
			if bmp_type == 'BM':
				self['windows_bmp'] = True
			else:
				self['mac_bmp'] = True
			byte_contents = f.read(28)
			self._initail_attr(byte_contents)
	def _initail_attr(slef,bype_contents):
		infos = struct.unpack('IIIIIIHH',byte_contents)
		self['size'] = infos[0]
		self['width'] = infos[4]
		self['height'] = infos[5]
		self['depth'] = infos[7]
		def __getattr__(self,name):
			if name not in self:
				return None
			return self[name]
	info = bmpinfo('test.bmp')
	print('size: %s,depth: %s' % (info.size,info.depth))