#using recursion find the factorial of n
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    
n=4
n=5
n=10
if n<0:
    print("sorry negative cont exist")
elif n==0:
    print("factorial of 0 is 1")
else:
    print("factorial of {0} is {1}".format(n,fact(n)))
