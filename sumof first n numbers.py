#to print sum of  given first n numbers
n=int(input("enter n value"))
N=(n*(n+1))/2
print("the sum of given {0} numbers is {1}".format(n,N))


#using function
def sum(n):
    N=(n*(n+1))/2
    return N
print(sum(25))