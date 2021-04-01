#program to print thier division
n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
print("the division is:",n1/n2)

#using function
def div(a,b):
    c=a/b
    return c
a=int(input("a value"))
b=int(input("b value"))
print(div(a,b))