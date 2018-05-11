a = [3, "1", 4, 2]
# 印出 a 的第 3 個元素
print(a[2])
print()

# 印出 a 的倒數第 1 個元素
print(a[-1])
print()

# 在 a 的最後新增一個數字 5 之後印出 a 的內容
a.append(5)
print(a)
print()

# a[1] = 1 之後印出 a 的內容
a[1]=1
print(a)
print()

# 建立一個新的 list b, 內容為 a 的第 2 到第 3 個元素
b = a[2:4]
print(b)
print()

# 建立一個新的 list c, 內容為 a 的第 2 到最後一個元素
c = a[2:]
print(c)
print()

# 建立一個新的 list d, 內容為 a 的第 1 到倒數第 2 個元素
d = a[1:-1]
print(d)
print()

# 建立一個新的 list e, 內容為 a 的第 2 到倒數第 2 個元素
e = a[2:-1]
print(e)
print()

# 建立一個新的 list f, 內容和 a 完全相同, 請驗證修改 f 不會修改到 a, 並想一想直接用等號將 f 指定為 a 有什麼不同?
f=[]
for el in a:
    f.append(el)
f[0]=99
print(a,f,sep="\n")
print()

# 建立一個新的 list g, 內容為 a 原本的內容但最後加上 [10, 20] 例如: a 為 [3, 1, 4, 2, 5], 加上 [10, 20] 後變成 [3, 1, 4, 2, 5, 10, 20]
g = a+[10,20]
print(g)
print()

# 將 a 中的從位置 2 到 3 的部份代換為 [7, 8, 9] 之後印出 a 的內容. 例如: a 為 [3, 1, 4, 2, 5], 代換後變成 [3, 1, 7, 8, 9, 5]
a[2:4]=[7,8,9]
print(a)
print()
