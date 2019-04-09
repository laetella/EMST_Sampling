#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2018-04-26 17:48:00
# updateDate: 2018-05-10 17:48:00
# described: 不同方法的对比

import sys
sys.path.append('../utils')
from sampling import first_sampling
from mst_cls import kruscal, mst_clustering
from time import time
from plt import *
from pnng_2018 import pnng
from fmst_2015 import fmst

def loadData(fileName,data_type, str): 
    point_set = [] 
    for line in open(fileName, 'r'): 
        point = [data_type(data) for data in line.split(str)]
        # point_set.append([point[1],point[2]])
        point_set.append(point)
    return point_set

if __name__ == '__main__': 
	# two dimension
	fileName = "../data/test/chaining.dat"   # 8
	point_set = loadData(fileName, float, ",")
	# our first_sampling method
	start = time()
	SMST = first_sampling(point_set)
	print "our first sampling method using time: ", round(time() - start, 2)

	# # 2018 Fast AMST Jothi
	# start = time()
	# PNNG = pnng(point_set)
	# print "2018 Fast AMST Jothi using time: ", round(time() - start, 2)

	# # 2015 Fast MST Zhong
	# start = time()
	# FMST = fmst(point_set)
	# print "2015 Fast MST Zhong using time: ", round(time() - start, 2)

	# # traditional kruscal MST
	# start = time()
	# KMST = kruscal(point_set)
	# print "kruscal MST using time: ", round(time() - start, 2)

	plot_mst(SMST, point_set, fileName)
	clusters = mst_clustering(SMST, point_set, 2)
	plt_clusters(point_set, clusters, fileName)