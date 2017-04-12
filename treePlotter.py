# -*- coding:utf-8 -*-
# __author__ = 'CaoRui'
import matplotlib.pyplot as plt

#定制文本框和箭头格式
decisionNode = dict(boxstyle = 'sawtooth', fc = '0.8')
leafNode = dict(boxstyle = 'round4', fc = '0.8')
arrow_args = dict(arrowstyle = '<-')

#回执带箭头的注解
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    #由全局变量createPlot.axl定义一个绘图区
    createPlot.axl.annotate(nodeTxt, xy = parentPt, xycoords = 'axes fraction',\
                            xytext = centerPt, textcoords = 'axes fraction',\
                            va = 'center', ha='center', bbox = nodeType,\
                            arrowprops = arrow_args)

def createPlot():
    fig = plt.figure(1, facecolor = 'white')
    fig.clf()
    createPlot.axl = plt.subplot(111, frameon = False)
    plotNode(U'decision', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode(U'leaf', (0.8, 0.1), (0.1, 0.8), leafNode)
    plt.show()

#获取叶节点数目
def getNumLeafs(mytree):
    numLeafs=0
    firstStr = mytree.keys()[0]
    secondDict = mytree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs

#获取树的层数
def getNumDepth(mytree):
    numDepth = 0
    firstStr = mytree.keys()[0]
    secondDict = mytree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getNumDepth(secondDict[key])
        else:
            thisDepth = 1
    if thisDepth > numDepth:
        numDepth = thisDepth
    return numDepth



if __name__ == '__main__':
    createPlot()

