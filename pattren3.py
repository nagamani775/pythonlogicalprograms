n=int(input("enter rows"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for p in range(1,n):
    print(" "*p,end="")
    for j in range(1,n+1-p):
        print("*",end=" ")
    print()