# An efficient MST-based clustering algotrithm based on sampling

# Highlight
1. 用到求最近邻的方法covertree 
2. 用多个采样方法

1. 对比算法：查找AMST相关文献对比1+elpson以及边的权重和时间
3. 

之前的MST算法都是先构造一个完全图 再计算MST 这样效率比较低，我们提出了一种采样 不需要构造完全图的方法
  可以写成类似于sklearn中的形式 给一个数据集，下面好几种聚类方法，画到一个图中 

3.28 实现第二种采样方法
Second Method：
2.  不能简单的连起来最近邻  因为这样连起来 孤立的component太多了
需要增加一些判断 比如：选择一个起始点 按最近邻加进去 （直接用基于KNN的MST）
3. 先找到剩下的点构成的图中最长的边
依次判断采样MST中的边（从小到大） 不构成环 就加进去 否则的话 舍弃
大于的时候 把起点和终点插入MST中

第二种采样方法的效果不好 
采样点太少的时候有问题 连接最近邻可能导致孤立的线段

3.31 在图像数据上对比结果
找原来提取图像数据的代码 改为在python上实现
运行图像数据 获取label 之后再用CV2画出来

用层次聚类的方法实现PNNG  测试时间效率  Bi-means

为什么2018年的文章说kruscal比prim高效呢？
实现所有的MST算法 对比效率

如何一次画同一数据集的四个图来同时对比四种算法

python 包里有相关的聚类质量评价指标 
ROC 画图等 
参考2018的文章 Edge error weight error 来评价

python 在图的左上角标号