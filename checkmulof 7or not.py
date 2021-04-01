#to print whether the number is multiplication of 7 or not
a=int(input("enter a value"))
if a%7==0:
    print("{0} is multiplication of 7".format(a))
else:
    print("{0} is not multiplication of 7".format(a))

#using function
def mul_of_7(a):
    if a%7==0:
        print("{0} is multiplication of 7".format(a))
    else:
        print("{0} is not multiplication of 7".format(a))
    

mul_of_7(77)