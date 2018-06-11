'''
from sklearn.datasets import load_iris
iris = load_iris()

print(iris.data.shape)                   # (150, 4)
n_samples, n_features = iris.data.shape
print(n_samples)                         # 150個樣本
print(n_features)                        # 4個不同特徵
print(iris.data[0])                      # [5.1 3.5 1.4 0.2]

print(iris.target.shape)
print(iris.target)
'''
# Load the data
from sklearn.datasets import load_iris
iris = load_iris()

from matplotlib import pyplot as plt

# The indices of the features that we are plotting
x_index = 0
y_index = 1

# this formatter will label the colorbar with the correct target names
formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

plt.figure(figsize=(5, 4))
plt.scatter(iris.data[:, x_index], iris.data[:, y_index], c=iris.target)
plt.colorbar(ticks=[0, 1, 2], format=formatter)
plt.xlabel(iris.feature_names[x_index])
plt.ylabel(iris.feature_names[y_index])

plt.tight_layout()
plt.show()