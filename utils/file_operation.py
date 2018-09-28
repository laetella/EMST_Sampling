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
        # point_set.append([point[1],point[2]])
        point_set.append(point)
    return point_set
