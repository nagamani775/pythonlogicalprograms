#to print sum of  given first n numbers
n=int(input("enter n value"))
N=(n*(n+1))/2
print("the sum of given {0} numbers is {1}".format(n,N))


#using function
def sum(n):
    N=(n*(n+1))/2
    return N
print(sum(25))

#using loop
n=int(input("enter n value"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
    
