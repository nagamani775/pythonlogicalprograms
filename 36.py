#to print right angle triangle in reverse order
n=int(input("enter the no.of rows"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print('*',end=" ")
    print()