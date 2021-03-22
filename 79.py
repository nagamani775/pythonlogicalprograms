
#multuplication of two matrices
a=[[1,2,3],
   [4,5,6],
   [7,8,9]]

b=  [[1,2,3],
     [4,5,6],
     [7,8,9]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

import numpy as np

result=np.dot(a,b)
print(result)
