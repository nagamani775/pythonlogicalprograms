

#write a program to accept m by n matrix and reprint in matrix
n=[[1,2,3],[4,5,6],[7,8,9]]
for r in n:
    print(r)
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[i][j],end=" ")
    print()


    #using numpy
import numpy as np
a=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(a)



