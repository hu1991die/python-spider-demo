#coding=utf-8
# Created by feizi at 2017/2/10

import matplotlib.pyplot as plt
import numpy as np

# 条形图
y = [20, 10, 30, 25, 15]
index = np.arange(5)
plt.bar(left=index, height=y, color='green', width=0.5)
plt.show()