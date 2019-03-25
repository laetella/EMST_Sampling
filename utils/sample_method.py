#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2018-10-13 10:29:54
# updateDate: 2018-10-13 17:30
# described: basic sample method 

# random 包中有sample 函数 可以实现简单随机抽样
# scipy.misc.imresize 
# scipy.ndimage.zoom   Resampling a numpy array representing an image
# 双线性插值与采样的关系

#简单的随机抽样 随机的抽取200个
def rand_sample(file):
    data = np.loadtxt(file)
    num_sample = len(data)
    indexs = list(range(num_sample))
    rand_index = random.sample(indexs,200)
    new_sample = data[rand_index]
    print(new_sample)

#等距抽样
def Equidistant_sample(file):
    new_data = []
    data = np.loadtxt(file)
    num_sample = 200 #抽取的样本的个数
    num_data = len(data) #共有的样本的数量
    step_size = int(num_data/num_sample) #每一步的长都
    for i in range(num_sample):
        new_data.append(data[i*step_size])
    print(new_data)

#分层抽样
def layer_sample(file):
    data = np.loadtxt(file) #导入带有标签的数据
    each_sample_count = 20 #定义每层 抽样的个数
    unique_labels = np.unique(data[:,-1])

    new_data = [] #用于存放最后的数据

    for value in unique_labels: #遍历每一个不同的标签
        label_data = [] #暂时的存放对应的标签的数据
        for row in data:
            if row[-1] == value:
                label_data.append(row)
        sample = random.sample(label_data,each_sample_count)
        new_data.extend(sample) #因为sample为[[],[],[]]的形式所以用extend
    print(new_data)

#整群抽样就是随机的抽缩几个类别对应的所有的数据
def Whole_group_sample(file):
    data = np.loadtxt(file)
    unique_labels = np.unique(data[:,-1])
    rand_label = random.sample(list(unique_labels),2) #抽取两个类的数据,因为sample无法抽取张量里面的所以转换成list
    new_data = []
    for value in rand_label:
        for row in data:
            if row[-1] == value:
                new_data.append(row)
    print(new_data)

# 下采样 以不同频率进行采样
def low_sample(filename):
    index = pd.date_range('1/1/2000', periods=4096, freq='T')  #这个起始时间任意指定，freq为其频率
    data = pd.read_table(filename, names=['feat'])
    data.index = index
    data_obj = data.resample('4T', label='right')  #第一个为抽样频率，label表示左右开闭区间
    data_new = data_new.asfreq()[0:]

if __name__ == "__main__" :
    Whole_group_sample('data4.txt')
