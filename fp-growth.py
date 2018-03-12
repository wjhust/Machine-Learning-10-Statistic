#coding:utf-8
class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
#name:节点名字；count：出现次数；nodeLink指向下一个相似节点的指针，默认为NONE
#parent：指向父节点；children：指向子节点，以元素名称为键，指向子节点的指针为值；
#inc:增加节点的出现次数； disp:输出节点和子节点的fp树结构
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None
        self.parent = parentNode
        self.children = {}

    def inc(self, numOccur):
        self.count += numOccur

    def disp(self, ind=1):
        print ' ' * ind, self.name, ' ', self.count
        for child in self.children.values():
            child.disp(ind + 1)

#--------------------代码测试--------------------
#rootNode = treeNode('pyramid', 9, None)
#rootNode.children['eye'] = treeNode('eye', 13, None)
#rootNode.children['phoenix'] = treeNode('phoenix', 3, None)
#rootNode.disp()
#------------------------------------------------





#--------------------------------------生成fpTree-----------------------
#总函数：createTree
def createTree(dataSet, minSup=1):
    ''' 创建FP树 '''
    # 第一次遍历数据集，创建头指针表
    headerTable = {}
    for trans in dataSet:
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
    # 移除不满足最小支持度的元素项
    for k in headerTable.keys():
        if headerTable[k] < minSup:
            del(headerTable[k])
    # 空元素集，返回空
    freqItemSet = set(headerTable.keys())
    if len(freqItemSet) == 0:
        return None, None
    # 增加一个数据项，用于存放指向相似元素项指针
    for k in headerTable:
        headerTable[k] = [headerTable[k], None]
    retTree = treeNode('Null Set', 1, None) # 根节点
    # 第二次遍历数据集，创建FP树
    for tranSet, count in dataSet.items():
        localD = {} # 对一个项集tranSet，记录其中每个元素项的全局频率，用于排序
        for item in tranSet:
            if item in freqItemSet:
                localD[item] = headerTable[item][0] # 注意这个[0]，因为之前加过一个数据项
        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)] # 排序
            updateTree(orderedItems, retTree, headerTable, count) # 更新FP树
    return retTree, headerTable
#解释：dataSet是集合的字典形式，集合为键，值为集合出现的次数


#辅助函数updateTree
def updateTree(items, inTree, headerTable, count):
    if items[0] in inTree.children:
        # 有该元素项时计数值+1
        inTree.children[items[0]].inc(count)
    else:
        # 没有这个元素项时创建一个新节点
        inTree.children[items[0]] = treeNode(items[0], count, inTree)
        # 更新头指针表或前一个相似元素项节点的指针指向新节点
        if headerTable[items[0]][1] == None:
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])

    if len(items) > 1:
        # 对剩下的元素项迭代调用updateTree函数
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)


#辅助函数；updateHeader

def updateHeader(nodeToTest, targetNode):
        while (nodeToTest.nodeLink != None):
            nodeToTest = nodeToTest.nodeLink
        nodeToTest.nodeLink = targetNode



#生成数据集：
def loadSimpDat():
    simpDat = [['r', 'z', 'h', 'j', 'p'],
               ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
               ['z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return simpDat
#该数据即为样例的格式

def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1
    return retDict



#main函数：测试代码
#simpDat = loadSimpDat()
#initSet = createInitSet(simpDat)
#myFPtree, myHeaderTab = createTree(initSet, 3)
#myFPtree.disp()

#---------------------------------------------------------------------------------



#----------------------------------------提取频繁项集------------------------

#主函数findPrefixPath

def findPrefixPath(basePat,treeNode):
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1:
            condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.nodeLink
    return condPats
#为给定元素项生成条件模式基，通过访问所有包含给定元素项的节点完成，basePat为输入的频繁项，treeNode为前FP树的一个节点


#辅助函数ascendTree

def ascendTree(leafNode, prefixPath):
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)
#这个函数直接修改prefixPath的值，将当前节点leafNode添加到prefixPath的末尾，
#然后递归添加其父节点。最终结果，prefixPath就是一条从treeNode（包括treeNode）到根节点（不包括根节点）的路径。
# 在主函数findPrefixPath()中再取prefixPath[1:]，即为treeNode的前缀路径。



#测试：创建fp条件树
#initset=createInitSet(loadSimpDat())
#myFPtree,myHeaderTab=createTree(initset,3)
#a=myFPtree.disp()
#b=findPrefixPath('x',myHeaderTab['x'][1])
#print b
#---------------------fp树已经创建完毕--------------------

#---------------------递归查找频繁项集合-------------------
def mineTree(inTree, headerTable, minSup, preFix, freqItemList):
    bigL = [v[0] for v in sorted(headerTable.items(), key=lambda p: p[1])]
    for basePat in bigL:
        newFreqSet = preFix.copy()
        newFreqSet.add(basePat)
        freqItemList.append(newFreqSet)
        condPattBases = findPrefixPath(basePat, headerTable[basePat][1])
        myCondTree, myHead = createTree(condPattBases, minSup)

        if myHead != None:
            # 用于测试
            print 'conditional tree for:', newFreqSet
            myCondTree.disp()
            mineTree(myCondTree, myHead, minSup, newFreqSet, freqItemList)

#：inTree和headerTable是由createTree()函数生成的数据集的FP树
#minSup表示最小支持度
#preFix请传入一个空集合（set([])），将在函数中用于保存当前前缀
#freqItemList请传入一个空列表（[]），将用来储存生成的频繁项集


#：测试数据
#freqItems=[]
#mineTree(myFPtree,myHeaderTab,3,set([]),freqItems)
#freqItems


#-------------------------以上各部分函数已经完毕，封装即可----------------------------
def fpGrowth(dataSet, minSup=3):
    initSet = createInitSet(dataSet)
    myFPtree, myHeaderTab = createTree(initSet, minSup)
    freqItems = []
    mineTree(myFPtree, myHeaderTab, minSup, set([]), freqItems)
    return freqItems

#main函数
dataSet=loadSimpDat()
freqItems=fpGrowth(dataSet)
freqItems