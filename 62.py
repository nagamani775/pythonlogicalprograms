#to find factorial prime or not and fabanocci series using functions
#to define funcyion by compute a factorialof a number
def fact(n):
    fact=1
    for i in range(n,0,-1):
        fact=fact*i
    print(fact)
fact(4)
fact(9)
fact(5)



#check wheather its aprime or not using a function
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        print("prime")
    else:
        print("not a prime")

prime(3)
prime(10)


#fabanocci series using functions

def fabnocci(n):
    a,b=0,1
    for i in range(1,n+1):
        print(a)
        temp=a
        a=b
        b=b+temp

fabnocci(5)
fabnocci(8)
