#to print the largest of two numbers
a=int(input("enter a value"))
b=int(input("enter b value"))
if a>b:
    print("{0} is largest number than {1}".format(a,b))
else:
    print("{0} is large than {1}".format(b,a))

#using function
def large(a,b):
    if a>b:
        print("{0} is greater than {1}".format(a,b))
    else:
        print("{0} is small than {1}".format(a,b))
#calling the function      
large(10,20)