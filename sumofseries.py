#print 1/1!+2/2!+3/3!......
n=int(input("enter n value"))
fact=1
sum=0
for i in range(1,n+1):
    fact*i=fact
    sum=sum+i/fact
print("sum is:",sum)