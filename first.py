print(1)
print("ABC")
print(9%2)

print("{0:<7}{1:<7}{2:<7}".format(1234, 567, 8999)) # <靠左對齊,7佔7個字元
print("{0:>7}{1:>7}{2:>7}".format(1234, 567, 8999)) # <靠右對齊,7佔7個字元
print("{0:10}{0:10}".format(200, 300))

s = "Stone Campus"
#這個字串的長度
print(len(s))
#位置６的字母（使用[]）
print(s[6])
#從位置 3 到位置 9 的子字串"ne Campus （使用[:]）
print(s[3:10])
# 從位置 3 到 最後 的字串
print(s[3:])
# 
# 
#