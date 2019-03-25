#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2018-10-09 09:31:32
# updateDate: 2018-10-09 09:31:32
# described: sampling data from original data

from headers import *

def cover_knn(point_set, k_threshold):
    my_cover = CoverTree(point_set, euclidean, leafsize=2)
    result_dist,result_index = my_cover.query(point_set, k_threshold)        
    return result_dist,result_index

# 换一种采样方法
# 1. 用python 包里的采样方法进行采样
# 2. 先将0取出来 然后找0的最近邻， 

# 采样： 取第一个点  将它的最近邻加进去 依次加近邻点
# 用论文中提到的方法，找每个点的四个近邻，保留最近的一个，删除其他三个
# def toSample(point_set, result_index):
# 	sample_data = [] 	# 采样结果的数据，用索引表示，初始为所有点，然后一个一个删除
# 	remained = []
# 	for i in range(len(point_set)):
# 		sample_data.append(i)
# 	# 用从点集中删除点的方法比采样简单，容易实现
# 	# print "sample_data ", sample_data
# 	for idx, knns in enumerate(result_index) :
# 		if idx in sample_data :
# 			for i in range(2, len(knns)):
# 				if knns[i] in sample_data :
# 					sample_data.remove(knns[i])
# 					remained.append(knns[i])
# 	return sample_data, remained

def toSample(point_set, result_index):
	sample_data = [result_index[0][0]] 	
	for idx, knns in enumerate(result_index) :
		if knns[1] not in sample_data :
			sample_data.append(knns[1])
	return sample_data


def indexToCoor(index, point_set):
	coor_set = []
	for i in index:
		coor_set.append(point_set[i])
	return coor_set

def index_change(sample_mst, sample_point, point_set):
	mst = []
	for edge in sample_mst:
		start = point_set.index(sample_point[edge[0]])
		end = point_set.index(sample_point[edge[1]])
		mst.append([start, end, edge[2]])
	return mst

def selectEdge(point, mst, parent, result_index, result_dist):
	nn = result_index[point]
	for neighbor in range(1,len(nn)) :
		edge = [point,result_index[point][neighbor], result_dist[point][neighbor]]
		if find(edge[0], parent) != find(edge[1], parent) :
			# print "add an edge: ", edge
			mst.append(edge)
			union(edge[0], edge[1], parent)
			break

# 传入参数为 采样剩余的点的索引， 返回值为这些点和最近邻连成的图
# 顶点用索引表示
def comRemMST(point_set, remained, result_index, result_dist):
	mst = [];  parent = [0]*len(point_set)
	for i in range(len(point_set)) :
		parent[i] = i
	# 用加最近邻的方法 应该49条边 但只有42条边  是EMST，后面需要合并component
	# 调用函数  找不一定最近邻 可以49条边 但是AMST  不是EMST
	for point in remained:
		edge = [point,result_index[point][1], result_dist[point][1]]
		if find(edge[0], parent) != find(edge[1], parent) :
			# print "add an edge: ", edge
			mst.append(edge)
			union(edge[0], edge[1], parent)
		# selectEdge(point, mst, parent, result_index, result_dist)
	return mst, parent

# 传入参数为采样的点的索引
# 将采样的点加入到 已构成的graph中 
def S1InsertS2(sample_mst, parent, graph, result_index, result_dist):
	# total_weight = 0
	# for edge in graph:
	# 	total_weight += edge[2]
	# thre = total_weight / len(graph)
	thre = max(e[2] for e in graph)
	# print "threshold: ", thre
	for index,  edge in enumerate(sample_mst) :
		if edge[2] < thre :
			temp_edge = [edge[0], result_index[edge[0]][1], result_dist[edge[0]][1]]
			if find(edge[0], parent) != find(result_index[edge[0]][1], parent) :
			  	graph.append(temp_edge)
			  	union(edge[0], result_index[edge[0]][1], parent) 
			# selectEdge(edge[0], graph, parent, result_index, result_dist)
		else:
			temp_edge = [edge[0], result_index[edge[0]][1], result_dist[edge[0]][1]]
			if find(edge[0], parent) != find(result_index[edge[0]][1], parent) :
			  	graph.append(temp_edge)
			  	union(edge[0], result_index[edge[0]][1], parent) 
			else:
				temp_edge = [edge[1], result_index[edge[1]][1], result_dist[edge[1]][1]]
				if find(edge[1], parent) != find(result_index[edge[1]][1], parent) :
				  	graph.append(temp_edge)
				  	union(edge[1], result_index[edge[1]][1], parent)  
				else:
					selectEdge(temp_edge[1] , graph, parent, result_index, result_dist)
	# 用连接component的方法		
	print "graph: ", len(graph)
	# 两次循环结束后  应该有 不连通的component，想办法连起来就好
	
	