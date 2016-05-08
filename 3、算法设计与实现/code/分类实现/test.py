#encoding=utf-8  

import jieba

fp = open("test.txt",'r')
wordList = []
strDocList = fp.readlines()
for strDoc in strDocList:
    print strDoc.strip()
    full_seg = jieba.cut(strDoc.strip(),cut_all = True)
    for word in full_seg:
        if len(word)>0:
            print word
            if ord(word[0])<127:
                wordList.append(word.lower())
            else:
                wordList.append(word)
print wordList
