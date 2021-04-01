#to print a right angle triangle patren
n=int(input("enter the no.of rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=" ") 
    print()