# utf-8
from numpy import *
#导入辅助函数

#文本数据解析函数
def loadDataSet(fileName):  # general function to parse tab -delimited floats
    dataMat = []  # assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
#将每一行数据映射成float型
        fltLine = map(float, curLine)  # map all elements to float()
        dataMat.append(fltLine)
    return dataMat

#计算欧氏距离
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))  # la.norm(vecA-vecB)

#初始化k个质心，随机；
def randCent(dataSet, k):
    #获得数据样本的维度
    n = shape(dataSet)[1]
    #初始化一个（k,n）矩阵
    centroids = mat(zeros((k, n)))  # create centroid mat
    #遍历数据集的每一个维度
    for j in range(n):  # create random cluster centers, within bounds of each dimension
        #得到该列数据的最小值
        minJ = min(dataSet[:, j])
        #得到该列数据的范围
        rangeJ = float(max(dataSet[:, j]) - minJ)
        #k个质心向量的第j维数据随机位于（最大值，最小值）内的某一值
        centroids[:, j] = mat(minJ + rangeJ * random.rand(k, 1))
    #返回k个质心向量
    return centroids

# k-means均值聚类
#dataset数据集，用户指定k个类，distMeans是距离计算方法：欧氏距离，createCent是获取k个质心方法：随机获取
def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    #获取样本数
    m = shape(dataSet)[0]
    #初始化（m,2)矩阵
    clusterAssment = mat(zeros((m, 2)))  # create mat to assign data points
    #创建k个质心向量
    # to a centroid, also holds SE of each point
    centroids = createCent(dataSet, k)
    #聚类结果是否发生变化的布尔类型
    clusterChanged = True
    #只要聚类结果一直变化，就执行聚类算法，直至结果不变
    while clusterChanged:
        clusterChanged = False
        for i in range(m):  # for each data point assign it to the closest centroid
            #初始化最小距离最正无穷，最小距离对应索引为-1
            minDist = inf;
            minIndex = -1
            #循环k个类的质心
            for j in range(k):
                #计算欧氏距离
                distJI = distMeas(centroids[j, :], dataSet[i, :])
                if distJI < minDist:
                    #计算当前距离为最小距离，最小距离对应索引为j个类
                    minDist = distJI;
                    minIndex = j
            #如果结果发生变化，布尔型置为true，继续算法
            if clusterAssment[i, 0] != minIndex: clusterChanged = True
            #更新当前变化结果的聚类结果和平方误差
            clusterAssment[i, :] = minIndex, minDist ** 2
        print centroids
        for cent in range(k):  # recalculate centroids
            #将数据集所有属于当前质心的样本通过条件筛选出来
            ptsInClust = dataSet[nonzero(clusterAssment[:, 0].A == cent)[0]]  # get all the point in this cluster
            #计算均值，作为质心向量
            centroids[cent, :] = mean(ptsInClust, axis=0)  # assign centroid to mean
    return centroids, clusterAssment


