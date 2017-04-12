# -*- coding:utf-8 -*-
# __author__ = 'CaoRui'

from math import log
import operator

#计算给定数据集的香浓熵
def calcShannonEnt(dataSet):
    numEntries=len(dataSet)
    labelCounts={} #创建dict字典数据类型
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob*log(prob,2)
    return  shannonEnt

#划分数据集
def splitDataSet(dataSet,axis,value):
    retDataSet=[]
    for featVel in dataSet:
        if featVel[axis] == value:
            reduceFeatVec = featVel[:axis]
            reduceFeatVec.extend(featVel[axis+1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet

#选择最好的数据集划分方式
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain=0.0
    bestFeature=-1
    for i in xrange(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEnttopy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            prob = len(subDataSet)/float(len(dataSet))
            newEnttopy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEnttopy
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

#返回出现次数最多的分类名称
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount:
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassSort = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassSort[0][0]

#创建数的函数代码
def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    #classList.count() 统计某个元素在列表中出现的次数
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValus = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValus)
    for value in uniqueVals:
        subLabels=labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)
    return myTree