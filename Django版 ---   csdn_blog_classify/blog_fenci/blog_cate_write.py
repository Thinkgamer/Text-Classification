#coding:utf-8
import os

class CateWrite(object):
    def __init__(self):
        pass

    def write(self,cate_list,num):
        i = 0
        if not os.path.exists("tagpose"):
            os.mkdir("tagpose")

        fp = open("tagpose/%s.txt" % num ,"a")
        for cate in cate_list:
            if i < 50:
                #print cate[0],"------",cate[1]
                fp.write(cate[0].encode("utf8")+"\n")
                i += 1
        fp.close()