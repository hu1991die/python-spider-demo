#coding=utf-8
# Created by feizi at 2017/2/10

import matplotlib.pyplot as plt
import numpy as np

# 饼状图
labels = 'A', 'B', 'C', 'D'
fracs = [15, 30, 45, 10]
# 使x y轴比例相同
plt.axes(aspect = 1)
# 突出某一部分区域
explode = [0, 0, 0, 0.05]
# autopct显示百分比
plt.pie(x = fracs, labels=labels, autopct='%.0f%%', explode=explode)
plt.show()

