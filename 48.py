#check whether the number is prime or not
n=int(input("enter n value"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    print("the given {0} is a prime number".format(n))      
else:
    
    print("the given {0} is  not a prime number".format(n))      
