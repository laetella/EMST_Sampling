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
# from plt import *
from pnng_2018 import pnng
from fmst_2015 import fmst
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt  
from numpy import array

if __name__ == '__main__': 
	# multi low dimension
	# 2 clusters
	# fileName = '../data/low dimension/arcene.arff'
	fileName = '../data/low dimension/appendicitis.arff'
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
	# fileName = '../data/low dimension/soybean-small.arff'   # 4
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
	# result_mst = kruscal(point_set)
	# # model = MSTClustering(cutoff=0.15)
	# # clusters = model.fit_predict(point_set)
	# print "kruscal MST using time: ", round(time() - start, 2)

	clusters = mst_clustering(result_mst, point_set, 2)
	# plt_clusters(point_set, clusters, "our_circle")
	# factors = analysis_cluster(labels, clusters)
	# print factors
	
	# compute y scores
	# ROC evaluation

	fpr,tpr,thresholds = roc_curve(labels, array(clusters) )
	plt.plot(fpr,tpr,linewidth=2,label="ROC")
	plt.xlabel("false presitive rate")
	plt.ylabel("true presitive rate")
	plt.show()