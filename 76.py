#To accept M by N matrix and print their addition of diagonals
def sum(matrix,n):
    primary=0
    secondary=0
    for i in range(0,n):
        for j in range(0,n):
            if i==j:
                primary=primary+matrix[i][j]

            if ((i+j)==(n-1)):
                secondary=secondary+matrix[i][j]
    print("diagonal of forward direction is:",primary)
    print("diagonal of backword is:",secondary)

a=[[1,2,3],
   [4,5,6],
   [7,8,9]]

sum(a,3)