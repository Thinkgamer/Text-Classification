#coding:utf8
from bs4 import BeautifulSoup
import re,urllib2
import html_download

class HtmlParser(object):
    def __init__(self):
        self.download = html_download.HtmlDownload()

    def get_one_blog(self,url):
        if url is None:
            return
        page = self.download.down(url)
        soup = BeautifulSoup(page,"lxml",from_encoding="utf-8")
        #<div id="article_content" class="article_content">
        content = soup.find('div',id='article_content',class_='article_content').get_text()
        try:
            cate = soup.find('div',class_="category_r").span.get_text()
        except:
            cate = "NULL"
        finally:
            return cate,content
        

    def get_page_num(self,url):

        page = self.download.down(url)

        soup = BeautifulSoup(page,"lxml",from_encoding="utf-8")
        #<div id="papelist" class="pagelist"><span> 121条数据  共9页</span>
        page_list = soup.find('div',id='papelist')
        span = page_list.span.get_text().split(' ')
        num = re.findall(r'\d+',span[3])
        return int(num[0])

    def get_blog_mess(self,soup):
        a_list = []
        #<div id="article_list" class="list">
        div_all = soup.find('div',id='article_list',class_='list')

        div_list = div_all.find_all('div',class_='list_item article_item')
        for div in div_list:
            blog_m = {}
            blog_title = div.find('h1'); blog_m['title'] = blog_title.get_text().lstrip().rstrip();
            print "Title:" ,blog_m['title']
            blog_url = div.find_all('a')[0]; blog_m['url'] = "http://blog.csdn.net" + blog_url.get('href');
            #print "href:",blog_m['url']
            blog_cate,blog_content = self.get_one_blog(blog_m['url'])
            blog_m['cate']=blog_cate; blog_m['content'] = blog_content
            #print "cate:",blog_m['cate']
            #print "content:"," 此处省略一万字\n==================================\n"
            a_list.append(blog_m)

        return a_list

    def parser(self,content):
        page_soup = BeautifulSoup(content,"lxml",from_encoding="utf-8")

        if len(page_soup)==0:
            return

        blog_list = self.get_blog_mess(page_soup)
        return blog_list


