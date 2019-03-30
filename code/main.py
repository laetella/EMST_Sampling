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
from mst_cls import mst_clustering, analysis_cluster
from scipy.io.arff import loadarff
from sklearn.datasets import *
from time import time
from plt import *
from pnng_2018 import pnng
from fmst_2015 import fmst

def loadData(fileName,data_type, str): 
    point_set = [] 
    for line in open(fileName, 'r'): 
        point = [data_type(data) for data in line.split(str)]
        point_set.append(point)
    return point_set

if __name__ == '__main__': 
	# two dimension
	# fileName = "../data/two dimension/data_f.dat"   # 2 174
	# fileName = "../data/two dimension/data_i.dat"   # 2   84
	# fileName = "../data/two dimension/data_ieee.dat"   # 9   441
	# fileName = "../data/two dimension/data_h.dat"   # 2    176
	# fileName = "../data/two dimension/data_syn1_2.dat"  # 4
	# fileName = "../data/two dimension/data_syn2_1.dat"   # 3
	# fileName = "../data/two dimension/data_caiming.dat" # 2   96
	# fileName = "../data/two dimension/data_caiming_1.dat" # 2   63
	# fileName = "../data/two dimension/density_d.dat"      # 5   38
	# fileName = "../data/two dimension/data_t4_sorted.csv"   # 6
	# fileName = "../data/two dimension/data_t5_sorted.csv"   # 6
	# fileName = "../data/two dimension/data_t7_sorted.csv"   # 9
	# fileName = "../data/two dimension/data_t8_sorted.csv"   # 8
	# point_set = loadData(fileName, float, ",") 
	# fileName = "../data/two dimension/data_l.dat"           # 7
	# fileName = "../data/two dimension/chaining.dat"   # 8
	# point_set = loadData(fileName, float, " ")

	# atuo generate datasets using sklearn package
	# point_set = make_circles(n_samples=1000, factor=.5, noise=.05)[0].tolist()
	point_set = make_moons(n_samples=1000, noise=.05)[0].tolist()
	# point_set = make_blobs(n_samples=1000, random_state=8)[0].tolist()

	# multi low dimension
	# 2 clusters
	# fileName = '../data/low dimension/arcene.arff'
	# fileName = '../data/low dimension/appendicitis.arff'
	# fileName = '../data/low dimension/banknote-authentication.arff'
	# fileName = '../data/low dimension/breast-cancer-wisconsin.arff'
	# fileName = '../data/low dimension/bupa.arff'
	# fileName = "../data/low dimension/fertility-diagnosis.arff"
	# fileName = '../data/low dimension/habermans-survival.arff'
	# fileName = '../data/low dimension/pima-indians-diabetes.arff'
	# fileName = '../data/low dimension/wdbc.arff'
	# fileName = '../data/low dimension/ionosphere.arff'
	#
	#     # more than 2 clusters: 
	# fileName = '../data/iris.arff'        # 3
	# fileName = '../data/hayes-roth.arff'  # 3
	# fileName = '../data/thyroid-newthyroid.arff'  # 3
	# fileName = '../data/soybean-small.arff'   # 4
	# # fileName = '../data/waveform-v1.arff'
	# fileName = '../data/waveform-v2.arff'
	# fileName = '../data/wine.arff'          # 3
	# fileName = "../data/pendigits.arff"     # 10 
	# dataset,meta = loadarff(open(fileName,'r'))
	# point_set = dataset[meta.names()[:-1]].tolist() 
	# labels = dataset[meta.names()[-1]] 
	# print fileName, ": size: ", len(dataset), ", Attributes: ", len(meta.names())   

	# our first_sampling method
	start = time()
	result_mst = first_sampling(point_set)
	print "our first sampling method using time: ", time() - start

	# 2018 Fast AMST Jothi
	# start = time()
	# result_mst = pnng(point_set)
	# print "2018 Fast AMST Jothi using time: ", time() - start

	# 2015 Fast MST Zhong
	# start = time()
	# result_mst = fmst(point_set)
	# print "2015 Fast MST Zhong using time: ", time() - start

	# traditional MST-based clustering
	# start = time()
	# model = MSTClustering(cutoff=0.15)
	# clusters = model.fit_predict(point_set)
	# print "traditional MST-based clustering using time: ", time() - start

	# plot MST and clusters on two dimension
	# plot_mst(result_mst, point_set, fileName,2)

	clusters = mst_clustering(result_mst, point_set, 2)
	plt_clusters(point_set, clusters, "our_circle")
	# factors = analysis_cluster(labels, clusters)
	# print factors