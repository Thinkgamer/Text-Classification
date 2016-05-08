#coding:utf-8

#第二部分：爬取每个系列的所有热门文章URL
#===============================================================================

import urllib2
from bs4 import BeautifulSoup
import re


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

def getPageNum(href):      #得到总的页数
    num =0
    page = getPage(href)
    soup = BeautifulSoup(page)
    div = soup.find('div',class_='page_nav')
    if len(div)>1:     #排除只有一页的情况
        result = div.span.get_text().split(' ')
        list_num = re.findall("[0-9]{1}",result[3])
        for i in range(len(list_num)):
            num = num*10 + int(list_num[i]) #计算总的页数
        return num
    else:
        return 1

def getAllUrl(href,count):
    soup = BeautifulSoup(getPage(href))   #代码规范化
    div = soup.find("div",class_="page_right")
    div_list = div.findAll("div","blog_list")
    for d in div_list:
       # print d.a.get('href')
        fp = open("%s.txt" % count,"a")
        fp.write(d.a.get('href') + "\n")
        fp.close()
    

if __name__=="__main__":
    count = 1
    fp = open("every.txt","r")
    hrefList = fp.readlines()
    for href in hrefList:
        numPage = getPageNum(href)
        #print numPage
        for num in range(numPage):
            getAllUrl(href.strip()+"?&page=" + str(num),count)  #strip()接受回车符
        print "第 %s 个类别URL 捉取完毕！" % count
        count += 1
        
       
    fp.close()
