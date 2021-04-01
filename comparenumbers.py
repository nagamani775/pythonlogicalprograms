#compare two numbers
def comp(a,b):
    if a>b:
        print("{0} is greatr than {1}".format(a,b))
    elif b>a:
        print("{0} is greatr than {1}".format(b,a))
    else:
        print("both are equal")

a=int(input("enter the first number"))
b=int(input("enter the second number"))
comp(a,b)