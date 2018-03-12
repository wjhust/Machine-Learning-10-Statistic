#coding:utf-8
#必须给出utf-8的注释，否则在输出汉字的时候找不到阿斯克码的数值；


#加载数据集
def loadDataSet():
    return [[2,3,11],[2,11],[4,6,7,10],[3,8],[2,8,10],[1,2,3,4,8,10],[1,10],[1,6,9],[5,7],[1,9,5]]

def createC1(dataSet):
    C1 = []   #C1为大小为1的项的集合
    for transaction in dataSet:  #遍历数据集中的每一条交易
        for item in transaction: #遍历每一条交易中的每个商品
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    #map函数表示遍历C1中的每一个元素执行forzenset，frozenset表示“冰冻”的集合，即不可改变
    return map(frozenset,C1)


#Ck表示数据集，D表示候选集合的列表，minSupport表示最小支持度
#该函数用于从C1生成L1，L1表示满足最低支持度的元素集合
def scanD(D,Ck,minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            #issubset：表示如果集合can中的每一元素都在tid中则返回true
            if can.issubset(tid):
                #统计各个集合scan出现的次数，存入ssCnt字典中，字典的key是集合，value是统计出现的次数
                if not can in ssCnt:
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        #计算每个项集的支持度，如果满足条件则把该项集加入到retList列表中
        support = ssCnt[key]/numItems
        if support >= minSupport:
            retList.insert(0, key)
        #构建支持的项集的字典
        supportData[key] = support
    return retList,supportData

#----------------------------以上为准备函数，下边是apriori算法-----------------------
#Create Ck,CaprioriGen ()的输人参数为频繁项集列表Lk与项集元素个数k，输出为Ck
def aprioriGen(Lk,k):
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1,lenLk):
            #前k-2项相同时合并两个集合
            L1 = list(Lk[i])[:k-2]
            L2 = list(Lk[j])[:k-2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])

    return retList

def apriori(dataSet, minSupport=0.2):
    C1 = createC1(dataSet)  #创建C1
    #D: [set([1, 3, 4]), set([2, 3, 5]), set([1, 2, 3, 5]), set([2, 5])]
    D = map(set,dataSet)
    L1,supportData = scanD(D, C1, minSupport)
    L = [L1]
    #若两个项集的长度为k - 1,则必须前k-2项相同才可连接，即求并集，所以[:k-2]的实际作用为取列表的前k-1个元素
    k = 2
    while(len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2], k)
        Lk,supK = scanD(D,Ck, minSupport)
        supportData.update(supK)
        L.append(Lk)
        k +=1
    return L,supportData

#下边是main函数，主要是求出频繁项集；

if __name__=="__main__":
    dataSet = loadDataSet()
    L,suppData = apriori(dataSet)
    i = 0
    for one in L:
        print "项数为 %s 的频繁项集：" % (i + 1), one,"\n"
        i +=1


#------------------------------------关联规则函数------------------------------


#主函数是geberateRules，其他两个函数是辅助函数，调用他们；
# rulesfromconseq--生成候选规则集合  calcconf--规则评估；

#def generateRules(L, supportData, minConf=0.7):
#参数L和supportData可以由apriori函数输出
    #    bigRuleList = []
        #    for i in range(1, len(L)):
        #for freqSet in L[i]:
        #    H1 = [frozenset([item]) for item in freqSet]
        #    if (i > 1):
        #        # 三个及以上元素的集合
        #        rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
        #    else:
                # 两个元素的集合
    #        calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    #return bigRuleList

def generateRules3(L, supportData, minConf=0.2):
    bigRuleList = []
    for i in range(1, len(L)):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            rulesFromConseq2(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList

#辅助函数1：计算可信度，过滤初大于阈值的规则；
def calcConf(freqSet, H, supportData, brl, minConf=0.7):
    ''' 对候选规则集进行评估 '''
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet] / supportData[freqSet - conseq]
        if conf >= minConf:
            print freqSet - conseq, '-->', conseq, 'conf:', conf
            brl.append((freqSet - conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH


#辅助函数2：根据当前候选规则生成下一层候选规则；
#def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
#freqSet为频繁项集，H为元素列表
#supportData储存支持度，brl保存生成的关联规则
#    ''' 生成候选规则集 '''
#    m = len(H[0])
 #   if (len(freqSet) > (m + 1)):
  #      Hmpl = aprioriGen(H, m + 1)
   #     Hmpl = calcConf(freqSet, Hmpl, supportData, brl, minConf)
    #    if (len(Hmpl) > 1):
     #       rulesFromConseq(freqSet, Hmpl, supportData, brl, minConf)

def rulesFromConseq2(freqSet, H, supportData, brl, minConf=0.2):
    m = len(H[0])
    if (len(freqSet) > m): # 判断长度改为 > m，这时即可以求H的可信度
        Hmpl = calcConf(freqSet, H, supportData, brl, minConf)
        if (len(Hmpl) > 1): # 判断求完可信度后是否还有可信度大于阈值的项用来生成下一层H
            Hmpl = aprioriGen(Hmpl, m + 1)
            rulesFromConseq2(freqSet, Hmpl, supportData, brl, minConf) # 递归计算，不变




if __name__=="__main__":
    dataSet = loadDataSet()
    L,suppData = apriori(dataSet)
    i = 0
    for one in L:
        print "项数为 %s 的频繁项集：" % (i + 1), one,"\n"
        i +=1

    print "minConf=0.2时："
    rules = generateRules3(L,suppData, minConf=0.2)

    print "\nminConf=0.2时："
    rules = generateRules3(L,suppData, minConf=0.2)


#运行时，对于小的数据集，把最开始load_dataSet改了即可，本例题是对应大数据挖掘中的习题；若是大样本数据集，则需其他初始化