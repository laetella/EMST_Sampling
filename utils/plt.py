# -*- coding: utf-8 -*-

from headers import *

def plt_point(point_set,fileName):
    for point in point_set:
        plt.scatter(point[0],point[1],s=20)
        plt.annotate(point_set.index(point), xy = (point[0], point[1]),xycoords = 'data',fontsize=0.2)
    plt.savefig('../result/%s_point.png'%(fileName.split('/')[2].split('.')[0]), dpi=1000)
