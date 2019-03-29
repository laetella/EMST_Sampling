#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2018-04-26 17:48:00
# updateDate: 2018-05-10 17:48:00
# described: 用到第二种采样方法 实验效果不好 需要进一步改进

import sys
sys.path.append('../utils')
from headers import *

# 采样： 取第一个点  将它的最近邻加进去 依次加近邻点
# 用论文中提到的方法，找每个点的四个近邻，保留最近的一个，删除其他三个
def toSample(point_set, result_index):
	sample_data = [] 	# 采样结果的数据，用索引表示，初始为所有点，然后一个一个删除
	remained = []
	for i in range(len(point_set)):
		sample_data.append(i)
	# 用从点集中删除点的方法比采样简单，容易实现
	# print "sample_data ", sample_data
	for idx, knns in enumerate(result_index) :
		if idx in sample_data :
			for i in range(2, len(knns)):
				if knns[i] in sample_data :
					sample_data.remove(knns[i])
					remained.append(knns[i])
	return sample_data, remained

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


if __name__ == '__main__':  
	fileName = "../data/chaining.dat"   # 8
	# fileName = "../data/data_caiming.dat"   # 8
	point_set = loadData(fileName, float, " ")
	ps_size = len(point_set)
	# sample_size = sqrt(ps_size)
	print "point set size: ", ps_size
	# result_set, edge_arr, dist_arr = prim_mst(point_set, 0)
	# plot_mst(result_set,point_set,fileName,3)
	k_threshold = 5 # 选最近邻的四个点 
	result_dist,result_index = cover_knn(point_set, k_threshold)
	# print "result_index: ", result_index
	# plt_point(point_set,fileName)
	
	# 进行采样 可以换为其他的采样方法
	sample_index, remained_index = toSample(point_set, result_index)
	# print "sample_point size : ", len(sample_index)  
	# plt_sampler(sample_index, point_set, fileName)

	# 对采样的数据创建EMST  调用mlpack的构造mst的方法效率更高
	# step1 construct MST with sample point 
	sample_point = indexToCoor(sample_index, point_set)
	sample_mst = kruscal(sample_point)
	# sample_mst, edge_arr, dist_arr = prim_mst(sample_point, 0)
	result_mst = index_change(sample_mst, sample_point, point_set)
	# result_mst = sorted(temp_mst, key = lambda x:x[2])
	plot_mst(result_mst, point_set, fileName, 3)

	# step2:  construct graph with remained point
	uf = utils.UnionFind()
	for e in result_mst:
		uf.union(e[0], e[1])
	remained_point = indexToCoor(remained_index, point_set)
	for idx in remained_index:
		result_mst.append([idx, result_index[idx][1], result_dist[idx][1]])
	plot_mst(result_mst,point_set,fileName,4)
		
	# remained_mst = kruscal(remained_point)
	# # remained_graph, parent = comRemMST(point_set, remained_index, result_index, result_dist)
	# print "remained_graph size : ", len(remained_mst) 
	# temp_mst = index_change(remained_mst, remained_point, point_set)

	# result_mst.extend(temp_mst)
	# result_mst.sort(key = lambda x:x[2])
	# uf = utils.UnionFind()
	# mst = []
	# for e in result_mst:
	# 	if uf[e[0]] != uf[e[1]] :
	# 		uf.union(e[0], e[1])
	# 		mst.append(e)
	# print "result_mst size: ", len(result_mst)
	# plot_mst(mst,point_set,fileName,3)
		
	# step3:  把S1中的点插入S2
	# S1InsertS2(result_mst, parent, remained_graph, result_index, result_dist)
	# # 删除长边以及把不相连的component连起来
	# print parent
	# step4: 连接component
	# 按照论文中的方法替换边
	# 判断并查集中一共有多少个component  连接多少条边 这样太复杂了
	# 就不用第四步了 插入采样点的MST就行了 短边不构成回路直接加
	# 长边 起点终点 分别按照最近邻的方法加 （不构成回路）如果构成回路 依次找其他三个近邻 
	
	# clusters = mst_clustering(result_mst, point_set, 2)
	# plt_10clusters(point_set, clusters, fileName)
