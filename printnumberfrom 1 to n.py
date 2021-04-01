#to print numbers from 1 to n
n=int(input("enter the n value"))
for i in range(1,n+1):
    print(i,end=' ')

#using function
def number(n):
    for i in range(1,n+1,1):
        print(i,end=" ")
number(15)
number(25)
