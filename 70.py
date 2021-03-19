#to print fabanocci series using upto nth term of arrays

from array import *
arr=array('i',[])
n=int(input("n value "))
a=0
b=1
for i in range(n):
    arr.append(a)
    temp=a
    a=b
    b=b+temp
print(arr)
