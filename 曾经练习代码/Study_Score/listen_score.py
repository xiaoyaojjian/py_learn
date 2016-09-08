#author:liangliang
#email:liangliangyy@gmail.com
#blog:http://www.lylinux.org/
import urllib2
import cookielib
from bs4 import BeautifulSoup
import smtplib
import time
from email.message import Message
from time import sleep
import email.utils
import base64




loginUrl = 'http://222.24.19.202/default_ysdx.aspx'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'

student_cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(student_cookie)) # Login


data = "__VIEWSTATE=dDw1MjQ2ODMxNzY7Oz799QJ05KLrvCwm73IGbcfJPI91Aw%3D%3D&TextBox1=********&TextBox2=***********&RadioButtonList1=%D1%A7%C9%FA&Button1=++%B5%C7%C2%BC++"
login_request = urllib2.Request(loginUrl, data, {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'UTF-8,*;q=0.5',
                    'User-Agent': USER_AGENT, 
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Connection': 'keep-alive',
                    'HOST': '222.24.19.202',
                    'Origin':  '222.24.19.202',
                    'Referer': 'http://222.24.19.202/xs_main.aspx?xh=********'})
opener.open(login_request, data)
theurl = "http://222.24.19.202/xscjcx.aspx?xh=************&xm=****************&gnmkdm=*****"  
thehtml = opener.open(theurl).read()

soup = BeautifulSoup(thehtml)

thestr = soup.find("table",{"class": "datelist"}).get_text()


subject = ""

def sendresult(str):
    global subject
    if str == "DZ110122":
        subject += "电路分析基础B"
    if str == "DZ110222":
        subject += "数字电路与逻辑设计B"
def sendmail():
    smtpserver = 'smtp.gmail.com'
    username = 'username @gmail.com'
    password = 'password '
         
    from_addr = 'from_addr @gmail.com'
    to_addr = 'to_addr @gmail.com'
   
         
   
         
    message = Message()
    message['Subject'] = '成绩监控'
    message['From'] = from_addr
    message['To'] = to_addr
  
    message.set_payload(subject + "   通过了!!!")
    msg = message.as_string()
         
    sm = smtplib.SMTP(smtpserver,port=587,timeout=20)
    
    sm.ehlo()
    sm.starttls()
    sm.ehlo()
    sm.login(username, password)
        
    sm.sendmail(from_addr, to_addr, msg)
    sleep(5)
    sm.quit()        

isfind = False
if (thestr.find('DZ110122')== -1):
    sendresult('DZ110122')
    isfind = True
    print "find ok"
if (thestr.find('DZ110222')== -1):
    sendresult('DZ110222')
    isfind = True
    print "find ok"

if isfind:
	sendmail()
print "the end"