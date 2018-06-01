import numpy as np
import matplotlib.pyplot as plt

arr = np.arange(10)
#print(arr)
#print(arr.ndim)
#print(arr.shape)

arr2 = np.arange(5,100,3) # 5開始100結束，每+3跑出一個數字
#print(arr2)
arr2_1 = arr2*2
#print(arr2_1)

arr3_x = np.arange(10,50,3)
arr3_y = arr3_x*2+5
#print(arr3_x)
#print(arr3_y)

arr4_x = np.linspace(0,10,21) # 0到10切成20個點，寫21是因為要包含最後一個點
arr4_y1 = arr4_x *2
arr4_y2 = arr4_x *3
#print(arr4_x)

plt.plot(arr4_x,arr4_y1,'-rv',arr4_x,arr4_y2,'--bo')
plt.show()