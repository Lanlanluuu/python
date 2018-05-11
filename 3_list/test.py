# 2 3 4
x=[2,3,4]
for i in x:
    print(i,end=" ")
print()

# i is position
# range(len(x)) = range(0, len(x), 1)
# 2 3 4
for i in range(len(x)):
    print(x[i],end=" ")
print()

# idx & value
# 1:2 , 2:3 , 3:4
for idx, i in enumerate(x):
    print(idx+1,i,sep=":")
print()

# add 5 behind x
# [2,3,4,5]
x.append(5)
print(x)
print()

# z is new list
#[2,3,4,5]
#[1,2]
#[2,3,4,5,1,2]
y=[1,2]
z=x+y
print(x,y,z,sep="\n")

# x & z is the same list
#[99,3,4,5]
z=x
z[0]=99
print(x,z,sep="\n")

# y is list
x.append(y)
print(x)
print()

#
print(len(x))
print(x[len(x)-1])
print(x[-1])
print()

#
print(x)
x[2:3]=[90,91,92]
print(x)
print()