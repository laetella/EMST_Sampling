#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2018-09-28 14:46:24
# updateDate: 2018-09-28 14:46:24
# described: include some file operations

def loadData(fileName,data_type, str): 
    point_set = [] 
    for line in open(fileName, 'r'): 
        point = [data_type(data) for data in line.split(str)]
        point_set.append(point)
    return point_set

    # fileName = "../data/data_t4_sorted.csv"   # 6
    # fileName = "../data/data_t5_sorted.csv"   # 6
    # fileName = "../data/data_t7_sorted.csv"   # 9
    # fileName = "../data/data_t8_sorted.csv"   # 8