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
from sklearn import cluster, datasets, mixture
from numpy import array
import matplotlib.pyplot as plt  
from itertools import islice, cycle
from os import walk, path, remove

if __name__=='__main__':
	# # fileName = "../data/chaining.dat"   # 8
	# fileName = "../data/data_f.dat"   # 8
	# point_set = loadData(fileName, float, ",")
	# print "point_set size: ", len(point_set)
	# result_mst = result_mst = pnng(point_set)

	# plot_mst(result_mst, point_set, fileName,1)

 