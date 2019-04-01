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
from mst_cls import kruscal, mst_clustering, analysis_cluster
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
	p = r'../data/two dimension'
    for root,dirs,files in walk(p): #（使用 walk ,这个方法返回的是一个三元tupple(dirpath(string), dirnames(list), filenames(list)), 其中第一个为起始路径， 第二个为起始路径下的文件夹, 第三个是起始路径下的文件.）
        for name in files:
            point_set = []
            for line in open(path.join(root,name), 'r'): 
                point = [float(data) for data in line.split(',')]
                point_set.append(point)
            # our first_sampling method
	# start = time()
	# result_mst = first_sampling(point_set)
	# print "our first sampling method using time: ", time() - start

	# 2018 Fast AMST Jothi
	# start = time()
	# result_mst = pnng(point_set)
	# print "2018 Fast AMST Jothi using time: ", time() - start

	# 2015 Fast MST Zhong
	start = time()
	result_mst = fmst(point_set)
	print "2015 Fast MST Zhong using time: ", time() - start

	# traditional MST-based clustering
	# start = time()
	# result_mst = kruscal(point_set)
	# # model = MSTClustering(cutoff=0.15)
	# # clusters = model.fit_predict(point_set)
	# print "kruscal MST using time: ", round(time() - start, 2)

	# plot MST and clusters on two dimension
	# plot_mst(result_mst, point_set, fileName,2)

	clusters = mst_clustering(result_mst, point_set, 3)
	# plt_clusters(point_set, clusters, "our_circle")
	
	# atuo generate datasets using sklearn package
	# point_set = make_circles(n_samples=1000, factor=.5, noise=.05)[0].tolist()
	# point_set = make_moons(n_samples=1000, noise=.05)[0].tolist()
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
	# fileName = '../data/low dimension/iris.arff'        # 3
	# fileName = '../data/low dimension/hayes-roth.arff'  # 3
	# fileName = '../data/low dimension/thyroid-newthyroid.arff'  # 3
	fileName = '../data/low dimension/soybean-small.arff'   # 4
	# # fileName = '../data/low dimension/waveform-v1.arff'
	# fileName = '../data/low dimension/waveform-v2.arff'
	# fileName = "../data/low dimension/pendigits.arff"     # 10 
	dataset,meta = loadarff(open(fileName,'r'))
	point_set = dataset[meta.names()[:-1]].tolist() 
	labels = dataset[meta.names()[-1]] 
	
	# load_boston, load_iris, load_diabetes, load_digits, load_linnerud, load_breast_cancer,load_wine
	# bc = load_wine()
	# point_set = bc.data
	# labels = bc.target
	print "soybean-small", ": size: ", len(point_set), ", Attributes: ", len(point_set[0])  

	# our first_sampling method
	# start = time()
	# result_mst = first_sampling(point_set)
	# print "our first sampling method using time: ", time() - start

	# 2018 Fast AMST Jothi
	# start = time()
	# result_mst = pnng(point_set)
	# print "2018 Fast AMST Jothi using time: ", time() - start

	# 2015 Fast MST Zhong
	start = time()
	result_mst = fmst(point_set)
	print "2015 Fast MST Zhong using time: ", time() - start

	# traditional MST-based clustering
	# start = time()
	# result_mst = kruscal(point_set)
	# # model = MSTClustering(cutoff=0.15)
	# # clusters = model.fit_predict(point_set)
	# print "kruscal MST using time: ", round(time() - start, 2)

	# plot MST and clusters on two dimension
	# plot_mst(result_mst, point_set, fileName,2)

	clusters = mst_clustering(result_mst, point_set, 3)
	# plt_clusters(point_set, clusters, "our_circle")
	factors = analysis_cluster(labels, clusters)
	print factors