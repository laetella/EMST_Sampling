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

if __name__ == '__main__': 
	# two dimension
	p = r'../data/two dimension'
	# 第一个为起始路径， 第二个为起始路径下的文件夹, 第三个是起始路径下的文件.
    for root,dirs,files in walk(p): 
        for name in files:
            point_set = []
            for line in open(path.join(root,name), 'r'): 
                point = [float(data) for data in line.split(',')]
                point_set.append(point)
        	# our first_sampling method
			# start = time()
			# result_mst = first_sampling(point_set)
			# print "our first sampling method using time: ", time() - start
    		# fileName = "our_" + name.split('.')[0]

			# 2018 Fast AMST Jothi
			# start = time()
			# result_mst = pnng(point_set)
			# print "2018 Fast AMST Jothi using time: ", time() - start
    		# fileName = "pnng_" + name.split('.')[0]

			# 2015 Fast MST Zhong
			# start = time()
			# result_mst = fmst(point_set)
			# print "2015 Fast MST Zhong using time: ", time() - start
    		# fileName = "fmst_" + name.split('.')[0]

			# traditional MST-based clustering
			# start = time()
			# result_mst = kruscal(point_set)
			# print "kruscal MST using time: ", round(time() - start, 2)
    		# fileName = "kruscal_" + name.split('.')[0]

			# plot MST and clusters on two dimension
			# plot_mst(result_mst, point_set, fileName,2)

			clusters = mst_clustering(result_mst, point_set, 3)
			# plt_clusters(point_set, clusters, fileName)
				
