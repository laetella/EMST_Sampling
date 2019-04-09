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

# from sklearn.metrics import roc_curve, auc
# from sklearn.model_selection import train_test_split
# ##划分数据集
# X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.1, random_state=0)
# y_score = clf.fit(X_train, y_train).predict_proba(X_test) #随机森林
# fpr, tpr, thresholds = roc_curve(y_test, y_score[:,1]);
# roc_auc = auc(fpr, tpr) 

# ##确定最佳阈值

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

# def _joint_log_likelihood(self, X):
#     check_is_fitted(self, "classes_")

#     X = check_array(X)
#     joint_log_likelihood = []
#     for i in range(np.size(self.classes_)):
#         jointi = np.log(self.class_prior_[i])
#         n_ij = - 0.5 * np.sum(np.log(2. * np.pi * self.sigma_[i, :]))
#         n_ij -= 0.5 * np.sum(((X - self.theta_[i, :]) ** 2) /
#                              (self.sigma_[i, :]), 1)
#         joint_log_likelihood.append(jointi + n_ij)

#     joint_log_likelihood = np.array(joint_log_likelihood).T
#     return joint_log_likelihood


if __name__=='__main__':
    a = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
    print array(a)[:,0]
#     # fileName = "../data/chaining.dat"   # 8
#     fileName = "../data/test/chaining.dat"   # 8
#     point_set = loadData(fileName, float, ",")
#     # plt.plot('xlabel', 'ylabel', data=array(point_set)[0])
#     # print "point_set size: ", len(point_set)
#     result_mst = first_sampling(point_set)
#     # plt.plot(result_mst[0])
#     plot_mst(result_mst,point_set,fileName,0)
#     # p = r'../data/test'

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