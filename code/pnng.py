#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2019-03-27 18:22:52
# updateDate: 2019-03-27 18:22:52
# described: 对比2017年的文章 PNNG 计算近似MST的算法

import sys
sys.path.append('../utils')
from headers import *

def pnng(point_set):
    init_part_num = int(round(sqrt(len(point_set))))   
    kmeans = KMeans(n_clusters=init_part_num, random_state=0).fit(point_set)
    clusters = kmeans.labels_
    centers = kmeans.cluster_centers_
    result_set, edge_arr, dist_arr = prim_mst(centers)
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
    for i in range(0, init_part_num-1) :
        for j in range(i, init_part_num) :
            if dist(centers[i], centers[j]) <= max(dist_arr) :   # 说明是近邻的簇
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
    G = nx.Graph()  
    for every_edge in edge_set:
        G.add_weighted_edges_from([(every_edge[0],every_edge[1],every_edge[2])])
    temp_mst = nx.minimum_spanning_tree(G)
    a = nx.get_edge_attributes(temp_mst, 'weight')
    mst_result = []
    for e in temp_mst.edges:
        mst_result.append([e[0], e[1], a[e]])
        # print e[0], "===", e[1] , "====", a[e]
    return  mst_result # temp_mst # 
