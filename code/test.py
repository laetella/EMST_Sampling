#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2018-10-10 08:51:44
# updateDate: 2018-10-10 08:51:44
# described: test union find  data structure

import sys
sys.path.append('../utils')
from headers import *

if __name__=='__main__':
	fileName = "../data/chaining.dat"   # 8
	# fileName = "../data/data_caiming.dat"   # 8
	point_set = loadData(fileName, float, " ")
	sample_mst, edge_arr, dist_arr = prim_mst(point_set, 0)
	total_weight = 0
	for d in dist_arr:
		total_weight += d
	print "total_weight: ", total_weight
	plot_mst(sample_mst, point_set, fileName,10)
