#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2018-10-10 08:51:44
# updateDate: 2018-10-10 08:51:44
# described: fast mst of Zhong 2015 (two rounds MST)
# 该算法对于稀疏的数据集结果不好 在第二阶段的构造过程中 有的中点位于稀疏部分 导致有的簇为空
# 无法计算neighbor subset的connect edge 

from math import sqrt
from networkx import utils
from sklearn.cluster import KMeans
from numpy import mean, array

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

def kruscal_graph(graph):
	sorted_edge = sorted(graph, key = lambda x:x[2])
	# initialize the union find set
	uf = utils.UnionFind()
	mst = []
	for e in sorted_edge:
	    if uf[e[0]] != uf[e[1]] :
	        uf.union(e[0], e[1])
	        mst.append(e)
	return mst

def index_change(sample_mst, sample_point, point_set):
	mst = []
	for edge in sample_mst:
		start = point_set.index(sample_point[edge[0]])
		end = point_set.index(sample_point[edge[1]])
		mst.append([start, end, edge[2]])
	return mst

def dce(cluster1, cluster2, center1, center2):
	# to find the neiboring edge
	temp_dist = 1.0e4
	start = []; end = []
	for p in cluster1:
		d = dist(p, center2)
		if d < temp_dist :
			temp_dist = d
			start = p
	temp_dist = 1.0e4
	for q in cluster2:
		d = dist(q, center1)
		if d < temp_dist :
			temp_dist = d
			end = q
	neighbor_edge = [start, end, dist(start,end)]
	return neighbor_edge

def sam(midpoints, point_set):
	# 对于点集中的每一个点 计算到所有中点的距离 然后取最小的，分配到相应的簇中，下面的过程一样
	init_part = [0] * len(midpoints)
	for i in range(len(midpoints)) :
	    init_part[i] = []
	for p in point_set:
		temp_dist = 1.0e14
		for idx, mp in enumerate(midpoints) :
			d = dist(p, mp)
			if d < temp_dist :
				temp_dist = d
				cls_label = idx
		# 每次循环结束后得到最小的距离和对应的簇标号
		init_part[cls_label].append(p)
	edge_set = []
	# compute mst of every subset 
	for each_cluster in init_part:
		temp_mst = kruscal(each_cluster)
		sub_mst = index_change(temp_mst, each_cluster, point_set)
		edge_set.extend(sub_mst)
	print edge_set
	ca(point_set, midpoints, init_part, edge_set)
	return edge_set

def dac(point_set, centers, clusters):
	# Divide and Conquer Using K-means (DAC)
	init_part = [0] * len(centers)
	for i in range(len(centers)) :
	    init_part[i] = []
	for index, p in enumerate(point_set) :
	    init_part[clusters[index]].append(p)
	edge_set = []
	# compute mst of every subset 
	for each_cluster in init_part:
		temp_mst = kruscal(each_cluster)
		sub_mst = index_change(temp_mst, each_cluster, point_set)
		edge_set.extend(sub_mst)
	return init_part, edge_set

def ca(point_set, centers, init_part, edge_set):
	# Combine Algorithm (CA)
	midpoints = []
	cen_mst = kruscal(centers)
	for edge in cen_mst:
		# Determine the neighboring subsets.
		sub_cluster1 = init_part[edge[0]]
		sub_cluster2 = init_part[edge[1]]
		# Detect the Connecting Edge (DCE)
		temp_edge = dce(sub_cluster1, sub_cluster2, centers[edge[0]], centers[edge[1]])
		start = point_set.index(temp_edge[0])
		end = point_set.index(temp_edge[1])
		edge_set.append([start, end, temp_edge[2]])
		# 同时计算边的中点
		two_point = array([centers[edge[0]], centers[edge[1]]]) 
		midpoints.append(mean(array(two_point), axis=1)) 
	return edge_set, midpoints

def fmst(point_set):
	init_part_num = int(round(sqrt(len(point_set))))   
	kmeans = KMeans(n_clusters=init_part_num, random_state=0).fit(point_set)
	clusters = kmeans.labels_
	centers = kmeans.cluster_centers_
	init_part, edge_set = dac(point_set, centers, clusters)
	mst1, midpoints = ca(point_set, centers, init_part, edge_set)
	# mst2 = sam(midpoints, point_set)
	# mst1.extend(mst2)
	result_mst = kruscal_graph(mst1)
	return result_mst

if __name__=='__main__':
	fileName = "../data/two dimension/density_d.dat"   # 8
	point_set = loadData(fileName, float, ",")
	result_mst = fmst(point_set)
