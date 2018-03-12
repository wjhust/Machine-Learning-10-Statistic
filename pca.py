#coding=utf-8
from numpy import *

def loadDataSet(filename,delim = "\t"):
    fr = open(filename)
    stringArr = [line.strip().split(delim) for line in fr.readlines()]
    datArr = [map(float, line) for line in stringArr]
    return mat(datArr)


def pca(dataMat,topNfeat=9999999):
    #求均值
    meanVals=mean(dataMat,axis=0)
    #去均值：数据中心化
    meanRemoved=dataMat - meanVals
    #计算cov阵
    covMat=cov(meanRemoved,rowvar=0)
    #求特征值
    eigVals,eigVects=linalg.eig(mat(covMat))
    #排序
    eigValInd=argsort(eigVals)
    #逆序处理，为了得到前N个最大特横向量
    eigValInd=eigValInd[:-(topNfeat+1):-1]
    redEigVects=eigVects[:,eigValInd]
    #转换数据到新的空间
    lowDDataMat=meanRemoved*redEigVects
    reconMat=(lowDDataMat*redEigVects.T)+meanVals
    return lowDDataMat,reconMat

dataMat=loadDataSet('/Users/wangjian/Desktop/testSet.txt')
lowDmat,reconMat=pca(dataMat,1)
print shape(lowDmat)


#show
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(dataMat[:,0].flatten().A[0], dataMat[:,1].flatten().A[0], marker='^',  s = 90 )
ax.scatter(reconMat[:,0].flatten().A[0], reconMat[:,1].flatten().A[0],marker='o', s = 50 , c ='red' )