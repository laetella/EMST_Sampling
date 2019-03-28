# EMST_Sampling
An efficient MST-based clustering algotrithm based on sampling

improving the efficiency of emst algorithm with sampling
1. 对比算法：查找AMST相关文献对比1+elpson以及边的权重和时间
2. 用多个采样方法丰富文章内容
3. our method部分 画图表示每一步执行过程

1. 用到求最近邻的方法covertree 

之前的MST算法都是先构造一个完全图 再计算MST 这样效率比较低，我们提出了一种采样 不需要构造完全图的方法
  可以写成类似于sklearn中的形式 给一个数据集，下面好几种聚类方法，画到一个图中 

 主要是时间复杂度的问题

Second Method：
2.  不能简单的连起来最近邻  因为这样连起来 孤立的component太多了
需要增加一些判断 比如：选择一个起始点 按最近邻加进去 （直接用基于KNN的MST）
第三步 
下面这段代码是啥意思？？
先找到剩下的点构成的图中最长的边
依次判断采样MST中的边（从小到大） 不构成环 就加进去 否则的话 舍弃
大于的时候 把起点和终点插入MST中