# SMTP is send mail protocol
# support SMTP is smtplib(send) and email(structure
'''
# 1 structure mail by email
from email.mime.text import MIMEText
msg = MIMEText('hello,send by Python...','plain','utf-8')
# msg is MIMEText object,parameter1 is content,parameter2 is MIMEText subtype(子类型)
# 2 send mail by smtplib
# input Email address and password
from_addr = input('From: ')
from_pass = input('Password: ')
# input receive address
to_addr = input('To: ')
# input SMTP Sever address
smtp_sever_addr = input('SMTP Sever: ')
import smtplib
sever = smtplib.SMTP(smtp_sever_addr,25)	# SMTP protocol default port is 25
sever.set_debuglevel(1)	# print infor about SMTP Sever
sever.login(from_addr,from_pass)	# login SMTP Sever
sever.sendmail(from_addr,[to_addr],msg.as_string())	# list[]可发送多人，将MIMEText object to str
sever.quit()
'''
# 1 纯文本邮件
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From: ')
from_pass = input('Password: ')
to_addr = input('To: ')
smtp_sever_addr = input('SMTP Sever: ')

msg = MIMEText('hello,send by PY...', 'plain', 'utf-8')
msg['From'] = _format_addr('PY <%s>' % from_addr)
msg['To'] = _format_addr('ZLXS <%s>' % to_addr)
msg['Subject'] = Header('From SMTP の ASK......', 'utf-8').encode()

sever = smtplib.SMTP(smtp_sever_addr, 465)
sever.set_debuglevel(1)
sever.login(from_addr, from_pass)
sever.sendmail(form_addr, [to_addr], msg.as_string())
sever.quit()
# 2 HTML邮件
# from email import encoders
# alter msg 即可
msgh = MIMEText('<html><body><h1>Hello</h1>' +
                '<p>send by <a href="http://www.python.org">PY</a>...</p>' + '</body></html>', 'html', 'utf-8')
# send 附件
'''
带附件的邮件可以看做包含若干部分的邮件：
文本和各个附件本身
可以构造一个MIMEMultipart对象代表邮件本身
然后往里面加上一个MIMEText作为邮件正文
再继续往里面加上表示附件的MIMEBase对象
'''
# 3 mail object
msgo = MIMEMultipart()
msgo['From'] = _format_addr_format_addr('PY <%s>' % from_addr)
msgo['To'] = _format_addr('ZLXS <%s>' % to_addr)
msgo['Subject'] = Header('From SMTP の ASK......', 'utf-8').encode()
# mail text
msgo.attach(MIMEText('Send with file...', 'plain', 'utf-8'))
# mail 附件
with open('F:\Save\python\\bulr.jpg', 'rb') as f:
    # set 附件 の MIME and filename
    mimeo = MIMEBase('image', 'jpg', filename='bulr.jpg')
    # add neccessary header info
    mimeo.add_header('Content-Disposition', 'attachment', filename='bulr.jpg')
    mimeo.add_header('Content-ID', '<0>')
    mimeo.add_header('X=Attachment-ID', '0')
    # read 附件 content
    mimeo.set_payload(f.read())
    # use base64 encode
    encoders.encode_base64(mimeo)
    # add to MIMEMultipart
    msgo.attach(mimeo)
# 4 将图片内嵌到mail text
'''
按照发送附件的方式，先把邮件作为附件添加进去
在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入
如果有多个图片，给它们依次编号，然后引用不同的cid:x即可
'''
msgo.attach(MIMEText('<html><body><h1>Hello</h1>' +
                     '<p><img src="cid:0"></p>' + '</body></html>', 'html', 'utf-8'))
# 5 同时支持HTML and Plain
'''
在发送HTML的同时再附加一个纯文本
如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件
利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative
'''
msgoh = MIMEMultipart('alternative')
msgoh['From'] = ...
msgoh['To'] = ...
msgoh['Subject'] = ...
# 6 encipher SMTP
'''
use standard port 25 connect SMTP SEver -> plain
so, encipher SMTP,first create SSL connect,second use SMTP protocol to send mail
example Gmail 587
'''
smtp_sever_addr = 'smtp.gmail.com'
smtp_port = 587
sever = smtplib.SMTP(smtp_sever_addr, smtp_port)
sever.starttls()
sever.set_debuglevel(1)
sever.login(from_addr, from_pass)
sever.sendmail(form_addr, [to_addr], msg.as_string())
sever.quit()
# after creating SMTP object,immediately use starttls() this is created 安全连接
'''
构造一个邮件对象就是一个Messag对象
如果构造一个MIMEText对象，就表示一个文本邮件对象
如果构造一个MIMEImage对象，就表示一个作为附件的图片
要把多个对象组合起来，就用MIMEMultipart对象
而MIMEBase可以表示任何对象
Message
+MIMEBase
	++MIMEMultipart
	++MIMEonMultipart
		+++MIMEMessage
		+++MIMEText
		+++MIMEImage
from https://docs.python.org/3/library/email.mime.html
'''
