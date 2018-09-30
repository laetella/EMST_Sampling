# EMST_Sampling
improving the efficiency of emst algorithm with sampling

# 9.28
思路： 结合之前做的EMST的算法，用采样的方法提高效率

 用 小得多的样本表示大数据集

 分组， 或者分层
 思路： 缩小数据集，
 1. 对所有数据，计算相似性， 相似的点删除，
 2. 对于剩下的点（即采样得到的点）计算MST，并进行聚类
 3. 把相似的点加进聚类结果中
 可以采用  相似的点要进行标记