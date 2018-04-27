def bmi(kg,m):
    return kg / (m*m)

def check(kg,m=2,name="guest"):
    b=bmi(kg,m)
    print(name,'BMI',b)

check(60,1.5,name="bob")
check(60,1.5)