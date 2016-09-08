# POP3 Protocol to receive mail
# receive mail is to create a MUA as client
# from MDA to collected to user's com or phone
# protocol use POP
# poplib
# 1 use poplib 将原始文本download to local
# 2 use email 解析原始文本 还原为mail object
# collect mail
import poplib
# input mail address password POP3 Server address
email = input('Email: ')
password = input('Password: ')
pop3_server = input('POP3 Server:')
# connect to POP3 Server
server = poplib.POP3(pop3_server)
# 可选 open or close debug infor
server.set_debuglevel(1)
# 可选 print POP3 Server welcome word
print(server.getwelcome().decode('utf-8'))
# id认证
server.user(email)
server.pass_(password)
# stat() return mail 数量and占用空间
print('Message: %s. Size: %s.' % server.stat())
# list() return mail number
resp, mails, octets = server.list()
# 可以 查看return列表
print(mails)
# collect newest mail index = 1,2,3...
index = len(mails)
resp, lines, octets = server.retr(index)  # keykeykey
# lines can save mail 原始文本の每一行
# 可获得整个mailの原始文本
mas_content = b'\r\n'.join(lines).decode('utf-8')
# later parse mail
mas = Parser().parsestr(msg_content)
# 可according to mail index number directly delete mail
# server.dele(index)
# close connection
server.quit()
'''
用POP3获取邮件其实很简单，要获取所有邮件，只需要循环使用retr()把每一封邮件内容拿到即可
真正麻烦的是把邮件的原始内容解析为可以阅读的邮件对象
'''
# parse mail
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import poplib
# 将 mail content parse to message object
msg = Parser().parseaddr(msg_content)
# but this Message object maybe a MIMEMultipart object会有嵌套
# so need to Iter to print Message object 层次结构


def print_info(ms, indent=0):  # indent is 行，排列，缩进
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(value)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('		'*indent, header, value))
    if (mas.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%s part %s' % ('		' * indent), n)
            print('%s ----------------' % ('		' * indent))
            print_info(part, indent+1)  # iter
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('		' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('		' * indent, content_type))
# mail の Subject or Email name is encoded string,if want to display must
# to decode


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value
# decode_header() return a list
'''
因为像Cc、Bcc这样的字段可能包含多个邮件地址，所以解析出来的会有多个元素
上面的代码我们偷了个懒，只取了第一个元素
'''
# mail content is  string too,it need to test encode otherwise,非UTF-8
# can't display


def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset
