#-*-coding:utf-8-*-
'''
登录教务系统查成绩
author = zlxs
'''
import urllib
import urllib2
import re
import os
import cookielib


def getVIEW(Page):          # Get viewststes for login page
    view = r'name="__VIEWSTATE" value="(.+)" '
    view = re.compile(view)
    return view.findall(Page)[0]


def Print(Score_html):		# print the result
    str = r"<td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.?)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.?)</td><td>(.?)</td>"
    str = re.compile(str)
    result = {}
    subject = []
    a = str.findall(Score_html)
    for i in a:
        for j in range(15):
            subject.append(i[j])
        result[subject[3]] = subject
        subject = []

    for i in result.keys():
        j = result[i]
        # print j
        print '%-10s%-2s%-10s%-8s%6s%8s%10s%6s%6s%5s%10s%-10s%-15s%s%s' % tuple(j)
        print " "


def getName(loginPage):		# get the name
    Sname = r'<span id="xhxm">(.+)同学</span>'
    Sname = re.compile(Sname)
    try:
        return Sname.findall(loginPage)[0]
    except IndexError, e:
        raise e
        print "User-name or password error, try again!"
        main()


def main():
    # this is the login page for xupt
    loginURL = 'http://202.200.144.63/default2.aspx'
    ID = raw_input("Please input your student ID:")
    Password = raw_input("Please input your password:")
    print 'Loading........'
    page = urllib2.urlopen(loginURL).read()
    postdata = urllib.urlencode({
        '__VIEWSTATE': getVIEW(page),
        'txtYhm': ID,  # std ID
        'txtMm': Password,  # password
        'rblJs': '学生',
        'btnDl': '登录'})
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0'}
    cookie = 'ASP.NET_SessionId=b5ypyozp50mncnmdn4nija45'
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    myRequest = urllib2.Request(loginURL, postdata, headers)
    loginPage = opener.open(myRequest).read()
    page = unicode(loginPage, 'gb2312').encode("utf-8")  # get the cookie
    # print page
    try:
        name = getName(page)
    except IndexError, e:
        # if name is not found, this is the reason
        print "User-name or password error, try again!"
        main()
        exit()
    else:
        pass

    # print cookie
    for i in cookie:
        Cookie = i.name+"="+i.value
    # print Cookie

    head = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': '202.200.144.63',
        'Cookie': Cookie,
        'Origin': 'http://202.200.144.63',
        'Pragma': 'no-cache',
        'Referer': 'http://202.200.144.63/xs_main.aspx?xh='+ID,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0'
    }

    getdata = urllib.urlencode({
        'xh': ID,
        'xm': name,
        'gnmkdm': 'N121605'

    })
    # According to this page ,we can get the viewstats
    MyRequest = urllib2.Request(
        'http://202.200.144.63/xscjcx.aspx?'+getdata, None, head)
    loginPage = unicode(
        opener.open(MyRequest).read(), 'gb2312').encode("utf-8")
    data = urllib.urlencode({
        "__VIEWSTATE": getVIEW(loginPage),
        "btn_zcj": "历年成绩"
    })
    MyRequest = urllib2.Request(
        'http://202.200.144.63/xscjcx.aspx?'+getdata, data, head)  # Score's page
    html = opener.open(MyRequest)
    result = unicode(html.read(), 'gb2312').encode("utf-8")
    Print(result)												# Score
if __name__ == '__main__':
    main()
