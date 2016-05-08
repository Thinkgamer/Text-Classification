#coding:utf-8
import os
import jieba
import blog_cate_write

class BlogFenci(object):

    def __init__(self):
        self.write = blog_cate_write.CateWrite()

    def sort(self,cate_list):
        cate_dic = {}
        for cate in cate_list:
            if cate in cate_dic.keys():
                cate_dic[cate] += 1
            else:
                cate_dic[cate] = 1

        cate_new_list = sorted(cate_dic.items(),key = lambda cate_dic:-cate_dic[1])


        return cate_new_list

    def fenci(self,doc):
        if doc is None:
            return
        print doc
        cate_list = []
        fp = open("gamer_gyt/%s" % doc,"r")
        content_list = fp.readlines()
        #print content_list
        fp.close()
        for content in content_list:
            line_list = jieba.cut(content.lstrip().rstrip(),cut_all=True)
            for line in line_list:
                if len(line) >1  and len(line) <4:
                    #print line
                    cate_list.append(line)

        return self.sort(cate_list)

    def open(self):
        i = 0
        #遍历作者文件夹下所有类别文件，并分词处理
        doc_list  =os.listdir(os.getcwd() + "/gamer_gyt")
        for doc in doc_list:
            self.write.write(self.fenci(doc),i)
            i += 1
            fp = open("type_list.txt","a")
            fp.write(doc[:-4] + "\n")
            fp.close()

    def fmain(self):
        self.open()