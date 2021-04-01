#to print he simple interest
P=int(input("enter P value"))
N=int(input("enter N value"))
R=int(input("enter R value"))
SI=(P*N*R)*0.01
print("the simple interest is:",SI)

#using function
def SI(p,n,r):
    S=(p*n*r)/100
    print(S)

SI(4,3,4)

#using function an dtake input from the user
def SI(p,n,r):
    S=(p*n*r)/100
    print(S)

p=int(input("p value"))
n=int(input("n value"))
r=int(input("r value"))
SI(p,n,r)