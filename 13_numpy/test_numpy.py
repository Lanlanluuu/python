import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3, 20)
# 0 到 3 切成 20 個點
y = np.linspace(0, 9, 20)
# 0 到 9 切成 20 個點
print(x)
print(y)
plt.plot(x, y,"ro")
plt.show()