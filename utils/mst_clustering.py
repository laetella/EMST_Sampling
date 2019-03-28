#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2019-03-27 17:33:57
# updateDate: 2019-03-27 17:33:57
# described: 基于MST的聚类方法 

from headers import *

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

