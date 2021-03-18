from array import *
arr=array('i',[])
n=int(input("n value "))
a=0
b=1
for i in range(n):
    arr.append(a)
    #print(arr)
    temp=a
    a=b
    b=b+temp
print(arr)
