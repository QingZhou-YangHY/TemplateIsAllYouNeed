"""
matplotlib.pyplot.hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None, 
histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, **kwargs)
"""

import matplotlib.pyplot as plt
import numpy as np

# 生成三组随机数据
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(2, 1, 1000)
data3 = np.random.normal(-2, 1, 1000)

# 绘制直方图
plt.hist(data1, bins=30, alpha=0.5, label='Data 1')
plt.hist(data2, bins=30, alpha=0.5, label='Data 2')
plt.hist(data3, bins=30, alpha=0.5, label='Data 3')

# 设置图表属性
plt.title('RUNOOB hist() TEST')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

# 显示图表
plt.show()

# 结合 Pandas 来绘制直方图：

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
 
# # 使用 NumPy 生成随机数
# random_data = np.random.normal(170, 10, 250)
 
# # 将数据转换为 Pandas DataFrame
# dataframe = pd.DataFrame(random_data)

# # 使用 Pandas hist() 方法绘制直方图
# dataframe.hist()
# or
# 生成随机数据
# data = pd.Series(np.random.normal(size=100))

# 绘制直方图
# bins 参数指定了直方图中的柱子数量
# plt.hist(data, bins=10)




# # 设置图表属性
# plt.title('RUNOOB hist() Test')
# plt.xlabel('X-Value')
# plt.ylabel('Y-Value')

# # 显示图表
# plt.show()