#encoding:utf-8
'''
Created on 2015��8��29��

@author: Administrator
'''

for i in range(1,11):
    print i
    fpRead = open("tag\%s.txt" % i,"r")
    wordList = fpRead.readlines()
    for j in range(len(wordList)):
        word = []
        word = wordList[j].split("\t")
        if len(word[0])>2 and len(word[0]) <10:
            if int(word[1].strip())>1:
                fpWrite = open("tagDispose\%s.txt" % i,"a")
                fpWrite.write(word[0])
                fpWrite.write("\n")

    fpRead.close()
    fpWrite.close()
