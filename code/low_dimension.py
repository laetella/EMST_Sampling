#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2018-04-26 17:48:00
# updateDate: 2018-05-10 17:48:00
# described: 不同方法的对比
from __future__ import division

import sys, os
sys.path.append('../utils')
from sampling import first_sampling
from mst_cls import kruscal, mst_clustering, analysis_cluster
from scipy.io.arff import loadarff
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from sklearn.datasets import *
from time import time
from _mst_clustering import MSTClustering
# from plt import *
from pnng_2018 import pnng
from fmst_2015 import fmst
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt  
from numpy import array
from plt import *
import random
import numpy as np
from sklearn.metrics import balanced_accuracy_score # ,accuracy_score# ,  adjusted_mutual_info_score# calinski_harabasz_score #, 
# from sklearn.metrics import confusion_matrix, precision_recall_fscore_support, 

def mst2clustering(result_set, cls_num, cls_size):
    # 需要把计算得到的MST转换成聚类可用的稀疏矩阵的形式
    sorted_edge = sorted(result_set, key = lambda x:x[2],  reverse=True)   #由小到大排序
    n = len(result_set) + 1
    for i in range(cls_num):
        result_set.remove(sorted_edge[i])
    mst = csr_matrix((n, n)).toarray()
    for edge in result_set:
        mst[edge[0]][edge[1]] = edge[2]
    n_components, labels = connected_components(mst, directed=False)
    # remove clusters with fewer than min_cluster_size
    counts = np.bincount(labels)
    to_remove = np.where(counts < cls_size)[0]
    if len(to_remove) > 0:
        for i in to_remove:
            labels[labels == i] = -1
        _, labels = np.unique(labels, return_inverse=True)
        labels -= 1  # keep -1 labels the same
    labels[labels == -1] = max(labels) + 1
    return labels

if __name__ == '__main__': 
	factor_file = open('../result/smst.csv','a')
	path = "../data/low dimension"
	for root,dirs,files in os.walk(path): 
		point_set = []
		for name in files:
			file_name, file_type = os.path.splitext(name)
			fileName = os.path.join(root,name)
			print (file_name)
			dataset,meta = loadarff(open(fileName,'r'))
			point_set = dataset[meta.names()[:-1]].tolist()
			labels = dataset[meta.names()[-1]].tolist()
			for i,l in enumerate(labels) :
				labels[i] = int(l)
			# print (fileName, ": size: ", len(point_set), ", Attributes: ", len(point_set[0]))  

			start = time()
			result_mst = first_sampling(point_set)
			end = round(time() - start, 2)
			factor_file.write(str(file_name) + "," + str(end) + ",bac,")
			print ("our first sampling method using time: ", end)

			clusters = mst2clustering(result_mst, 5, 20).tolist()
			factors = balanced_accuracy_score(labels, clusters)
			print (file_name, factors)
			factor_file.write(str(factors)+ "\n")
	factor_file.close()

	# load_boston, load_iris, load_diabetes, load_digits, load_linnerud, load_breast_cancer,load_wine
	# bc = load_wine()
	# point_set = bc.data
	# labels = bc.target

	# our first_sampling method
	# start = time()
	# result_mst = first_sampling(point_set)
	# print ("our first sampling method using time: ", time() - start)

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
	# result_mst = kruscal(point_set)
	# # model = MSTClustering(cutoff=0.15)
	# # clusters = model.fit_predict(point_set)
	# print "kruscal MST using time: ", round(time() - start, 2)

	# model = MSTClustering(cutoff=0.2, min_cluster_size=10)
	# clusters = model.fit(point_set)
	# clusters = model.fit_predict(point_set)
	# clusters = mst_clustering(result_mst, point_set, 4)
	# # plt_clusters(point_set, clusters, "our_circle")
	# # factors = analysis_cluster(labels, clusters)
	# # print factors
	# # calinski_harabasz_score
	# # compute y scores
	# # ROC evaluation
	# labels = [int(i) for i in labels]
	# factors = adjusted_mutual_info_score(labels, clusters)
	# # factors = balanced_accuracy_score(labels, clusters)
	# # factors = precision_recall_fscore_support(labels, clusters)
	# print factors
	# print (labels)
	# print (clusters)
