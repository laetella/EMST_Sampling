#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2018-10-09 09:31:32
# updateDate: 2018-10-09 09:31:32
# described: sampling data from original data
'''
两种采样方法：
1.	任选一个点作为初始点，然后选取它的最近邻，再依次加入近邻点
2.	求所有点的5个近邻， 取完一个点和它的近邻之后，其他点都不要
'''
from covertree import CoverTree, distance_matrix
from scipy.spatial.distance import euclidean, cityblock, chebyshev
from mst_cls import kruscal
from sklearn.neighbors import KDTree

def cover_knn(point_set, k_threshold):
    my_cover = KDTree(point_set, leaf_size=3)              
    # my_cover = CoverTree(point_set, euclidean, leafsize=1)
    result_dist,result_index = my_cover.query(point_set, k_threshold)        
    return result_dist,result_index

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

def first_sampling(point_set):
	result_dist,result_index = cover_knn(point_set, 6)
	# plt_point(point_set,fileName)
	
	# 进行采样 可以换为其他的采样方法
	# sample_index, remained_index = toSample(point_set, result_index)
	sample_index = toSample(point_set, result_index)
	# print "sample_point size : ", len(sample_index) 
	# plt_sampler(sample_index, point_set, fileName)

	# 对采样的数据创建EMST  调用mlpack的构造mst的方法效率更高
	# step1 construct MST with sample point 
	sample_point = indexToCoor(sample_index, point_set)
	sample_mst = kruscal(sample_point)
	result_mst = index_change(sample_mst, sample_point, point_set)
	# print "sample_mst size: ", len(result_mst)
	# plot_mst(result_mst, point_set, fileName, 1)

	# 把剩下的点加入EMST
	for idx, point in enumerate(point_set) :
		if idx not in sample_index :
			result_mst.append([idx, result_index[idx][1], result_dist[idx][1]])
	# total_weight = 0
	# for edge in result_mst:
	# 	total_weight += edge[2]
	# print "total_weight: ", total_weight
	return result_mst	
 
