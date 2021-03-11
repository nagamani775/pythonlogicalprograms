
n=int(input("enter rows"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(chr(64+n+1-i),end=" ")
        if i>=2:
            print(" "*(2*i-4),end="")
            for k in range(i,i+1):
                print(chr(64+n+1-i),end=" ")
        print()