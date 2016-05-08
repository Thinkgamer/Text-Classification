#coding:utf-8

#第一部分：得到首页博客专家各个系列链接
#===============================================================================

import urllib2
from bs4 import BeautifulSoup
import os


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

def getText(href,count):   #得到博客内容和博主的相关信息
    soup = BeautifulSoup(getPage(href))
    div = soup.find("div",id="article_details",class_="details")
    #print div
    
#写博文标签---------------------------------------
    tag = div.find("div",class_="tag2box")             #文章标签
    if tag:
        for a in tag.findAll("a"): 
            #print a.get_text()                          #标签
            aTag = a.get_text()
            fp = open("%s\\tag.txt" % count,"a")
            fp.write(aTag.encode('utf-8'))
            fp.write("\n")
            fp.close()
#写博文标题和内容-----------------------------------------------------   
    title = div.find("div",class_="article_title")  #文章标题
    content = div.find("div",id="article_content",class_="article_content") #内容
    titleName = title.h1.span.a.get_text().strip()       #标题
    #print titleName
    cont = content.get_text()   
    #print cont                       #内容
    fp = open("%s\\content.txt" % count,"a")
    fp.write(titleName.encode('utf-8'))
    fp.write(cont.encode('utf-8'))
    fp.close()
#写博主的访问量排名等--------------------------------------------------
    div = soup.find("div",id="panel_Profile",class_="panel")
    if div:
        ul_1 = div.find("ul",id = "blog_rank")
        
        fp = open("%s\\aother.txt" % count,"a")
        ul_1_List = ul_1.findAll("li")
        visit = ul_1_List[0].get_text()
        fp.write(visit.encode("utf-8"))
        fp.write("\n")
        #print ul_1_List[0].get_text()                 #访问量

        score = ul_1_List[0].get_text()
        fp.write(score.encode("utf-8"))
        fp.write("\n")
        #print ul_1_List[0].get_text()                   #积分

        num = ul_1_List[3].get_text()
        fp.write(num.encode("utf-8"))
        fp.write("\n")
        #print ul_1_List[3].get_text()                 #排名
  
        ul_2 = div.find("ul",id = "blog_statistics")
        ul_2_List = ul_2.findAll("li")
        
        #print ul_2_List[0].get_text()        #原创文章数
        ower = ul_2_List[0].get_text()
        fp.write(ower.encode("utf-8"))
        fp.write("\n")
        
        #print ul_2_List[1].get_text()           #转载文章数 
        fromAnother = ul_2_List[2].get_text()
        fp.write(fromAnother.encode("utf-8"))
        fp.write("\n")
        
        #print ul_2_List[2].get_text()             #译文文章数
        translator = ul_2_List[2].get_text()
        fp.write(translator.encode("utf-8"))
        fp.write("\n")
        
        #print ul_2_List[3].get_text()             #评论条数
        talk = ul_2_List[3].get_text()
        fp.write(talk.encode("utf-8"))
        fp.write("\n\n")
        fp.close()
#------------------------------------------------------------------------


if __name__=="__main__":
    for count in range(10,11):
        fp = open("%s.txt" % count,"r")
        hrefList = fp.readlines()
        for href in hrefList:
            print href.strip()
            getText(href.strip(),count)
        print count , "is  Ok ==========================================="
