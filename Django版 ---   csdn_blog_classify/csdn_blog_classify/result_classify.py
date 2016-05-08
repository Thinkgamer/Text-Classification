#encoding:utf-8

import csdn_bayes as cbc

def result():
    type = []
    fp = open("csdn_blog_classify/doc/type_list.txt","r")
    for doc in fp.readlines():
        type.append(doc)
    fp.close()
    classifiedNum = cbc.testingBayes()
    #print "the text is classified as:",str(type[classifiedNum]).decode("utf-8")
    result = str(type[classifiedNum])

    return result