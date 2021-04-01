#program to print thier subtraction
n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
print("the subtration is:",n1-n2)

#using function take input from the user
def sub(n1,n2):
    n3=n1-n2
    print(n3)
n1=int(input("enter n1 value"))
n2=int(input("enter the n2 value"))
sub(n1,n2)

#using return statement

def sub(a,b):
    c=a-b
    return c

print(sub(12,13))