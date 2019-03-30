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

if __name__=='__main__':
    point_set = datasets.make_circles(n_samples=1000, factor=.5, noise=.05)[0].tolist()
    result_mst = first_sampling(point_set)
    clusters = mst_clustering(result_mst, point_set, 2)
    plt_clusters(point_set, clusters, "../data/our.data")
    # plt_10clusters(point_set, clusters, "../data/make.dat")
    # print point_set
    # noisy_moons = datasets.make_moons(n_samples=1000, noise=.05)
    # blobs = datasets.make_blobs(n_samples=1000, random_state=8)
    # no_structure = np.random.rand(1000, 2), None

	# # fileName = "../data/chaining.dat"   # 8
	# fileName = "../data/data_f.dat"   # 8
	# point_set = loadData(fileName, float, ",")
	# print "point_set size: ", len(point_set)
	# result_mst = result_mst = pnng(point_set)

	# plot_mst(result_mst, point_set, fileName,1)

 