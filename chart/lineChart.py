#coding=utf-8
# Created by feizi at 2017/2/10

import matplotlib.pyplot as plt
import numpy as np

# 折线图
x = np.linspace(-10, 10, 100)
y = x ** 3
plt.plot(x, y, linestyle='--', color='green', marker='<')
plt.show()
