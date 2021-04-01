#  * * *    
#   * *
#    *
n=int(input("enter rows"))

for i in range(1,n+1):
    print(" "*(i-1),end="")
    for j in range(1,n+2-i):
        print("*",end=" ")
    print()