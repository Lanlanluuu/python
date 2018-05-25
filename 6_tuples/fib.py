# 1,1,2,3,5,8,13,......

def fib(n):
    a = 0
    b = 1
    for i in range(1, n):
        a, b = b, a+b
    return b

print(fib(3))
print(fib(5))
print(fib(7))
print(fib(99))