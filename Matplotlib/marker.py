import matplotlib
import matplotlib.pyplot as plt
import matplotlib.markers
import numpy as np

"""
fmt 参数定义了基本格式，如标记、线条样式和颜色

markersize，简写为 ms：定义标记的大小。
markerfacecolor，简写为 mfc：定义标记内部的颜色。
markeredgecolor，简写为 mec：定义标记边框的颜色。

"""

ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, marker = 'o', ms = 10, mec = 'r', mfc = 'r')
plt.show()