#to add lower sum of matrix


#to accept M by N matrix and print upper triangular matrix addition

def sum(mat,r,c):
    i,j=0,0
    upper_sum=0
    lower_sum=0
    for i in range(0,r):
        for j in range(0,c):
            if (i>=j):
                lower_sum=lower_sum+mat[i][j]
    print("lower sum is:",lower_sum) 
    


a=[[1,2,3],
   [4,5,6],
   [7,8,9]]

sum(a,3,3)

            



