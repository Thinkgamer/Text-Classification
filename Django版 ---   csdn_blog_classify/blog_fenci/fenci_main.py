#coding:utf8
import blog_fenci

class fenMain(object):

    def __init__(self):
        self.fenci = blog_fenci.BlogFenci()

    def start(self):
        self.fenci.fmain()


if __name__=="__main__":
    fenmain = fenMain()
    fenmain.start()