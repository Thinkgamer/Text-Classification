#coding:utf-8

#第一部分：得到首页博客专家各个系列链接
#===============================================================================

import urllib2
from bs4 import BeautifulSoup


def getPage(href): #伪装成浏览器登陆,获取网页源代码
    headers = {  
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
    }  
    req = urllib2.Request(  
        url = href ,
        headers = headers  
    )  
    
    #content = urllib2.urlopen(req).read()
    if urllib2.urlopen(req).read():
        return urllib2.urlopen(req).read()

url = 'http://blog.csdn.net/mobile/hot.html'

def getEvery(url):
    page = BeautifulSoup(getPage(url))
    div = page.find('div',class_='side_nav')
    liList = div.find_all('li')
    for li in liList:
        href = 'http://blog.csdn.net' + li.a.get('href')
        if href!='http://blog.csdn.net/hot.html':
            fp = open("every.txt","a")
            fp.write(href + "\n")
            fp.close()


if __name__=="__main__":
    getEvery(url)
    print "OK"
