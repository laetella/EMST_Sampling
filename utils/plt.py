# -*- coding: utf-8 -*-

from headers import *

def plt_point(point_set,fileName):
    for point in point_set:
        plt.scatter(point[0],point[1],s=20)
        plt.annotate(point_set.index(point), xy = (point[0], point[1]),xycoords = 'data',fontsize=0.2)
    plt.savefig('../result/%s_point.png'%(fileName.split('/')[2].split('.')[0]), dpi=1000)

def plot_mst(result_set,point_set,fileName,s):
    for point in point_set:
        plt.scatter(point[0],point[1],color= 'r', s=15) # plt.figure(0)
        plt.annotate(point_set.index(point), xy = (point[0], point[1]),xycoords = 'data',fontsize=8)
    for edge in result_set:
        # plt.scatter(point_set[edge[0]][0],point_set[edge[0]][1],color= 'r', marker = 'o')
        plt.plot([point_set[edge[0]][0],point_set[edge[1]][0]] ,[point_set[edge[0]][1],point_set[edge[1]][1]], color= 'b', linewidth = 1.3)
        # plt.annotate(edge[0], xy = (point_set[edge[0]][0], point_set[edge[0]][1]),xycoords = 'data',fontsize=4)
    plt.title("")
    plt.xticks([])
    plt.yticks([])
    plt.savefig('../result/%s_mst_%d.png'%(fileName.split('/')[2].split('.')[0], s), dpi=400)
    # plt.close(0)
