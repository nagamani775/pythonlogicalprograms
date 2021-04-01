#program to accept values from the keyboard of two numbers and print thier addition
n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
print("the adition is:",n1+n2)

#using function using return statment
def add(n1,n2):
    n3=n1+n2
    return n3

print(add(45,65))

#using print statement
def add(n1,n2):
    n3=n1+n2
    print(n3)

add(45,65)

#take input from the user using function
def add(n1,n2):
    n3=n1+n2
    print(n3)
n1=int(input("enter n1 value"))
n2=int(input("enter the n2 value"))
add(n1,n2)