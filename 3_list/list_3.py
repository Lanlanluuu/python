# 試著使用 range() 函數建立以下 list:

''' range(start, stop, 數的變化) 
    range(5,0,-1) => 從5開始，0結束，一次(-1) '''

# list1 內容為 [0, 1, 2, 3, 4]
# list2 內容為 [2, 3, 4, 5, 6]
# list3 內容為 [1, 3, 5, 7, 9]
list3= list(range(1,9,2))
print(list3)

# list4 內容為 [5, 4, 3, 2, 1]
list4 = list(range(5,0,-1))
print(list4)