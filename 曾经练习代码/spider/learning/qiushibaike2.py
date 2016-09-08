# -*- coding:utf-8 -*-
import urllib2
import urllib,re
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
os.chdir('F:\Save\python\spider\learning')
class qsbk:
    def __init__(self):
        self.pageindex = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0'
        self.headers = {'User-Agent':self.user_agent}
    def getpage(self):
        try:
            url = r'http://www.qiushibaike.com/hot/page/'+str(self.pageindex)
            request = urllib2.Request(url,headers = self.headers)
            response = urllib2.urlopen(request)
            pagecode = response.read().decode('utf-8')
            return pagecode
        except:
            print 'Error!'
    def getpageitems(self):
        pagecode = self.getpage()
        if not pagecode:
            print '页面失败'
            return None
        pattern = re.compile(r'.*?<a.*?<a.*?(.*?).*?(.*?)<!.*?.*?(.*?)',re.S)
        items = re.findall(pattern,pagecode)
        pagestories = []
        for item in items:
            pagestories.append([item[0].strip(),item[1].strip().replace('','\n'),item[2].strip()])
        return pagestories
    def save(str):
        f = open('content.txt','w')
        f.write(str)
        f.close()

    def load(self,k):
        while self.pageindex<k:
            for i in self.getpageitems():
                self.save(i[0])
                self.save(i[1])
                self.save(i[2])
            self.pageindex += 1

qs=qsbk()
qs.load(4)