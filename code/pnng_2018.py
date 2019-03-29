#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2019-03-27 18:22:52
# updateDate: 2019-03-27 18:22:52
# described: 对比2017年的文章 PNNG 计算近似MST的算法

from math import sqrt
from sklearn.cluster import KMeans
from networkx import utils

def loadData(fileName,data_type, str): 
    point_set = [] 
    for line in open(fileName, 'r'): 
        point = [data_type(data) for data in line.split(str)]
        point_set.append(point)
    return point_set

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

def pnng(point_set):
    init_part_num = int(round(sqrt(len(point_set))))   
    kmeans = KMeans(n_clusters=init_part_num, random_state=0).fit(point_set)
    clusters = kmeans.labels_
    centers = kmeans.cluster_centers_
    # 用plot scatter的方法 画一下初次划分的情况
    center_mst = kruscal(centers)
    init_part = [0] * init_part_num
    for i in range(init_part_num) :
        init_part[i] = []
    for index, p in enumerate(point_set) :
        init_part[clusters[index]].append(p)
    edge_set = []
    # intra-partition all pair-edges
    for each_cluster in init_part:
        # print each_cluster, "======"
        for i in range(len(each_cluster)-1) :
            for j in range(i+1, len(each_cluster)) :
                temp_dist = dist(each_cluster[i], each_cluster[j])
                start = point_set.index(each_cluster[i])
                end = point_set.index(each_cluster[j])
                # print start, "======", end, "====="
                edge_set.append([start, end, temp_dist])
    # inter-partition 
    max_we = max(edge[2] for edge in center_mst)
    for i in range(0, init_part_num-1) :
        for j in range(i, init_part_num) :
            if dist(centers[i], centers[j]) <= max_we :   # 说明是近邻的簇
                for p1 in init_part[i] :
                    for p2 in init_part[j]:
                        dii = dist(p1,centers[i])
                        dij = dist(p1,centers[j])
                        dji = dist(p2,centers[i])
                        djj = dist(p2,centers[i])
                        if dij < 2 * dii or dji < 2 * djj :
                            temp_dist = dist(p1,p2)
                            start = point_set.index(p1)
                            end = point_set.index(p2)
                            edge_set.append([start, end, temp_dist])
    # combine process
    uf = utils.UnionFind()
    result_mst = []
    edge_set.sort(key = lambda x:x[2])
    for e in edge_set:
        if uf[e[0]] != uf[e[1]] :
            result_mst.append(e)
            uf.union(e[0], e[1])
    return  result_mst

if __name__=='__main__':
    fileName = "../data/data_f.dat"   # 8
    point_set = loadData(fileName, float, ",")
    result_mst = pnng(point_set)
