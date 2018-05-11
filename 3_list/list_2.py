'''Prob 1'''
def prlist(arr):
    for idx,el in enumerate(arr):
        if(idx != len(arr)-1):
            print(el,end=",")
        else:
            print(el)

a = [10,20,30,40,50]
prlist(a)

'''Prob 2'''
def enumList(arr):
    for i from 1 to len(arr):
        print(i+". "+enumList[i-1])
    print()

enumList(['apple','banana','orange'])