import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])

# plt.plot(ypoints, linestyle = 'dotted', c = 'SeaGreen', linewidth = '1.5')
# linestyle 可以简写成ls，后面的类型同样可以简写
# 当然我这里并没有遵守编程规范，可能会引发编程战争，不要骂我~

y1 = np.array([3, 7, 5, 9])
y2 = np.array([6, 2, 13, 10])

plt.plot(y1)
plt.plot(y2)
plt.show()