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