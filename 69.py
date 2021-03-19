from array import *
arr=[1,2,3,4,5,6,7,8,9]
a=max(arr)
b=min(arr)
print("max is:",a)
print("min is:",b)

#take an input from the user and print an array and find max min values

from array import *
arr=array('i',[])
n=int(input("enter the length of the array"))
for i in range(n):
    x=int(input("enter an array element"))
    arr.append(x)
print(arr)

Max=max(arr)
print("max value of array is:",Max)
Min=min(arr)
print("min value of array is:",Min)




