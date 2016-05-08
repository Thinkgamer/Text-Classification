#coding:utf8
import urllib2
import requests

class HtmlDownload(object):
    def __init__(self):
        pass

    def down(self,url):
        if url is None:
            return

        header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        response = urllib2.Request(url,headers=header)
        page = urllib2.urlopen(response).read()

        if  urllib2.urlopen(response).getcode()!= 200:
            return None

        return page