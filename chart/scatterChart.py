#coding=utf-8
# Created by feizi at 2017/2/10

import matplotlib.pyplot as plt
import numpy as np

# 散点图
x = np.random.randn(1000)
y = x + np.random.randn(1000) * 0.5

# s表示面积，marker表示图形
plt.scatter(x, y, s = 5, marker='<')
plt.show()