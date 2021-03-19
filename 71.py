#print positive and negative numbers seperately
from array import *
arr=array('i',[1,2,3,4,-7,8,-9])
arr1=[]
arr2=[]
x=len(arr)
for i in range(x):
    if arr[i]>=0:
        arr1.append(arr[i])
        print(arr1)
    else:
        arr2.append(arr[i])
        print(arr2)


#take input from user and seperate negative and positive numbers in seperate ayyays
from array import *
n=int(input("enter length of an array"))
arr=array('i',[])
for i in range(n):
    x=int(input("enter an array element"))
    arr.append(x)
print(arr)
arr1=[]
arr2=[]
x=len(arr)
for i in range(x):
    if arr[i]>=0:
        arr1.append(arr[i])
        print(arr1)
    else:
        arr2.append(arr[i])
        print(arr2)

def arr():
    arr1=[]
    arr2=[]
    for i in range(len(arr)):
    if arr[i]>=0:
        arr1.append(arr[i])
        print(arr1)
    else:
        arr2.append(arr[i])
        print(arr2)

arr([1,2,3,-,4,5,-9,8,-7])

#using array function

from array import *
arr=array('i',[])
def Arr(arr):
    arr1=[]
    arr2=[]
    for i in range(len(arr)):
        if arr[i]>=0:
            arr1.append(arr[i])
            print(arr1)
        else:
            arr2.append(arr[i])
            print(arr2)

Arr([1,2,3,4,5,-9,8,-7])
