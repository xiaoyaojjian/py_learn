# urllib
# URL operation
# _*_coding:utf-8_*_
from urllib import request  # Python3X の 不同


def getHtml(url):
    page = request.urlopen(url)
    html = page.read()
    return html
html = getHtml("http://www.cnblogs.com/fnng/p/3576154.html")
with open('F:/Save/python/io_test.txt', 'w') as f:
    f.write(str(html))
# url.request 模块可将抓取URL内容 即发送一个GET请求至指定页面 返回HTTP响应
# eg:https://api.douban.com/v2/book/2129650
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('可看到HTTP响应の头与JSON数据:\n')
    print('Data:', data.decode('utf-8'))
# if want to sim browser send GET request 需使用Request对象
# 通过向Request添加HTTP头 则可将请求伪装成browser
req = request.Request('http://www.douban.com/')
req.add_header(
    'User-Agent', 'Mozilla/6.0(iPhone:CPU iPhone OS 8_0 like Mac OS X)AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('通过模拟iPhone6登录查看豆瓣网站 HTTP and JavaScript Object Notation\n')
    print('Data:', f.read().decode('utf-8'))
# if want to sim POST request 只需要将parameter data 以bytes形式传入
# sim weibo register first,email and password second,by weibo.com 登录页格式
# 以username = XXX  &  password = XXX 编码传入
from urllib import parse, request
print('Login to weibo.cn...')
email = input('Email: ')
password = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', password),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer',
     'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])
req2 = request.Request('https://passport.weibo.cn/sso/logi')
req2.add_header('Origin', 'http://passport.weibo.cn')
req2.add_header(
    'User-Agent', 'Mozilla/6.0 (iPhone:CPU iPhone OS 8_0 like Mac OS X)AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req2.add_header(
    'Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
with request.urlopen(req2, data=login_data.encode('utf-8')) as f2:
    print('Status:', f2.status, f2.reason)
    for k2, v2 in f2.getheaders():
        print('%s: %s' % (k2, v2))
    print('微博登录....')
    print('DATA:', f2.read().decode('utf-8'))
# by Proxy（代理） 访问网站 则需要ProxyHandler 处理
# by Proxy（代理） 访问网站 则需要ProxyHandler 处理
proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://examplel.com/login.html') as f:
    pass
'''
urllib 提供的功能是利用程序去执行各种HTTP请求
if sim browser完成特定功能
需要将请求伪装成browser
伪装方法是先监控browser send request
再根据browser的request来伪装
User—Agent 头解释用来标识browser
'''
# 利用urllib读取XML 将XML一节数据有硬编码(指固定の配置の宏の)改为urllib获取
from urllib import request, parse
from xml_test import WeatherSaxHandler


def fectch_xml(url):
    with request.urlopen(url) as f:
        xml_data = f.read()
        return parse_weather(xml_data.decode('utf-8'))
