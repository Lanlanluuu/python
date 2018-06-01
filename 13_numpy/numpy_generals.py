import numpy as np

mat1 = np.zeros((3,4))
#print(mat1)
#print(mat1.ndim)
#print(mat1.shape)

mat2 = np.ones((3,3)) * 2
mat2_2 = mat2 * 2
mat2_3 = mat2 * mat2_2 
mat2_4 = np.matmul(mat2,mat2_2)
#print(mat2)
#print(mat2_2)
#print(mat2_3)
#print(mat2_4)

mat3 = np.eye(3)
#print(mat2)
#print(mat3)
#print(mat2*mat3)
#print(np.matmul(mat2,mat3))

import matplotlib.pyplot as plt
arr_x = np.arange(10)
a = np.random.rand(10)      
b = np.random.randint(5, 10, 10) 
plt.plot(arr_x, a,'-r^',arr_x, b,'--go')
plt.show()