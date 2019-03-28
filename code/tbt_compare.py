#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2019-03-27 18:23:54
# updateDate: 2019-03-27 18:23:54
# described: 对比传统的MST聚类方法


import sys
sys.path.append('../utils')
from headers import *

if __name__ == "__main__" :
	fileName = "../data/data_f.dat"   # 2 174
	# fileName = "../data/data_i.dat"   # 2   84
	# fileName = "../data/data_ieee.dat"   # 9   441
	# fileName = "../data/data_h.dat"   # 2    176
	# fileName = "../data/data_syn1_2.dat"  # 4
	# fileName = "../data/data_syn2_1.dat"   # 3
	# fileName = "../data/data_caiming.dat" # 2   96
	# fileName = "../data/data_caiming_2.dat" # 2   63
	# fileName = "../data/density_d.dat"      # 5   38
	# fileName = "../data/gestalt.dat"      # 2    63
	# fileName = "../data/data_t4_sorted.csv"   # 6
	# fileName = "../data/data_t5_sorted.csv"   # 6
	# fileName = "../data/data_t7_sorted.csv"   # 9
	# fileName = "../data/data_t8_sorted.csv"   # 8
	point_set = loadData(fileName, float, ",") 
	# fileName = "../data/chaining.dat"
	# point_set = loadData(fileName,float, ' ')
	s = 0
	result_set, parent_arr, ratio_arr = prim_mst(point_set, 0)
	# plot_mst(result_set, point_set, fileName, s)
	model = MSTClustering(cutoff=0.15)
	clusters = model.fit_predict(point_set)
	# # print clusters
	# # plt_two_clusters(point_set, clusters, fileName,1)
	plt_10clusters(point_set, clusters, fileName)