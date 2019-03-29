#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2019-03-29 18:08:36
# updateDate: 2019-03-29 18:08:36
# described: some plot functions

import matplotlib.pyplot as plt  

def plt_point(point_set,fileName):
    for point in point_set:
        plt.scatter(point[0],point[1],s=20)
        plt.annotate(point_set.index(point), xy = (point[0], point[1]),xycoords = 'data',fontsize=0.2)
    plt.savefig('../result/%s_point.png'%(fileName.split('/')[2].split('.')[0]), dpi=1000)

def plot_mst(result_set,point_set,fileName,s):
    for point in point_set:
        plt.scatter(point[0],point[1],color= 'r', s=15) # plt.figure(0)
        # plt.annotate(point_set.index(point), xy = (point[0], point[1]),xycoords = 'data',fontsize=8)
    for edge in result_set:
        # plt.scatter(point_set[edge[0]][0],point_set[edge[0]][1],color= 'r', marker = 'o')
        plt.plot([point_set[edge[0]][0],point_set[edge[1]][0]] ,[point_set[edge[0]][1],point_set[edge[1]][1]], color= 'b', linewidth = 1.3)
        # plt.annotate(edge[0], xy = (point_set[edge[0]][0], point_set[edge[0]][1]),xycoords = 'data',fontsize=4)
    plt.title("")
    plt.xticks([])
    plt.yticks([])
    plt.savefig('../result/%s_mst_%d.png'%(fileName.split('/')[2].split('.')[0], s), dpi=400)
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

def plt_10clusters(point_set, clusters, fileName):
    x = []; y = []; cl = []
    for i, point in enumerate(point_set) :
        # plt.annotate(point_set.index(point), xy = (point[0], point[1]),xycoords = 'data',fontsize=4)
        x.append(point[0])
        y.append(point[1])
        # cl.append(0.6)
        if clusters[i] == 1 :
            cl.append('black')
        elif clusters[i] == 2:
            cl.append('r')
        elif clusters[i] == 3:
            cl.append('g')
        elif clusters[i] == 4:
            cl.append('b')
        elif clusters[i] == 5:
            cl.append('y')
        elif clusters[i] == 6:
            cl.append('coral')
        elif clusters[i] == 7:
            cl.append('purple')
        elif clusters[i] == 8:
            cl.append('m')
        elif clusters[i] == 9:
            cl.append('lawngreen')
        else:
            cl.append('deepskyblue')
    plt.title("")
    plt.xticks([])
    plt.yticks([])
    plt.scatter(x, y, c = cl)
    plt.savefig('../result/%s_clusters.png'%(fileName.split('/')[2].split('.')[0]), dpi=500)

def plt_test(point_set, clusters, fileName):
    for point in point_set:
        plt.scatter(point[0],point[1],s=20)
        plt.annotate(point_set.index(point), xy = (point[0], point[1]),xycoords = 'data',fontsize=0.2)
    plt.savefig('../result/%s_point.png'%(fileName.split('/')[2].split('.')[0]), dpi=1000)
