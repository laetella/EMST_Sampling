#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2018-10-10 08:51:44
# updateDate: 2018-10-10 08:51:44
# described: 
from __future__ import division

import sys
sys.path.append('../utils')
from sampling import first_sampling
from mst_cls import mst_clustering
from _mst_clustering import MSTClustering
from plt import *
from sklearn import cluster, datasets, mixture
from numpy import array, ndarray
import matplotlib.pyplot as plt  
from itertools import islice, cycle, product
from os import walk, path, remove
from time import time
import random
import numpy as np
from sklearn.metrics import confusion_matrix
# from sklearn.metrics import roc_curve, auc
# from sklearn.model_selection import train_test_split
# ##划分数据集
# X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.1, random_state=0)
# y_score = clf.fit(X_train, y_train).predict_proba(X_test) #随机森林
# fpr, tpr, thresholds = roc_curve(y_test, y_score[:,1]);
# roc_auc = auc(fpr, tpr) 

# right_index = (tpr + (1 - fpr) - 1)
# yuzhi = max(right_index)
# index = right_index.index(max(right_index))
# tpr_val = tpr(index)
# fpr_val = fpr(index)
# ## 绘制roc曲线图
# plt.subplots(figsize=(7,5.5));
# plt.plot(fpr, tpr, color='darkorange',
#          lw=2, label='ROC curve (area = %0.2f)' % roc_auc);
# plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--');
# plt.xlim([0.0, 1.0]);
# plt.ylim([0.0, 1.05]);
# plt.xlabel('False Positive Rate');
# plt.ylabel('True Positive Rate');
# plt.title('ROC Curve');
# plt.legend(loc="lower right");
# plt.show()

# 将聚类结果的离群点划分到最近的簇


def loadData(fileName,data_type, str): 
    point_set = [] 
    for line in open(fileName, 'r'): 
        point = [data_type(data) for data in line.split(str)]
        point_set.append(point)
    return point_set

# 将类标号转换为点的坐标的形式
def l2Coor(labels, point_set):
    l = len(set(labels) )
    clusters = [[]]*l
    for i in range(l):
        clusters[i] = []
    # print clusters
    for i, point in enumerate(point_set) :
        clusters[labels[i]].append(point)
    return clusters

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
    # print TPR, FPR
    return TPR, FPR

# 预测某点的概率的方法： 这点预测成了3 实际类标号为1， 该方法对这个点的预测概率=预测成3的点数 、、预测成1 的点数
# tn  [0, 0]
# fp  [0, 1]
# fn  [1, 0]
# tp  [1, 1]
if __name__=='__main__':
    # fileName = "../data/chaining.dat"   # 8
    # fileName = "../data/test/chaining.dat"   # 8
    # point_set = loadData(fileName, float, ",")
    # plt.plot('xlabel', 'ylabel', data=array(point_set)[0])
    # print "point_set size: ", len(point_set)
    # result_mst = first_sampling(point_set)
    # plt.plot(result_mst[0])
    # plot_mst(result_mst,point_set,fileName)
    # p = r'../data/test'
    # clusters = mst_clustering(result_mst, point_set, 2)
    # print clusters
    ###################   data caiming  ################
    flieName = "../data/two dimension/data_caiming.dat"
    point_set = loadData(flieName, float, ',') 
    y_true = [1]*24
    y_true.extend([0]*72) 
    y_true[28] = 1
    y_true[37] = 1
    # smst = first_sampling(point_set)
    # y_pred = mst_clustering(smst, point_set, 2)
    # tpr, fpr = get_tpr_fpr(y_true, y_pred, point_set)
    # plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve');
    # plt.show()
    # print tpr, fpr

    # # print y_pred
    # smst_clusters = l2Coor(y_pred, point_set)
    # # 当前计算的类标号记为l，该类的正确标号的数量为M 
    # l = 0
    # M = y_true.count(0)
    # # print smst_clusters
    # n = 96; p = 0; tp = 0; fp = 0
    # for y in y_true:
    #     if y == l :
    #         p += 1
    # for i, y in enumerate(y_pred) :
    #     if y == l :
    #         tp += 1
    #         if y_true[i] == l :
    #             fp += 1
    # tpr = fp / p
    # fpr = fp / (n - p)
    # print tpr, fpr
    # tpr, fpr = get_tpr_fpr(y_true, y_pred, point_set, l, M)
    # # 需要一个循环，对每一个类分别画一个ROC曲线
    # right_clusters = l2Coor(y_true, point_set)
    # for c in right_clusters:
    #     tpr, fpr = get_tpr_fpr(clusters, point_set)
    #     plt_roc(tpr, fpr)
	
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
    # model = MSTClustering(cutoff= 3)
    model = MSTClustering(cutoff=0.3, min_cluster_size=20)
    clusters = model.fit(point_set)
    # clusters = model.predict_proba(point_set)
    # clusters = model.fit_predict(point_set)
    print (clusters.labels_)