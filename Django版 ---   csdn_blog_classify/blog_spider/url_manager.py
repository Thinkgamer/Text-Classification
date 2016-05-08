#coding:utf8
'''
urls
添加新的url  add_url
url出栈     pop_url
得到总的页数  get_all_page
'''

import html_download
import html_parser

class UrlManager(object):

    urls = set()

    def __init__(self):
        self.download = html_download.HtmlDownload()
        self.parser = html_parser.HtmlParser()

    def get_all_page(self,root_url):
        if root_url is None:
            return

        html_content = self.download.down(root_url)
        blog_message = self.parser.parser(html_content)

    def add_url(self,url):
        pass

    def pop_url(self):
        pass