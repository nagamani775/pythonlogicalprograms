#take input from the user and print array elements in ascending and decending order
arr=[2,1,3,4,5,6]
print(arr)
arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)

#using numpy
import numpy as np
arr=np.sort([9,8,7,4,5,6,3,2,1])
print(arr)
#create a two dimentional array
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1)
#create 3D array
arr2=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr2)
