#to print factorialo of number
n=int(input("enter number"))
factorial=1
if n<0:
    print("factorial does not exist")
elif n==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,n+1):
        factorial=factorial*i
    print("the factorial of {0} is {1}".format(n,factorial))

