import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4])
y = np.array([1,4,9,16])
plt.rcParams['font.family']=['STFangsong']

plt.plot(x,y)

# 我们可以使用 xlabel() 和 ylabel() 方法来设置 x 轴和 y 轴的标签
# 我们可以使用 title() 方法来为图表添加标题
plt.title("Label Example Title")

plt.xlabel("x - label")
plt.ylabel("y - label")

plt.show()
# from matplotlib import pyplot as plt
# import matplotlib
# a=sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])

# for i in a:
#     print(i)