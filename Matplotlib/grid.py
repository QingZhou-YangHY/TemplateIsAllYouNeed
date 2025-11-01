import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])


plt.title("RUNOOB grid() Test")
plt.xlabel("x - label")
plt.ylabel("y - label")

plt.plot(x, y)


"""
matplotlib.pyplot.grid(b=None, which='major', axis='both', )
grid(color = 'color', linestyle = 'linestyle', linewidth = number)
"""
plt.grid(color = 'r', linestyle = '--', linewidth = 0.5)

plt.show()