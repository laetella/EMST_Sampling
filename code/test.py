#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2018-10-10 08:51:44
# updateDate: 2018-10-10 08:51:44
# described: test union find  data structure

if __name__ == "__main__" :
    edges = [[0,1],[5,2],[2,3],[3,4],[4,5],[6,7],[7,8],[8,9]]
    parent = [0]*10
    for x in range(10) :
    	parent[i] = i
    for edge in edges:
        union(edge[0],edge[1],parent)
    print parent
    point = edge[0]; toAdd1 = []
			# toAdd1 = [point,result_index[point][1], result_dist[point][1]]
			nn1 = result_index[point]
			for neighbor in range(1,len(nn1)) :
				edge = [point,result_index[point][neighbor], result_dist[point][neighbor]]
				if find(edge[0], parent) != find(edge[1], parent) :
					toAdd1 = edge
					break
			point = edge[1]; toAdd2 = []
			# toAdd2 = [point,result_index[point][1], result_dist[point][1]]
			nn2 = result_index[point]
			for neighbor in range(1,len(nn2)) :
				edge = [point,result_index[point][neighbor], result_dist[point][neighbor]]
				if find(edge[0], parent) != find(edge[1], parent) :
					toAdd2 = edge
					break
			if len(toAdd1) == 0 and len(toAdd2) == 0 :
				print "current edge : ", edge
				continue
			if len(toAdd2) == 0 or toAdd1[2] < toAdd2[2] :
				print "add an edge====toAdd1: ", toAdd1
				graph.append(toAdd1)
				union(toAdd1[0], toAdd1[1], parent)
			else:
				print "add an edge====toAdd2: ", toAdd2
				graph.append(toAdd2)
				union(toAdd2[0], toAdd2[1], parent)
	# 	selectEdge(edge[0] , graph, parent, result_index, result_dist)
		# 	selectEdge(edge[1] , graph, parent, result_index, result_dist)