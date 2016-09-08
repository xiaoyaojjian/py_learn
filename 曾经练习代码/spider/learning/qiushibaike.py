# -*- coding:utf-8 -*-
import urllib2
import urllib,re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

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
    def load(self,k):
        while self.pageindex<k:
            for i in self.getpageitems():
                print '作者：'+i[0]+'\n','   '+i[1]+'\n','点赞数：'+i[2].strip()+'\n\n'
                print 'hehe'
            self.pageindex += 1

qs=qsbk()
qs.load(4)
