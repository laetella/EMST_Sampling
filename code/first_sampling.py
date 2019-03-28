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

def toSample(point_set, result_index):
	sample_data = [result_index[0][0]] 	
	for idx, knns in enumerate(result_index) :
		if knns[1] not in sample_data :
			sample_data.append(knns[1])
	return sample_data

if __name__ == '__main__': 
	# fileName = "../data/data_f.dat"   # 2 174
	# fileName = "../data/data_i.dat"   # 2   84
	# fileName = "../data/data_ieee.dat"   # 9   441
	# fileName = "../data/data_h.dat"   # 2    176
	# fileName = "../data/data_syn1_2.dat"  # 4
	# fileName = "../data/data_syn2_1.dat"   # 3
	# fileName = "../data/data_caiming.dat" # 2   96
	# fileName = "../data/data_caiming_1.dat" # 2   63
	# fileName = "../data/density_d.dat"      # 5   38
	fileName = "../data/gestalt.dat"      # 2    63
	# fileName = "../data/data_t4_sorted.csv"   # 6
	# fileName = "../data/data_t5_sorted.csv"   # 6
	# fileName = "../data/data_t7_sorted.csv"   # 9
	# fileName = "../data/data_t8_sorted.csv"   # 8
	point_set = loadData(fileName, float, ",") 
	# fileName = "../data/data_l.dat"           # 7
	# fileName = "../data/chaining.dat"   # 8
	# # fileName = "../data/data_caiming.dat"   # 8
	# point_set = loadData(fileName, float, " ")
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
	# sample_index, remained_index = toSample(point_set, result_index)
	sample_index = toSample(point_set, result_index)
	print "sample_point size : ", len(sample_index)  
	# plt_sampler(sample_index, point_set, fileName)

	# 对采样的数据创建EMST  调用mlpack的构造mst的方法效率更高
	# step1 construct MST with sample point 
	sample_point = indexToCoor(sample_index, point_set)
	sample_mst, edge_arr, dist_arr = prim_mst(sample_point, 0)
	temp_mst = index_change(sample_mst, sample_point, point_set)
	result_mst = sorted(temp_mst, key = lambda x:x[2])
	# plot_mst(result_mst, point_set, fileName, 1)

	# 把剩下的点加入EMST
	for idx, point in enumerate(point_set) :
		if idx not in sample_index :
			result_mst.append([idx, result_index[idx][1], result_dist[idx][1]])
	total_weight = 0
	for edge in result_mst:
		total_weight += edge[2]
	print "total_weight: ", total_weight
	# plot_mst(result_mst, point_set, fileName,1)

	clusters = mst_clustering(result_mst, point_set, 2)
	plt_10clusters(point_set, clusters, fileName)