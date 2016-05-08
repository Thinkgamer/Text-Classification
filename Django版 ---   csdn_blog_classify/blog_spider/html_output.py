#coding:utf8
import MySQLdb
import os
class HtmlOutput(object):

    def __init__(self):
        pass

    def output_db(self,blog_list):
        conn = MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="root",db="spider")
        cursor = conn.cursor()
        for blog in blog_list:
            title = blog['title'];href = blog['url'];
            cate = blog['cate']; content = blog['content']
            sql = "insert into csdn_blog(title,href,cate,content) values(%s,%s,%s,%s)"
            param = (title,href,cate,content)
            n = cursor.execute(sql,param)
            print n
            cursor.execute(sql)
            conn.commit()
        cursor.close()
        conn.close()
        print "本页写入数据库OK"

    def output(self,blog_list,url):
        #创建以该作者命名的文件夹
        title = url.split("/")[3].encode('utf-8')
        if not os.path.exists("%s" % title):
            os.mkdir("%s" % title)

        for blog in blog_list:
            #构建类别的列表
            cate_list = []
            name = blog['title'].encode('utf-8').lstrip().rstrip()
            name = name.replace('\n',' ').replace('\r',' ').replace('\\',' ').replace(',',' ').replace('/',' ').replace('//',' ')
            wjj_cate = blog['cate'].encode('utf-8').lstrip().rstrip()
            wjj_cate=wjj_cate.replace('\n',' ').replace('\r',' ').replace('\\',' ').replace(',',' ').replace('/',' ').replace('//',' ')
            #将某类文章写入到同一个文件内
            fout = open("%s/%s.txt" % (title,wjj_cate),"a")
            fout.write(blog['title'].encode('utf-8')+"\n")
            fout.write(blog['content'].encode('utf-8')+"\n")

            fout.close()

        print "本页写入数据库OK"