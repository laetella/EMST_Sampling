#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2018-04-26 17:48:00
# updateDate: 2018-05-10 17:48:00
# described: to test the method and data

import sys
sys.path.append('../utils')
from headers import *

if __name__ == '__main__':  
    fileName = "../data/chaining.dat"   # 8
    point_set = loadData(fileName, float, " ")
    plt_point(point_set,fileName)