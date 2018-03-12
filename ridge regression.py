# coding:utf-8

# 本代码可以运行
from numpy import *
import matplotlib.pyplot as plt



# 函数1：加载数据集,打开由tab键分割的txt,
def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t')) - 1
    dataMat = [];
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat


#系数计算：
def ridgeRegres(xMat,yMat,lamda=0.2):
    xTx=xMat.T*xMat
    denom=xTx+eye(shape(xMat)[1])*lamda
    if linalg.det(denom)==0.0:
        print("Wrong!")
        return
    ws=denom.I*(xMat.T*yMat)
    return ws

#在一组lambda上测试：
def ridgeTest(xArr,yArr):
    xMat=mat(xArr)
    yMat=mat(yArr).T
    yMean=mean(yMat,0)
    yMat=yMat-yMean
    xMeans=mean(xMat,0)
    xVar=var(xMat,0)
    xMat=(xMat-xMeans)/xVar          #数据标准化

    numTestPts=30
    wMat=zeros((numTestPts,shape(xMat)[1]))
    for i in range(numTestPts):
        ws=ridgeRegres(xMat,yMat,exp(i-10))
        wMat[i,:]=ws.T
    return wMat



xArr,yArr=loadDataSet("/Users/wangjian/Desktop/abalone.txt")
ridgeWeights=ridgeTest(xArr,yArr)
print (ridgeWeights)


def showRidge():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(ridgeWeights)
    plt.show()


showRidge()