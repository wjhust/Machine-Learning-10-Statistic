#coding:utf-8
from numpy import *

#同样的，先定义词库，相当于对词库中的词进行分类
def loadDataSet():
    postingList=[['my','dog','has','flea',\
                  'problems','help','please'],
                 ['maybe','not','take','him',\
                  'to','dog','park','stupid'],
                  ['my','dalmation','is','so','cute',
                  'I','love','him'],
                 ['stop','posting','stupid','worthless','garbage'],
                 ['my','licks','ate','my','steak','how',\
                  'to','stop','him'],
                 ['quit','buying','worthless','dog','food','stupid']]
    classVec=[0,1,0,1,0,1]
    return postingList,classVec

#函数1。统计所有文档中出现的词条列表：
def createVocabList(dataSet):
    #先建立一个存放词条的集合
    vocabSet=set([])
    #遍历文档集合的每一个文档
    for document in dataSet:
        #set函数先将document转化为集合形式，保证唯一性；
        # 再和vocabSet取并集
        vocabSet=vocabSet|set(document)
        #转化为列表，方便处理
    return list(vocabSet)

#函数2。根据词条在文档中是否出现（出现是1，未出现为0），并转化文档为词条向量
#调用了函数1
def setOfWords2Vec(vocabSet,inputSet):
    #新建一个长度为vocabSet的列表，并且初始化为0
    returnVec=[0]*len(vocabSet)
    #遍历词条
    for word in inputSet:
        #如果在词条历表中出现
        if word in vocabSet:
            #获取当前word的索引（下标），并将之从0改为1
            returnVec[vocabSet.index(word)]=1
        else:print 'not in dictionary'

    return returnVec


#函数3。定义计算概率函数：
def trainNBO(trainMatrix,trainCategory):
   #获取文档矩阵中的文档数目
    numTrainDocs=len(trainMatrix)
   #获取向量的此条长度
    numWords=len(trainMatrix[0])
   #所有文档中属于类1所占的比例
    pAbusive=sum(trainCategory)/float(numTrainDocs)
   #创建长度为词条长度的列表
    p0Num=zeros(numWords)
    p1Num=zeros(numWords)
    p0Denom=2.0
    p1Denom=2.0
   #遍历词条
    for i in range(numTrainDocs):
        #若标签为1
        if trainCategory[i]==1:
            #统计1类中各个词条出现的次数
            p1Num+=trainMatrix[i]
            #统计1类的所有单词数目
            p1Denom+=sum(trainMatrix[i])
        else:
            #统计0类的
            p0Num+=trainMatrix[i]
            p0Denom+=sum(trainMatrix[i])
    #计算条件概率p(wi|c1)和p(wi|c0)
    p1Vect=p1Num/p1Denom
    p0Vect=p0Num/p0Denom
    return p0Vect,p1Vect,pAbusive
    print  p0Vect,p1Vect,pAbusive
#算法改进：
#1.为降低0的影响，所有词初始化为1，并将分母初始化为2；
#p0Denom=2.0;p1Denom=2.0;
#2.为解决下溢问题，采取自然对数处理；
#p0Vect=log(p0Num/p0Denom);p1Vect=log(p1Num/p1Denom)




#函数4。朴素贝叶斯分类
#vec2Classify:待测试分类的词条向量
#p0Vec:类别0所有文档中各个词条出现的频数p(wi|c0)
#p1Vec:类别1所有文档中各个词条出现的频数p(wi|c1)
#pClass1:类别为1的文档占文档总数比例
def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    p1=sum(vec2Classify*p1Vec)+log(pClass1)
    p0=sum(vec2Classify*p0Vec)+log(1-pClass1)
    if p1>p0:
        return 1
    else:
        return 0

#分类测试整体函数，调用函数2，函数3，
def testingNB():
    listOPosts,listClasses=loadDataSet()
    myVocabList=createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList,postinDoc)),
    p0V,p1V,pAb=trainNBO(array(trainMat),array(listClasses))
    testEntry=['dog','my','dalmation']
    thisDoc=array(setOfWords2Vec(myVocabList,testEntry))
    print testEntry,'classified as:',classifyNB(thisDoc,p0V,p1V,pAb)
    testEntry1=['ate','garbage']
    thisDoc1=array(setOfWords2Vec(myVocabList,testEntry1))
    print testEntry1,'classified as:',classifyNB(thisDoc1,p0V,p1V,pAb)

#将文档转为词袋
def bagOfWordsVecMN(vocabList,inputSet):
    #词袋向量
    returnVec=[0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]+=1
    return returnVec


#test
output=testingNB()
print output





