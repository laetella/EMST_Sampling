#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2018-04-26 17:48:00
# updateDate: 2018-05-10 17:48:00
# described: to test the method and data

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
	sample_mst, edge_arr, dist_arr = prim_mst(sample_point, 0)
	temp_mst = index_change(sample_mst, sample_point, point_set)
	result_mst = sorted(temp_mst, key = lambda x:x[2])
	# plot_mst(result_mst, point_set, fileName, 1)

	# step2:  construct graph with remained point
	remained_graph, parent = comRemMST(point_set, remained_index, result_index, result_dist)
	print "remained_graph size : ", len(remained_graph) 
	# plot_mst(remained_graph,point_set,fileName,2)
	
	# step3:  把S1中的点插入S2
	S1InsertS2(result_mst, parent, remained_graph, result_index, result_dist)
	# 删除长边以及把不相连的component连起来
	plot_mst(remained_graph,point_set,fileName,3)
	# print parent
	# step4: 连接component
	# 按照论文中的方法替换边
	# 判断并查集中一共有多少个component  连接多少条边 这样太复杂了
	# 就不用第四步了 插入采样点的MST就行了 短边不构成回路直接加
	# 长边 起点终点 分别按照最近邻的方法加 （不构成回路）如果构成回路 依次找其他三个近邻 
	
	# clusters = mst_clustering(result_mst, point_set, 2)
	# plt_10clusters(point_set, clusters, fileName)
