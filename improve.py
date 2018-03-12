# -*- coding: utf-8 -*-

from numpy import *
import matplotlib.pyplot as plt

# 函数1，打开文本并逐行读取，每行前两个值为X1,X2，第三个值为数据对应的标签；
def loadDataSet():
    dataMat = []; labelMat = []
    fr = open('/Users/wangjian/Desktop/testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat


# 函数2:sigmoid函数
def sigmoid(inX):
    return 1.0 / (1 + exp(-inX))

#随机梯度上升函数：区别在于--h和error均为数值，非向量；不需要矩阵转置，均为numpy数组
def stocGradAscent0(dataMatrix, classLabels):
    dataMatrix=array(dataMatrix)
    m,n = shape(dataMatrix)
    alpha = 0.01
    weights = ones(n)   #initialize to all ones
    for i in range(m):
        h = sigmoid(sum(dataMatrix[i]*weights))
        error = labelMat[i] - h
        weights = weights + alpha * error * dataMatrix[i]
    return weights


def plotBestFit(weights,dataMatrix,labelMat):
    import matplotlib.pyplot as plt
    dataMat,labelMat=loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0]-weights[1] * x)/weights[2]
    ax.plot(x, y)
    plt.xlabel('X1'); plt.ylabel('X2');
    plt.show()

dataMatrix, labelMat = loadDataSet()
weight = stocGradAscent0(dataMatrix, labelMat)
print weight
plotBestFit(weight, dataMatrix, labelMat)

#评价：错过三分之一的样本，原因是最初的梯度上升算法迭代了500次
#因此将随即梯度再迭代200次试试


