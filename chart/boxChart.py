#coding=utf-8
# Created by feizi at 2017/2/10

import matplotlib.pyplot as plt
import numpy as np

# 箱状图
np.random.seed(1000)
data = np.random.normal(size=(1000, 4), loc=0, scale=1)
labels = ['A', 'B', 'C', 'D']
plt.boxplot(data, labels=labels)
plt.show()
