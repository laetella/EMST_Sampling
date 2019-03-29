#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2018-10-10 08:51:44
# updateDate: 2018-10-10 08:51:44
# described: 

import sys
sys.path.append('../utils')
from sampling import first_sampling
from mst_cls import mst_clustering
from plt import *

if __name__=='__main__':
    q  = [[1,2,0.3], [2,3,0.9], [2,9,1.6]]
    a = max(e[2] for e in q)
    print a
	# # fileName = "../data/chaining.dat"   # 8
	# fileName = "../data/data_f.dat"   # 8
	# point_set = loadData(fileName, float, ",")
	# print "point_set size: ", len(point_set)
	# result_mst = result_mst = pnng(point_set)

	# plot_mst(result_mst, point_set, fileName,1)

 