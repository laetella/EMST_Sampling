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

sklearn 数据加载工具 产生数据集

可以尝试其他的采样方法优化实验结果

python 绘制ROC曲线 (需要计算yscore， 根据analysis cluster中真正例计算指标)
yscore 怎么得到 ：sklearn 内置的聚类模型 fit 得到的结果就是
表示每个测试样本属于正样本的概率 如何预测每个样本的概率呢？我的分类器并不能得到每个样本的概率值
你可以试一下这样，在一个数据集上有N个类，C1,C2,C3...CN，对其中一个类C1，总共有N1个数据。
你在聚类结果中把这N1个数据提取出来，它们现在按某一种聚类算法A被标号为类1、类2、类3等。假设类1为正确标号，那么被标为其他类标号的都是误标。

对这N1个数据，提取其中n1个，然后用另一种算法B在同样的数据集上画出曲线BC1，这样就可得到不同的算法在某个数据集某个类上的ROC图。

想用MSTClustering的包，直接在上面改mst的算法，但是这个包好像也不能得到预测概率，只能得到类标号
所以基于MST的聚类画ROC好像有点困难
考虑一下用其他的评估标准。

5.29 投稿
5.27 完成修改、完善
5.25 摘要 引言  结论
5.23 相关工作 写related work查找sampling相关的论文
5.21 实验结果评价
5.19 算法描述
5.17  高维大数据
5.16  低维小数据
Rand Index度量的正确的百分比

RI = （TP+TN）/（TP+FP+FN+TN）
Precision=TP/(TP+FP)

Recall=TP/(TP+FN)

F1=2×Recall×Precision/(Recall+Precision)
adjusted_mutual_info_score  
arcene 0.0562
appendicitis 0.0016

采样方法的完善 
进一步做实验 多个二维数据
进行评估 （低维数据）? 基于MST的聚类结果都差不多 需要先评价MST，用edge-error 和 weight-error来评价
图像数据上的实验

找对比算法 对比结果

写相关工作

contraceptive-method-choice 不能做byte运算