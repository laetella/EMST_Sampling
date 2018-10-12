# -*- coding: utf-8 -*-

from headers import *

def prim_mst(point_set, s):
    result_set = []
    nodes_finished = []
    nodes_unfinished = []
    nodes_finished.append(s)
    dist_arr = [0] * len(point_set)
    edge_arr = [0]* len(point_set)
    temp_dist1 = 1.0e14
    position = -1
    for index in range(len(point_set)):
        if index == s :
            dist_arr[index] = 0
            edge_arr[index] = -1
            continue
        t = dist(point_set[s], point_set[index])
        dist_arr[index] = t
        edge_arr[index] = s
        if t < temp_dist1 :
            temp_dist1 = t
            position = index
    nodes_finished.append(position)
    # print position, temp_dist1
    result_set.append([s,position,temp_dist1])
    for index in range(len(point_set)):
        if index != s and index != position :
            nodes_unfinished.append(index)
    # print "add an edge--", s,"---,", index, "----,", 1
    q_index = 0
    # print dist_arr
    while len(nodes_unfinished) > 0 :
        temp_dist2 = 1.0e14
        temp_posit = len(nodes_finished) - 1
        for point_i in nodes_unfinished :
            new_node = nodes_finished[temp_posit]
            d = dist(point_set[new_node], point_set[point_i])
            if d < dist_arr[point_i] : #and r != 0 :
                dist_arr[point_i] = d
                edge_arr[point_i] = new_node
            if dist_arr[point_i] < temp_dist2  :
                temp_dist2 = dist_arr[point_i]
                position = nodes_unfinished.index(point_i)
                q_index = point_i
        nodes_finished.append(q_index)
        nodes_unfinished.remove(nodes_unfinished[position])
        result_set.append([edge_arr[q_index], q_index,dist_arr[q_index]])
        # print "add an edge--", edge_arr[q_index],"---,", q_index, "----,", dist_arr[q_index]
    return result_set, edge_arr, dist_arr

def find(x, parent):
    # return parent[x]
    if parent[x] == x :
        return x
    else:
        parent[x] = find(parent[x],parent)
        return parent[x]

def union(x, y, parent):
    root_x = find(x, parent)
    root_y = find(y, parent)
    if root_x == root_y :
        return
    else:
        if root_x > root_y :
            parent[x] = root_y
        else:
            parent[y] = root_x

