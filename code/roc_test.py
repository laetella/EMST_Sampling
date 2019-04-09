#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2018-10-10 08:51:44
# updateDate: 2018-10-10 08:51:44
# described: 

#绘制二分类ROC曲线
import pylab as pl
# %matplotlib inline
from math import log,exp,sqrt

evaluate_result = "D:/python_sth/1.txt"
db = []
pos , neg = 0 , 0
with open(evaluate_result , 'r') as fs:
    for line in fs:
        nonclk , clk , score = line.strip().split('\t')
        nonclk = int(nonclk)
        clk = int(clk)
        score = float(score)
        db.append([score , nonclk , clk])
        pos += clk
        neg += nonclk

db = sorted(db , key = lambda x:x[0] , reverse = True) #降序

#计算ROC坐标点
xy_arr = []
tp , fp = 0. , 0.
for i in range(len(db)):
    tp += db[i][2]
    fp += db[i][1]
    xy_arr.append([tp/neg , fp/pos])

#计算曲线下面积即AUC
auc = 0.
prev_x = 0
for x ,y in xy_arr:
    if x != prev_x:
        auc += (x - prev_x) * y
        prev_x = x
print "the auc is %s."%auc
x = [_v[0] for _v in xy_arr]
y = [_v[1] for _v in xy_arr]
pl.title("ROC curve of %s (AUC = %.4f)" % ('svm' , auc))
pl.ylabel("False Positive Rate")
pl.plot(x ,y)
pl.show()


# another  method
def drawRoc(weights,testLabels,testSet):
    testSet= mat(testSet)   #list转换成矩阵类型
    m, n = shape(testSet)   #训练集的行数和特征个数
    FPR = zeros((101,1))    #1-specificity
    TPR = zeros((101,1))    #sensitivity
    probability = zeros((m,1))#每个样本的概率
    for j in range(101):      #求Roc图像的每一个点
        TP = 0  # true positive
        FN = 0  # ture negative
        FP = 0  # false positive
        TN = 0  # true negative
        threshold = float(j / 100.0)
        for i in range(m):
            dataSet = testSet[i]
            dataSet = dataSet.transpose()
            probability[i] = sigmoid(dot(weights,dataSet))#求每个样本的概率
            #print('pro = ',probability[i])
            if probability[i] > threshold:
                value = 1
            else:
                value = 0
            if abs(testLabels[i]-1.0)<1e-7 and abs(value-1.0)<1e-7:#true positive
                TP = TP + 1
            elif abs(testLabels[i]-1.0)<1e-7 and abs(value-0.0)<1e-7:#false positive
                FN = FN + 1
            elif abs(testLabels[i]-0.0)<1e-7 and abs(value-0.0)<1e-7:#true negative
                TN = TN + 1
            elif abs(testLabels[i]-0.0)<1e-7 and abs(value-1.0)<1e-7:#false positive
                FP = FP + 1
        TPR[j] = float(TP/(TP+FN))
        FPR[j] = float(FP/(TN+FP))
    # print(TPR)
    # print(FPR)
    roc_auc = auc(FPR, TPR)
    print('Auc=',roc_auc)
    plt.plot([0, 1], [0, 1], '--', color=(0 , 0, 1))#画对角线
    plt.plot([0, 1], [0, 0], '-', color=(0, 0, 1))#画x轴
    plt.plot([1, 1], [0, 1], '-', color=(0, 0, 1))#画边界
    plt.plot(FPR, TPR, "b", linewidth=1)#在当前绘图对象绘图，蓝线
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic curve')
    plt.show()#显示图像
