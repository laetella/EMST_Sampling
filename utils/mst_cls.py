#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2019-03-27 17:33:57
# updateDate: 2019-03-27 17:33:57
# described: 基于MST的聚类方法 

from networkx import utils
from math import sqrt

def dist(point1,point2):
    sum_dis = 0.0
    dimension = len(point1)
    for index in range(dimension)  :
        sum_dis += (point2[index] - point1[index])**2
    return sqrt(sum_dis)

def kruscal(point_set):
    # compute graph and sort first
    n = len(point_set)
    graph = []
    for i in range(n-1) :
        for j in range(i+1, n) :
            d = dist(point_set[i], point_set[j])
            graph.append([i, j, d])
    sorted_edge = sorted(graph, key = lambda x:x[2])
    # initialize the union find set
    uf = utils.UnionFind()
    mst = []
    for e in sorted_edge:
        if uf[e[0]] != uf[e[1]] :
            uf.union(e[0], e[1])
            mst.append(e)
    return mst

def mst_clustering(mst, point_set, cls_num):
    sorted_edge = sorted(mst, key = lambda x:x[2],  reverse=True)   #由小到大排序
    # print sorted_edge
    for i in range(cls_num-1):
        mst.remove(sorted_edge[i])
    subtrees = utils.UnionFind()
    for edge in mst:
        subtrees.union(edge[0], edge[1])
    labels = [0] * len(point_set)
    for i in range(len(point_set)) :
        labels[i] = subtrees[i]
    label_set = list(set(labels))
    for i in range(len(point_set)) :
        for j in range(len(label_set)) :
            if labels[i] == label_set[j] :
                labels[i] = j
                break
    return labels

