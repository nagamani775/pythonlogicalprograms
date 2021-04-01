#to print number is less or greater or equal to ten
a=int(input("enter a value"))
if a>10:
    print("{0} is greater than 10".format(a))
elif a<10:
    print("{0} is less than 10".format(a))
else:
    print("{0} is equal to 10".format(a))

#using function
def large(a):
    if a>10:
        print("{0} is greater than 10".format(a))
    elif a<10:
        print("{0} is less than 10".format(a))
    else:
        print("{0} is equal to 10".format(a))

large(100)