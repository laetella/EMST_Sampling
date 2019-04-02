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
from numpy import array, ndarray
import matplotlib.pyplot as plt  
from itertools import islice, cycle, product
from os import walk, path, remove
from time import time
def loadData(fileName,data_type, str): 
    point_set = [] 
    for line in open(fileName, 'r'): 
        point = [data_type(data) for data in line.split(str)]
        # point_set.append([point[1],point[2]])
        point_set.append(point)
    return point_set
if __name__=='__main__':
    # a = array([[1,2,0.23], [2,3,0.46], [2,5,1.25]]) 
    # print [x for x in a[:, 0]] 
        # print x
    # print a[:, 0]
    # print a[:, 1]
    # fileName = "../data/chaining.dat"   # 8
    fileName = "../data/test/chaining.dat"   # 8
    point_set = loadData(fileName, float, ",")
    # plt.plot('xlabel', 'ylabel', data=array(point_set)[0])
    # print "point_set size: ", len(point_set)
    result_mst = first_sampling(point_set)
    # plt.plot(result_mst[0])
    plot_mst(result_mst,point_set,fileName,0)
    # p = r'../data/test'

	# plot_mst(result_mst, point_set, fileName,1)
    # plt.figure(figsize=[40,8.9])
    # plt.subplots_adjust(left=0.02, right=0.978, bottom=0.15, wspace=0.05)
    # plot_num = 1
    # for root,dirs,files in walk(p): 
    #     for name in files:
    #         point_set = []
    #         for line in open(path.join(root,name), 'r'): 
    #             point = [float(data) for data in line.split(',')]
    #             point_set.append(point)
    #         start = time()
    #         SMST = first_sampling(point_set)
    #         print "our first sampling method using time: ", time() - start
    #         clusters = mst_clustering(SMST, point_set, 2)
    #         colors = array(list(islice(cycle(['#377eb8', '#ff7f00', '#4daf4a',
    #                                          '#f781bf', '#a65628', '#984ea3',
    #                                          '#999999', '#e41a1c', '#dede00']),
    #                                   int(max(clusters) + 1))))
    #         plt.subplot(1, 4, plot_num)
    #         plt.title("")
    #         plt.xticks([])
    #         plt.yticks([])
    #         plt.scatter(array(point_set)[:, 0],array(point_set)[:, 1], s=20, color=colors[clusters])
    #         plot_num += 1
    # plt.savefig('../result/clusters.png', dpi=500)