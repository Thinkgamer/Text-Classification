#coding:utf8

from numpy import *

#构造文档列表和标签列表
def loadDataSet():
    wordList = []
    typeList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]#0~19代表20种类型
    for i in range(0,20):
        lineList2 = []
        fp = open("doc/%s.txt" % i,"r")
        lineList1 = fp.readlines()
        fp.close()
        for j in range(len(lineList1)):
            strWord = lineList1[j].strip()
            if ord(strWord[0])<127:
                strWord= strWord.lower()
            lineList2.append(strWord)
        wordList.append(lineList2)
    return wordList,typeList

#求所有文档的并集
def createBingjiList(wordList):
    bingjiList = set([])        #调用set方法创建一个空集
    for doc in wordList:
        bingjiList = bingjiList | set(doc)   #创建两个集合并集
    return list(bingjiList)

#如果一个文档在该词库中，那么出现该单词的位置由0变成1
def setOfWords(bingjiList,inputList):
    returnList = [0] * len(bingjiList)          #创建以一个所有元素都为0的向量
    for word in inputList:
        if word in bingjiList:
            returnList[bingjiList.index(word)] =1
    return returnList


#朴素贝叶斯分类器训练集
def trainBayes(trainMatrix,trainTag):
    pA = []      #任意文档属于0-9类别的概率
    for i in range(0,20):
        pA.append(trainTag.count(i)/float(len(trainTag)))
    numTrainDocs= len(trainMatrix)    #文档矩阵的长度
    numWords = len(trainMatrix[0])     #文档矩阵第一行的单词个数
    #初始化每个标签对应的矩阵，总数，避免某一个概率为0最后乘积为0，so初始化分子为1分母为2
    p0Num = ones(numWords);p0Denom = 2.0
    p1Num = ones(numWords);p1Denom = 2.0
    p2Num = ones(numWords);p2Denom = 2.0
    p3Num = ones(numWords);p3Denom = 2.0
    p4Num = ones(numWords);p4Denom = 2.0
    p5Num = ones(numWords);p5Denom = 2.0
    p6Num = ones(numWords);p6Denom = 2.0
    p7Num = ones(numWords);p7Denom = 2.0
    p8Num = ones(numWords);p8Denom = 2.0
    p9Num = ones(numWords);p9Denom = 2.0
    p10Num = ones(numWords);p10Denom = 2.0
    p11Num = ones(numWords);p11Denom = 2.0
    p12Num = ones(numWords);p12Denom = 2.0
    p13Num = ones(numWords);p13Denom = 2.0
    p14Num = ones(numWords);p14Denom = 2.0
    p15Num = ones(numWords);p15Denom = 2.0
    p16Num = ones(numWords);p16Denom = 2.0
    p17Num = ones(numWords);p17Denom = 2.0
    p18Num = ones(numWords);p18Denom = 2.0
    p19Num = ones(numWords);p19Denom = 2.0
    for i in range(0,numTrainDocs):
        if trainTag[i] == 0:
            p0Num +=trainMatrix[i];p0Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 1:
            p1Num +=trainMatrix[i];p1Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 2:
             p2Num +=trainMatrix[i];p2Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 3:
            p3Num +=trainMatrix[i];p3Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 4:
            p4Num +=trainMatrix[i];p4Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 5:
            p5Num +=trainMatrix[i];p5Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 6:
            p6Num +=trainMatrix[i];p6Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 7:
            p7Num +=trainMatrix[i];p7Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 8:
            p8Num +=trainMatrix[i];p8Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 9:
            p9Num +=trainMatrix[i];p9Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 10:
            p10Num +=trainMatrix[i];p10Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 11:
            p11Num +=trainMatrix[i];p11Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 12:
            p12Num +=trainMatrix[i];p12Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 13:
            p13Num +=trainMatrix[i];p13Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 14:
            p14Num +=trainMatrix[i];p14Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 15:
            p15Num +=trainMatrix[i];p15Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 16:
            p16Num +=trainMatrix[i];p16Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 17:
            p17Num +=trainMatrix[i];p17Denom +=sum(trainMatrix[i])
        elif trainTag[i] == 18:
            p18Num +=trainMatrix[i];p18Denom +=sum(trainMatrix[i])
        else:
            p19Num +=trainMatrix[i];p19Denom +=sum(trainMatrix[i])
    pV = []
    pV0 = log(p0Num/p0Denom);pV.append(pV0)
    pV1 = log(p1Num/p1Denom);pV.append(pV1)
    pV2 = log(p2Num/p2Denom);pV.append(pV2)
    pV3 = log(p3Num/p3Denom);pV.append(pV3)
    pV4 = log(p4Num/p4Denom);pV.append(pV4)
    pV5 = log(p5Num/p5Denom);pV.append(pV5)
    pV6 = log(p6Num/p6Denom);pV.append(pV6)
    pV7 = log(p7Num/p7Denom);pV.append(pV7)
    pV8 = log(p8Num/p8Denom);pV.append(pV8)
    pV9 = log(p9Num/p9Denom);pV.append(pV9)
    pV10 = log(p10Num/p10Denom);pV.append(pV10)
    pV11 = log(p11Num/p11Denom);pV.append(pV11)
    pV12 = log(p12Num/p12Denom);pV.append(pV12)
    pV13 = log(p13Num/p13Denom);pV.append(pV13)
    pV14 = log(p14Num/p14Denom);pV.append(pV14)
    pV15 = log(p15Num/p15Denom);pV.append(pV15)
    pV16 = log(p16Num/p16Denom);pV.append(pV16)
    pV17 = log(p17Num/p17Denom);pV.append(pV17)
    pV18 = log(p18Num/p18Denom);pV.append(pV18)
    pV19 = log(p19Num/p19Denom);pV.append(pV19)

    return pA,pV

