#coding=utf-8
# Created by feizi at 2017/2/10

import matplotlib.pyplot as plt
import numpy as np

# 直方图
mu = 100
sigma = 20

# 样本数量
x = mu + sigma * np.random.randn(20000)

# bins 显示有几个直方，normed是否对数据进行标准化
plt.hist(x, bins=10, color='green', normed=True)
plt.show()




