#encoding:utf-8

import CSDN

type = ['移动开发','Web前端','架构设计','编程语言','互联网',\
            '数据库','系统运维','云计算','研发管理','综合']
classifiedNum = CSDN.testingBayes()
#print "the text is classified as:",str(type[classifiedNum]).decode("utf-8")
result = str(type[classifiedNum])
print result