#朴素贝叶斯分类函数
def classifyBayes(testDoc,pV,pA):
    p0  = sum(testDoc * pV[0])  + log(pA[0])
    p1  = sum(testDoc * pV[1])  + log(pA[1])
    p2  = sum(testDoc * pV[2])  + log(pA[2])
    p3  = sum(testDoc * pV[3])  + log(pA[3])
    p4  = sum(testDoc * pV[4])  + log(pA[4])
    p5  = sum(testDoc * pV[5])  + log(pA[5])
    p6  = sum(testDoc * pV[6])  + log(pA[6])
    p7  = sum(testDoc * pV[7])  + log(pA[7])
    p8  = sum(testDoc * pV[8])  + log(pA[8])
    p9  = sum(testDoc * pV[9])  + log(pA[9])
    p10 = sum(testDoc * pV[10]) + log(pA[10])
    p11 = sum(testDoc * pV[11]) + log(pA[11])
    p12 = sum(testDoc * pV[12]) + log(pA[12])
    p13 = sum(testDoc * pV[13]) + log(pA[13])
    p14 = sum(testDoc * pV[14]) + log(pA[14])
    p15 = sum(testDoc * pV[15]) + log(pA[15])
    p16 = sum(testDoc * pV[16]) + log(pA[16])
    p17 = sum(testDoc * pV[17]) + log(pA[17])
    p18 = sum(testDoc * pV[18]) + log(pA[18])
    p19 = sum(testDoc * pV[19]) + log(pA[19])
    listValue = [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19]
    return listValue.index(max(listValue))

#从文本中得到数据
def getDoc():
    import jieba
    fp = open("content.txt",'r')
    wordList = []
    strDocList = fp.readlines()
    fp.close()
    for strDoc in strDocList:
        full_seg = jieba.cut(strDoc.strip(),cut_all = True)
        for word in full_seg:
            if len(word)>1:  #去除标点符号和单音节字
                if ord(word[0])<127:
                    wordList.append(word.lower())
                else:
                   wordList.append(word)
    return wordList

def testingBayes():
    wordList,typeList = loadDataSet()
    bingjiList = createBingjiList(wordList)
    trainMat = []   #创建一个空的列表
    for lineDoc in wordList:
        trainMat.append(setOfWords(bingjiList,lineDoc))#使用词向量来填充trainMat列表
    pA,pV = trainBayes(trainMat,typeList)
    testDoc = getDoc()      #从文本中得到数据
    thisList = array(setOfWords(bingjiList,testDoc))
    return classifyBayes(thisList,pV,pA)