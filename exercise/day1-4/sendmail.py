import smtplib
from email.mime.text import MIMEText
#from email.header import Header

def sm(receiver, title, body):

    host = 'smtp-mail.outlook.com'
    port = 587
    sender = 'email'
    pwd = 'password'

    try:
        msg = MIMEText(body, 'plain', 'utf-8')
        msg['subject'] = title
        msg['from'] = sender
        msg['to'] = receiver
        server = smtplib.SMTP(host, port)
        #按照国内博客的套路怎么也发不出去, 添加以下两行解决, 注意部分邮箱使用了tls
        server.ehlo()
        server.starttls()
        server.login(sender,pwd)
        server.sendmail(sender, receiver, msg.as_string())
        server.close()
        return True
    except:
        return False

'''
example
if sm('1305482232@qq.com', 'second_name', 'she is gaoyuan'):
    print('send done.')
'''