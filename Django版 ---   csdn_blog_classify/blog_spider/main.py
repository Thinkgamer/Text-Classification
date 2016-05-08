#coding:utf8
import url_manager
import html_download
import html_parser
import html_output
import time

class spiderMain(object):

    def __init__(self):
        self.parser = html_parser.HtmlParser()
        self.download = html_download.HtmlDownload()
        self.output = html_output.HtmlOutput()

    def start(self,url,root_url):
        page = self.download.down(url)
        blog_list = self.parser.parser(page)
        self.output.output(blog_list,root_url)


if __name__=="__main__":

    root_url = "http://blog.csdn.net/gamer_gyt/article/list/1"
    obj_spider = spiderMain()
    #try:
        #获取一个人blog的总的页数
    blog_page_num = obj_spider.parser.get_page_num(root_url)
    print "该作者的blog共有 %d 页" % blog_page_num
        #循环得到all blog
    for num in range(1,blog_page_num+1):
        url = "http://blog.csdn.net/gamer_gyt/article/list/" + str(num)
        print "第 %s 页开始爬取" % num, "URL:",url
        obj_spider.start(url,root_url)
        time.sleep(3)
#    except Exception as e:
#        print "抓包失败：",e