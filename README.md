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
../data/low dimension/arcene.arff : size:  200 , Attributes:  10001
2018 Fast AMST Jothi using time:  281.21600008
[0.5137688442211056, 0.026637537702602465, 0.3684897532959144, 0.404123179252221
4]

3.31 在图像数据上对比结果
找原来提取图像数据的代码 改为在python上实现
运行图像数据 获取label 之后再用CV2画出来