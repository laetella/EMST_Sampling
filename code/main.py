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
from mst_cls import mst_clustering
from plt import *
from pnng_2018 import pnng

def loadData(fileName,data_type, str): 
    point_set = [] 
    for line in open(fileName, 'r'): 
        point = [data_type(data) for data in line.split(str)]
        point_set.append(point)
    return point_set

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
	# fileName = "../data/data_t4_sorted.csv"   # 6
	# fileName = "../data/data_t5_sorted.csv"   # 6
	# fileName = "../data/data_t7_sorted.csv"   # 9
	# fileName = "../data/data_t8_sorted.csv"   # 8
	# point_set = loadData(fileName, float, ",") 
	# fileName = "../data/data_l.dat"           # 7
	fileName = "../data/chaining.dat"   # 8
	# fileName = "../data/data_caiming.dat"   # 8
	point_set = loadData(fileName, float, " ")

	# our first_sampling method
	# result_mst = first_sampling(point_set)

	# 2018 Fast AMST Jothi
	result_mst = pnng(point_set)

	# plot MST and compute clusters
	# plot_mst(result_mst, point_set, fileName,2)
	# clusters = mst_clustering(result_mst, point_set, 2)

	# traditional MST-based clustering
	# model = MSTClustering(cutoff=0.15)
	# clusters = model.fit_predict(point_set)

	# plt_10clusters(point_set, clusters, fileName)
