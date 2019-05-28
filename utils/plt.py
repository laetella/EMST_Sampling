#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2019-03-29 18:08:36
# updateDate: 2019-03-29 18:08:36
# described: some plot functions

import matplotlib.pyplot as plt  
from numpy import array
from itertools import islice, cycle

def plt_point(point_set,fileName):
    for point in point_set:
        plt.scatter(point[0],point[1],s=20)
        plt.annotate(point_set.index(point), xy = (point[0], point[1]),xycoords = 'data',fontsize=0.2)
    plt.savefig('../result/%s_point.png'%(fileName.split('/')[2].split('.')[0]), dpi=1000)

def plot_mst(result_set,point_set,fileName):
    for point in point_set:
        plt.scatter(point[0],point[1],color= 'r', s=15) # plt.figure(0)
        # plt.annotate(point_set.index(point), xy = (point[0], point[1]),xycoords = 'data',fontsize=8)
    for edge in result_set:
        plt.plot([point_set[edge[0]][0],point_set[edge[1]][0]] ,[point_set[edge[0]][1],point_set[edge[1]][1]], color= 'b', linewidth = 1.3)
        # plt.annotate(edge[0], xy = (point_set[edge[0]][0], point_set[edge[0]][1]),xycoords = 'data',fontsize=4)
    plt.title("")
    plt.xticks([])
    plt.yticks([])
    plt.savefig('../result/%s_mst.png'%(fileName.split('/')[2].split('.')[0]), dpi=400)
    # plt.close(0)

def plt_sampler(sample_index, point_set, fileName):
    for idx, point in enumerate(point_set) :
        if idx in sample_index :
            plt.scatter(point[0], point[1], s=20, color='r')
            # plt.annotate(idx, xy = (point[0], point[1]),xycoords = 'data',fontsize=5)
        else:
            plt.scatter(point[0],point[1],s=10, color='b')
            # plt.annotate(idx, xy = (point[0], point[1]),xycoords = 'data',fontsize=5)
    plt.title("")
    plt.xticks([])
    plt.yticks([])
    plt.savefig('../result/%s_point.png'%(fileName.split('/')[2].split('.')[0]), dpi=1000)

def plt_clusters(point_set, clusters, fileName):
    colors = array(list(islice(cycle(['#377eb8', '#ff7f00', '#4daf4a',
                                             '#f781bf', '#a65628', '#984ea3',
                                             '#999999', '#e41a1c', '#dede00']),
                                      int(max(clusters) + 1))))
    plt.scatter(array(point_set)[:, 0],array(point_set)[:, 1], s=10, color=colors[clusters])
    plt.title("")
    plt.xticks([])
    plt.yticks([])
    plt.savefig('../result/%s_clusters.png'%(fileName.split('/')[2].split('.')[0]), dpi=500)

def plt_test(point_set, clusters, fileName):
    for point in point_set:
        plt.scatter(point[0],point[1],s=20)
        plt.annotate(point_set.index(point), xy = (point[0], point[1]),xycoords = 'data',fontsize=0.2)
    plt.savefig('../result/%s_point.png'%(fileName.split('/')[2].split('.')[0]), dpi=1000)

# 预测某点的概率的方法： 这点预测成了3 实际类标号为1， 该方法对这个点的预测概率=预测成3的点数 、、预测成1 的点数
# tn  [0, 0]
# fp  [0, 1]
# fn  [1, 0]
# tp  [1, 1]
# tpr = fp / p
# fpr = fp / (n - p)
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

