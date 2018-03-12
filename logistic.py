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


# 函数3:梯度上升算法
def gradAscent(dataMatIn, classLabels):
    # dataMatIn是2维numpy数组，每列代表不同特征，每行为训练样本
    # test数据包含两个特征X1，X2，加上第0维特征X0，因此dataMatIn存放100X3矩阵；
    # mat帮助转化为numpy矩阵
    dataMatrix = mat(dataMatIn)  # 将数组转为矩阵
    labelMat = mat(classLabels).transpose()
    m, n = shape(dataMatrix)  # 返回矩阵的行和列
    # 步长
    alpha = 0.001
    # 迭代次数
    maxCycles = 500
    weights = ones((n, 1))
    # 开始迭代：
    for k in range(0,maxCycles):
        # h是列向量
        h = sigmoid(dataMatrix * weights)  # matrix mult
        error = labelMat - h # vector subtraction
        weights = weights + alpha * dataMatrix.transpose() * error  # matrix mult
    return weights

# 函数4:画出数据集和拟合直线：
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
    y = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x, y)
    plt.xlabel('X1'); plt.ylabel('X2');
    plt.show()

if __name__ == "__main__":
    dataMatrix, labelMat = loadDataSet()
    weight = gradAscent(dataMatrix, labelMat)
    plotBestFit(weight, dataMatrix, labelMat)

############该结果无法运行，原因是迭代次数超过最大值，基本是算法太差，超过迭代限制，因此需要改进，不知道网上是怎么运行出来的










































