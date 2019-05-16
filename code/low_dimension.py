#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2018-04-26 17:48:00
# updateDate: 2018-05-10 17:48:00
# described: 不同方法的对比
from __future__ import division

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
import random
import numpy as np
from sklearn.metrics import confusion_matrix
# 用于计算某一个类的一组tpr和fpr的值
# 需要传入一个参数：当前计算的类的正确编号以及数量，即，l,M
def get_tpr_fpr(lables, clusters, point_set):
    TPR = []; FPR = []; # TPR=m1/N;FPR=(n1-m1)/(N-M)
    roc_p_num = 5; # 设定一条ROC曲线上的点数
    sam_num = 20; # s设定每次用来计算tpr的样本点数， 即n1
    N = len(point_set)
    # m1是可改变的，用一个循环来多次计算m1的值
    counter = 0
    while counter < roc_p_num :
        temp_p = random.sample(point_set, sam_num)
        y_true = []; y_pred = []
        for p in temp_p:
            y_true.append(lables[point_set.index(p)])
            y_pred.append(clusters[point_set.index(p)])
        cm = confusion_matrix(y_true, y_pred)
        tpr = cm[0,1] / (cm[0,1] + cm[0,0])
        fpr = cm[1,1] / (cm[1,1] + cm[1,0])
        TPR.append(tpr)
        FPR.append(fpr)
        counter += 1
    print (TPR, FPR)
    return TPR, FPR

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
	print (fileName, ": size: ", len(point_set), ", Attributes: ", len(point_set[0]))  

	# our first_sampling method
	start = time()
	result_mst = first_sampling(point_set)
	print ("our first sampling method using time: ", time() - start)

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
	labels = [int(i) for i in labels]
	print (labels)
	print (clusters)
	tpr, fpr = get_tpr_fpr(labels, clusters, point_set)

	# fpr,tpr,thresholds = roc_curve(labels, array(clusters) )
	plt.plot(fpr,tpr,linewidth=2,label="ROC")
	plt.xlabel("false presitive rate")
	plt.ylabel("true presitive rate")
	plt.show()