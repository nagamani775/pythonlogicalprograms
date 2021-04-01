#to print swap the values
a=int(input("enter the a value"))
b=int(input("enter the b  value"))
a,b=b,a
print("after swapping:",a,b)

#using temp variable
a=int(input("enter the a value"))
b=int(input("enter the b  value"))
print("before swapping:",a,b)
temp=a
a=b
b=temp
print("after swapping:",a,b)

#using function 
def swap(a,b):
    a,b=b,a
    return a,b

a=int(input("enter a value"))
b=int(input("enter b value"))
print(swap(a,b))

#using function with temp variable
def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b

a=int(input("enter a value"))
b=int(input("enter b value"))
print(swap(a,b))

#using 3 variables
def swap(a,b,c):
    temp=a
    a=b
    b=c
    c=temp
    return a,b,c

a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))

print(swap(a,b,c))