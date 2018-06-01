import numpy as np
'''
def table(m,n):
    arr=[]
    for i in range(0,m):
        # append = 輸入
        arr.append([1*(i+1),2*(i+1),3*(i+1),4*(i+1),5*(i+1)])
    return np.array(arr)
'''
def table(m,n):
    arr=[]
    for i in range(1,m+1):
        sub=[] # 形成陣列條(一維)
        for j in range(1,n+1):
            sub.append(i*j) # 輸入陣列元(一個)
        arr.append(sub) # 包成完整的二維陣列
    return np.array(arr)

def table2(m,n):
    arr = [ [i*j for j in range(1, n+1)] for i in range(1, m+1)]
    return np.array(arr)

def test():
    arr = table(4,5)
    print(arr)
    print(arr.ndim) # 陣列維度
    print(arr.shape) # 陣列大小

def test2():
    nparr = table(4,5)
    print(nparr)

test()