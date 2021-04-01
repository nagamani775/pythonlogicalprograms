#program to print thier multiplication
n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
print("the multiplication is:",n1*n2)

#using return statement
def mul(a,b):
    c=a*b
    return c

print(mul(12,13))

#using fuction statement take input  from th user
def mul(a,b):
    c=a*b
    return c
a=int(input("a value"))
b=int(input("b value"))
print(mul(a,b))