#to print first even numbers
def even(n):
    for i in range(1,n+1):
        if i%2==0:
            print(i,end=" ")
        else:
            continue

n=int(input("enter n value"))
even(n)
