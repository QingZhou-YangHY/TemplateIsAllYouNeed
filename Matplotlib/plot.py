import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])


# plt.plot(xpoints, ypoints, 'o')

# plt.show()
"""
颜色字符：'b' 蓝色，'m' 洋红色，'g' 绿色，'y' 黄色，'r' 红色，'k' 黑色，'w' 白色，'c' 青绿色，'#008000' RGB 颜色符串。多条曲线不指定颜色时，会自动选择不同颜色。

线型参数：'‐' 实线，'‐‐' 破折线，'‐.' 点划线，':' 虚线。

标记字符：'.' 点标记，',' 像素标记(极小点)，'o' 实心圈标记，'v' 倒三角标记，'^' 上三角标记，'>' 右三角标记，'<' 左三角标记...等等。

如果我们要绘制坐标 (1, 3) 到 (8, 10) 的线，我们就需要传递两个数组 [1, 8] 和 [3, 10] 给 plot 函数：
"""


x = np.arange(0,4*np.pi,0.1)   # start,stop,step
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,x,z)
plt.show()