#coding:utf-8
from numpy import *
import operator


#给出训练数据和所对应的类别
def createDataSet():
    group=array([[1.0,0.9],[1.0,1.0],[0.1,0.2],[0.0,0.1]])
    labels=['A','A','B','B']
    return group,labels

#k-nearest neighbor函数编写
def classify(imput,dataSet,label,k):


    #1.计算欧氏距离


    dataSize=dataSet.shape[0]
    #tile(a,b)对a重复输出b次；
    #在行上重复input的datasize次，在列上重复1次，输出应当为datasize行，1列，重复元素为input；
    diff=tile(input,(dataSize,1))-dataSet
    # **是乘方的含义
    sqdiff=diff**2
    #将行向量相加；
    squareDist=sum(sqdiff,axis=1)
    #计算欧氏距离
    dist=squareDist**0.5
    #argsort()函数是对数据进行升序排列，并返回索引Index，注意从0开始，结束是n-1；
    sortedDistIndex=argsort(dist)


    #2。排序并选取前k个


    classCount={}
    for i in range(k):
        #选取排序中的前k个邻居
        voteLabel=label[sortedDistIndex[i]]
        #统计他们所属类别个数
        classCount[voteLabel]=classCount.get(voteLabel,0)+1
    #找出上述类别中样本个数最多的类，返回该类



    #3。找出这k个类中所占最多的类；



    maxCount=0
    for key ,value in classCount.items():
        if value > maxCount:
            maxCount=value
            classes=key

    return classes



#test
input=array([0.1,0.3])
k=4
dataSet,labels=createDataSet()
outputLabel=classify(input,dataSet,labels,k)
print "your input belongs to type:"," ' ",outputLabel," ' "

#注意，文件命名时候不要出现-，否则程序报错