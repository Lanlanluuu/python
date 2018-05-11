nums = list(range(5,0,-1))
print(nums)

nums[2]=100
print(nums)

a = [1,2,3]
total=0

for el in a:
    total+=el
# sum = 把list中的數都加起來
total2 = sum(a)
print(total,total2)

# range(start, stop, 數的變化)
b = range(5,0,-1)
# b = range(5,4,3,2,1) => 從5開始，0結束，一次(-1)
total3 = sum(b)
print(total3)

strA = "Stone"
# 沒辦法直接 strA[0]="Y"
# 轉成list才能改裡面的東西
strA = list(strA)
strA[0]="Y"
# 轉回string再輸出 ( ''.join(list) )
print(''.join(strA))
print(','.join(strA))