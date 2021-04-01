a=int(input("enter a value"))
if a%2==0:
    print("{0} is even number ".format(a))
else:
    print("{0} is odd number ".format(a))

#using function
def even_odd(a):
    if a%2==0:
        print("{0} is even number ".format(a))
    else:
        print("{0} is odd number ".format(a))

even_odd(25)