#encoding:utf-8

import csdn_bayes as cbc

type = []
fp = open("doc/type_list.txt","r")
for doc in fp.readlines():
    type.append(doc)

classifiedNum = cbc.testingBayes()
#print "the text is classified as:",str(type[classifiedNum]).decode("utf-8")
result = str(type[classifiedNum])

print result