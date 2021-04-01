#to print first odd numbers
def Odd(n):
    for i in range(1,n+1):
        if i%2!=0:
            print(i,end=" ")
        else:
            continue
Odd(30)