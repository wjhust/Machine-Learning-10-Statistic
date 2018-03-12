#coding:utf-8
from math import log
import operator


#伪代码：
#1.定义好香农熵的函数
#2.定义好划分数据集的函数
#3.利用1，2，定义选取信息熵增益最大的函数
#4.定义返回信息增益最大的数据集编号的函数
#5.主函数--利用3，4，构建tree函数




#这里先定义好需要鉴别的数据集函数，后边直接用---待测试数据为dataSet
def createDataSet():
    dataSet=[[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    labels=['no surfacing','flippers']
    return dataSet,labels



#基本函数1.计算给定数据集的香农熵；
def calcShannonEnt(dataSet):
    numEntries=len(dataSet)
    labelCounts={}
    for featVec in dataSet:
        #获得标签
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        #统计该类标签下含有数据的个数
        labelCounts[currentLabel]+=1

    shannonEnt=0.0
    for key in labelCounts:
        #同类标签出现的概率
        prob=float(labelCounts[key])/numEntries
        #香农熵
        shannonEnt-=prob*log(prob,2)
    return shannonEnt

#test1
#data,labels=createDataSet()
data=[[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
#output=calcShannonEnt(data)
#print "the shannon ent is:",output



#基本函数2.划分数据集
def splitDataSet(dataSet,axis,value):
        retDataSet=[]
        for featVec in dataSet:
            if featVec[axis]==value:
               reducedFeatVec=featVec[:axis]
               reducedFeatVec.extend(featVec[axis+1:])
               retDataSet.append(reducedFeatVec)
        return retDataSet


#test2
#output1=splitDataSet(data,0,1)
#output2=splitDataSet(data,0,0)
#print output1
#print output2

#函数3：选取特征，划分数据集，计算最好的划分数据集的特征：
#调用函数2：对数据集进行划分；函数1，计算数据集的香农熵
def chooseBestFeatureToSplit(dataSet):
    #剩下的为特征个数：
    numFeatures=len(dataSet[0])-1
    #计算数据集的熵，由baseEntropy存储；
    baseEntropy=calcShannonEnt(dataSet)
    bestInfoGain=0.0;
    bestFeature=-1;
    for i in range(numFeatures):
        featList=[example[i] for example in dataSet]
        #set相当于set集合，用于以后的交，补，并等运算；
        uniqueVals=set(featList)
        newEntropy=0.0
        for value in uniqueVals:
            #计算每种划分方式的信息熵，特征i个，每个特征value个数值
            subDataSet=splitDataSet(dataSet,i,value)
            prob=len(subDataSet)/float(len(dataSet))
            newEntropy=prob*calcShannonEnt(subDataSet)
            #原来数据集的熵-划分后的新熵，infoGain是不同划分下的信息增益
            infoGain=baseEntropy-newEntropy
            #测试时候注意去掉注释print infoGain
            if(infoGain>bestInfoGain):
                bestInfoGain=infoGain
                #返回增益最大的划分所在的标签
                bestFeature=i
    return bestFeature

#test3
data,labels=createDataSet()
#output3=chooseBestFeatureToSplit(data)
#print output3



#函数4：找到出现次数最多的分类名称
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():classCount[vote]=0
        classCount[vote]+=1
        sortedClassCount=sorted(classCount.iteritems(),\
                                key=operator.itemgetter(1),reverse=True)
        return sortedClassCount[0][0]



#创建树--主函数，调用函数3-找出最佳分类集；函数4，返回出现次数最多的分类名称
def createTree(dataSet,labels):
    #将最后一行数据放到classList
    classList=[example[-1] for example in dataSet]
    if classList.count(classList[0])==len(classList):
        return classList[0]
    #若特征数为1的时候
    if len(dataSet[0])==1:
        #只需返回该特征值
        return majorityCnt(classList)
    bestFeat=chooseBestFeatureToSplit(dataSet)
    #print bestFeat
    bestFeatLabel=labels[bestFeat]
    myTree={bestFeatLabel:{}}
    del (labels[bestFeat])
    #第0个特征值
    featValues=[example[bestFeat] for example in dataSet]
    uniqueVals=set(featValues)
    for value in uniqueVals:
        subLabels=labels[:]
        myTree[bestFeatLabel][value]=createTree(splitDataSet\
                                                    (dataSet,bestFeat,value),subLabels)
    return myTree



#test4
#myTree=createTree(data,labels)
#print myTree



#############################################画图#######################################

#得到叶子节点的数目
def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':#这里说的只是二叉树吧？？应该？
            numLeafs +=getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs

#树的层数
def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':#一层只有一个dict
            thisDepth = 1 + getTreeDepth(secondDict[key])
            #print(123)
        else:
            thisDepth = 1
            #print(456)
        if thisDepth > maxDepth: maxDepth = thisDepth
    return maxDepth



#函数retrieveTree输出预先存储的树信息
#避免每次测试代码时都要从数据中创建树的麻烦
def retrieveTree(i):
    listOfTrees = [{'no surfacing':{0:'no',1:{'flippers':\
                                              {0:'no',1:'yes'}}}},
                   {'no surfacing':{0:'no',1:{'flippers':\
                    {0:{'head':{0:'no',1:'yes'}},1:'no'}}}}
                   ]
    return listOfTrees[i]

import matplotlib.pyplot as plt
decisionNode = dict(boxstyle = "sawtooth",fc="0.8")
leafNode = dict(boxstyle="round4",fc="0.8")
arrow_args = dict(arrowstyle="<-")

def plotNode(nodeTxt,centerPt,parentPt,nodeType):
    createPlot.ax1.annotate(nodeTxt,xy=parentPt,xycoords = 'axes fraction',
                            xytext=centerPt,textcoords='axes fraction',va="center",ha="center",bbox=nodeType,arrowprops=arrow_args)
'''
def createPlot():
    fig = plt.figure(1, facecolor='white')#创建一个新图形
    fig.clf()#清空绘图区
    createPlot.axl = plt.subplot(111,frameon=False)
    #在图中绘制两个代表不同类型的树节点
    plotNode('a decision node',(0.5,0.1),(0.1,0.5),decisionNode)
    plotNode('a leaf node',(0.8,0.1),(0.3,0.8),leafNode)
    plt.show()
'''
#画二叉树，实现和上面代码相似的功能
#1、计算父节点和子节点的中间位置
def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0]-cntrPt[0])/2.0 + cntrPt[0]
    yMid = (parentPt[1]-cntrPt[1])/2.0 + cntrPt[1]
    createPlot.ax1.text(xMid,yMid,txtString)#??
#绘制树的很多工作都是在这个函数中完成
def plotTree(myTree,parentPt,nodeTxt):
    #计算树的宽和高
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = myTree.keys()[0]
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW,\
              plotTree.yOff)#??
    plotMidText(cntrPt,parentPt,nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key],cntrPt,str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff,plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff,plotTree.yOff),cntrPt,str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD

def createPlot(inTree):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[],yticks=[])
    createPlot.ax1 = plt.subplot(111,frameon=False, **axprops)
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5/plotTree.totalW;plotTree.yOff = 1.0;
    print(plotTree.xOff,plotTree.yOff)
    #plotTree.xOff = 1.0;plotTree.yOff = 1.0;
    plotTree(inTree, (0.5,1.0), '')
    plt.show()




myTree=retrieveTree(0)
output5=createPlot(myTree)
print output5
