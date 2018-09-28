#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# author: LiJia
# email: laetella@outlook.com
# date: 2018-06-08 08:57:11
# updateDate: 2018-06-08 08:57:11
# described:  main test

from __future__ import division
from sklearn.cluster import Birch, AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster, distance,maxinconsts, inconsistent, single
from sklearn.datasets.samples_generator import make_blobs
import numpy as np
import scipy.cluster.hierarchy as hac
from math import sqrt
from random import randint
import pandas as pd
import math  
import matplotlib.pyplot as plt  

from distance import *
from file_operation import *
from plt import *
