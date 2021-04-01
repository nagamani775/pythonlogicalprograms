#take an input from the user and print an array in reverse 

from array import *
arr=array('i',[])
n=int(input("enter the length of the array"))
for i in range(n):
    x=int(input("enter an array element"))
    arr.append(x) 
print(arr)
arr.reverse()
print(arr)






