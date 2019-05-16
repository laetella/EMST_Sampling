#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2019-03-27 17:33:57
# updateDate: 2019-03-27 17:33:57
# described: 基于MST的聚类方法 

from __future__ import division
from networkx import utils
from math import sqrt

def dist(point1,point2):
    sum_dis = 0.0
    dimension = len(point1)
    for index in range(dimension)  :
        sum_dis += (point2[index] - point1[index])**2
    return sqrt(sum_dis)

# TODO 更新parent array
def prim(point_set):
    result_set = []
    low_cost = [0]* len(point_set)
    start_index = 0
    end_index = 0
    flags = [False] *len(point_set)
    for index in range(len(point_set)):
        low_cost[index] =  dist(point_set[start_index], point_set[index]) 
    while len(result_set) < len(point_set):
        min_dist = 65535
        for index1 in range(len(point_set)):
            if low_cost[index1]!=0.0 and low_cost[index1] < min_dist and not flags[index1]:
                min_dist = low_cost[index1]
                end_index = index1
        flags[end_index] = True
        for index,distance in enumerate(low_cost) :
            if distance == min_dist:
                start_index = index
        flags[start_index] = True
        edge = [start_index, end_index, min_dist] 
        result_set.append(edge)
    return result_set

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
    for i in range(cls_num-1):
        mst.remove(sorted_edge[i])
    subtrees = utils.UnionFind()
    for edge in mst:
        subtrees.union(edge[0], edge[1])
    labels = [0] * len(point_set)
    for i in range(len(point_set)) :
        labels[i] = subtrees[i]
    label_set = list(set(labels))
    for l in label_set:
        if labels.count(l) < 10 :
            print (l)
            for i,ll in enumerate(labels):
                if ll == l :
                    labels[i] = 1
    # print "label_set: ", label_set
    # 因为初始化类标号是0， 离群点类标号为1， 所以其他点从2开始标号
    for i in range(len(point_set)) :
        for j in range(1, len(label_set)+1) :
            if labels[i] == label_set[j-1] :
                labels[i] = j
                break
    for i,l in enumerate(labels) :
        if l > 10 :
            labels[i] = l % 10
    return labels

def analysis_cluster(right_labels, clusters):
    a = 0; b = 0; c = 0; d = 0;
    n = len(right_labels) 
    for i in range(n) :
        for j in range(n) :
            if j != i :
                if right_labels[i] == right_labels[j] and clusters[i] == clusters[j] :
                    a += 1
                elif right_labels[i] != right_labels[j] and clusters[i] == clusters[j]:
                    b += 1
                elif right_labels[i] == right_labels[j] and clusters[i] != clusters[j] :
                    c += 1
                elif right_labels[i] != right_labels[j] and clusters[i] != clusters[j] :
                    d += 1
    a = a / 2; b = b / 2; c = c / 2; d = d/2;
    m = n * (n-1) / 2
    r = ((a+c)*(a+b)/m);
    ARI=(a-r)/(((a+c)+(a+b))/2-r)
    Rand = (a+d)/m
    Jaccard = a/ (a+b+c)
    FolkesAndMallow = sqrt(a/(a+b))*(a/(a+c))
    return [round(Rand, 4), round(ARI, 4), round(Jaccard, 4), round(FolkesAndMallow, 4)]    
