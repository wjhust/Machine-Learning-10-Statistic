# coding:utf-8

#本代码运行不出来，可以使用anaconda中的Spyder进行画图
from numpy import *
import matplotlib.pyplot as plt

#函数1：加载数据集,打开由tab键分割的txt,
def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t')) - 1 #get number of fields
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat

#函数2：计算最佳拟合曲线，先读入x,y再计算xTx,等价于判断是否可逆；
def standRegress(xArr,yArr):
    xMat=mat(xArr)
    yMat=mat(yArr).T    #.T代表转置矩阵
    xTx=xMat.T*xMat
#numpy提供函数库linalg,包含很多函数；
    if linalg.det(xTx)==0.0: #linalg.det（xTx)为计算行列式
        print "Wrong!"
    ws=xTx.I*(xMat.T*yMat)    #.I为逆
    return ws


#test1:
xArr,yArr=loadDataSet("/Users/wangjian/Desktop/ex0.txt")
ws=standRegress(xArr,yArr)
print ("ws(相关系数）：" , ws)

#函数3：画图函数
def show():
    xMat=mat(xArr)
    yMat=mat(yArr)
    yHat=xMat*ws  #预测值的计算
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,0].flatten().A[0])
    xCopy=xMat.copy()
    xCopy.sort(0)
    yHat=xCopy*ws
    ax.plot(xCopy[:,1],yHat)
    plt.show()
show()

yHat=mat(xArr)*ws
print("相关性：",corrcoef(yHat.T,mat(yArr)))


